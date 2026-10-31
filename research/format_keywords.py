"""Format an Ahrefs keyword export by difficulty and flag the big, immediate opportunities.

Usage: python format_keywords.py <input.xlsx> [output.xlsx]

Colours: Easy = green, Medium = yellow, Hard = red, unknown KD = grey,
"Big & immediate" (Easy KD with >= 1,000 searches/month) = purple.
"""
import collections
import sys
from pathlib import Path

import openpyxl
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

BIG_MIN_VOLUME = 1_000

FILL = {
    "big": PatternFill("solid", fgColor="C4B5FD"),  # purple
    "Easy": PatternFill("solid", fgColor="BBF7D0"),  # green
    "Medium": PatternFill("solid", fgColor="FEF08A"),  # yellow
    "Hard": PatternFill("solid", fgColor="FECACA"),  # red
    "unknown": PatternFill("solid", fgColor="E5E7EB"),  # grey
}
STRONG = {  # darker shade for the KD / priority cells
    "big": PatternFill("solid", fgColor="7C3AED"),
    "Easy": PatternFill("solid", fgColor="16A34A"),
    "Medium": PatternFill("solid", fgColor="EAB308"),
    "Hard": PatternFill("solid", fgColor="DC2626"),
    "unknown": PatternFill("solid", fgColor="9CA3AF"),
}
HEADER_FILL = PatternFill("solid", fgColor="0F172A")
HEADER_FONT = Font(bold=True, color="FFFFFF")
THIN = Border(bottom=Side(style="thin", color="D1D5DB"))

# Ahrefs shows ranges; map them to a sortable number (lower bound of the range).
TIER = {"<100": 0, ">100": 100, ">1000": 1_000, ">10,000": 10_000, ">100K": 100_000, ">1M": 1_000_000}
KD_RANK = {"Easy": 0, "Medium": 1, "Hard": 2}
PRIORITY_LABEL = {
    "big": "★ Big & immediate",
    "Easy": "Easy",
    "Medium": "Medium",
    "Hard": "Hard",
    "unknown": "KD unknown",
}


def volume_of(row):
    v = row["Volume"]
    if isinstance(v, (int, float)):
        return int(v)
    return TIER.get(str(row["Volume (as shown)"] or "").strip(), 0)


def kd_of(row):
    k = str(row["KD (as shown)"] or "").strip()
    return k if k in KD_RANK else "unknown"


def priority_of(kd, volume):
    if kd == "Easy" and volume >= BIG_MIN_VOLUME:
        return "big"
    return kd


def header(ws, names, widths):
    ws.append(names)
    for cell in ws[ws.max_row]:
        cell.fill, cell.font = HEADER_FILL, HEADER_FONT
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = ws.cell(row=ws.max_row + 1, column=2)


def paint(ws, row_idx, prio, kd_col, prio_col):
    for cell in ws[row_idx]:
        cell.fill = FILL[prio]
        cell.border = THIN
    for col in (kd_col, prio_col):
        c = ws.cell(row=row_idx, column=col)
        c.fill = STRONG[prio if col == prio_col else (prio if prio != "big" else "Easy")]
        c.font = Font(bold=True, color="FFFFFF")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_name(src.stem + "_FORMATTED.xlsx")

    wb_in = openpyxl.load_workbook(src, read_only=True)
    rows = list(wb_in["All Keywords Detail"].iter_rows(values_only=True))
    head = rows[0]
    records = [dict(zip(head, r)) for r in rows[1:] if r and r[0]]

    # Merge duplicates (same keyword + country), keeping the best-known data and every tool/list.
    merged = {}
    for r in records:
        key = (str(r["Keyword"]).strip().lower(), r["Country"])
        vol, kd = volume_of(r), kd_of(r)
        m = merged.get(key)
        if not m:
            merged[key] = {
                "keyword": str(r["Keyword"]).strip(),
                "country": r["Country"],
                "volume": vol,
                "shown": r["Volume (as shown)"] or "",
                "kd": kd,
                "tools": [r["Tool"]],
                "group": r["Group"],
                "batch": r["Batch"],
                "lists": {r["List"]},
                "seed": r["Seed"],
            }
            continue
        if vol > m["volume"]:
            m["volume"], m["shown"] = vol, r["Volume (as shown)"] or m["shown"]
        if m["kd"] == "unknown" and kd != "unknown":
            m["kd"] = kd
        if r["Tool"] not in m["tools"]:
            m["tools"].append(r["Tool"])
        m["lists"].add(r["List"])

    items = list(merged.values())
    for it in items:
        it["priority"] = priority_of(it["kd"], it["volume"])

    wb = openpyxl.Workbook()

    # ---- Sheet 1: Big & immediate opportunities ----
    ws = wb.active
    ws.title = "★ Opportunities"
    cols = ["Keyword", "Country", "Volume", "Volume (Ahrefs)", "KD", "Priority", "Tool", "Group", "Batch", "List"]
    header(ws, cols, [44, 9, 11, 14, 10, 18, 40, 30, 8, 22])
    big = sorted((i for i in items if i["priority"] == "big"), key=lambda i: (-i["volume"], i["country"], i["keyword"]))
    for it in big:
        ws.append([it["keyword"], it["country"], it["volume"], it["shown"], it["kd"], PRIORITY_LABEL["big"],
                   " / ".join(it["tools"]), it["group"], it["batch"], ", ".join(sorted(it["lists"]))])
        paint(ws, ws.max_row, "big", 5, 6)
        ws.cell(row=ws.max_row, column=3).number_format = "#,##0"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{ws.max_row}"

    # ---- Sheet 2: All keywords, colour-coded ----
    ws = wb.create_sheet("All keywords")
    header(ws, cols, [44, 9, 11, 14, 10, 18, 40, 30, 8, 22])
    order = {"big": 0, "Easy": 1, "Medium": 2, "Hard": 3, "unknown": 4}
    for it in sorted(items, key=lambda i: (order[i["priority"]], -i["volume"], i["keyword"])):
        ws.append([it["keyword"], it["country"], it["volume"], it["shown"],
                   it["kd"] if it["kd"] != "unknown" else "–", PRIORITY_LABEL[it["priority"]],
                   " / ".join(it["tools"]), it["group"], it["batch"], ", ".join(sorted(it["lists"]))])
        paint(ws, ws.max_row, it["priority"], 5, 6)
        ws.cell(row=ws.max_row, column=3).number_format = "#,##0"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{ws.max_row}"

    # ---- Sheet 3: Per-tool summary ----
    ws = wb.create_sheet("Tool summary")
    scols = ["Tool", "Group", "Batch", "Keywords", "★ Big & immediate", "Easy", "Medium", "Hard", "KD unknown",
             "Easy volume (sum)", "Best easy keyword", "Biggest keyword (any KD)"]
    header(ws, scols, [44, 30, 8, 10, 16, 8, 9, 8, 11, 16, 50, 50])
    by_tool = collections.defaultdict(list)
    for it in items:
        by_tool[it["tools"][0]].append(it)
    summary = []
    for tool, its in by_tool.items():
        c = collections.Counter(i["priority"] for i in its)
        easy = [i for i in its if i["kd"] == "Easy"]
        best_easy = max(easy, key=lambda i: i["volume"], default=None)
        biggest = max(its, key=lambda i: i["volume"])
        fmt = lambda i: f'{i["keyword"]} ({i["country"]}, {i["shown"]}, {i["kd"] if i["kd"] != "unknown" else "KD ?"})' if i else ""
        summary.append([tool, its[0]["group"], its[0]["batch"], len(its), c["big"], c["Easy"] + c["big"], c["Medium"],
                        c["Hard"], c["unknown"], sum(i["volume"] for i in easy), fmt(best_easy), fmt(biggest)])
    summary.sort(key=lambda s: (-s[4], -s[9]))
    for s in summary:
        ws.append(s)
        r = ws.max_row
        for col, key in ((5, "big"), (6, "Easy"), (7, "Medium"), (8, "Hard"), (9, "unknown")):
            cell = ws.cell(row=r, column=col)
            if cell.value:
                cell.fill = FILL[key]
        ws.cell(row=r, column=10).number_format = "#,##0"
        if s[4]:
            ws.cell(row=r, column=1).fill = FILL["big"]
            ws.cell(row=r, column=1).font = Font(bold=True)
    ws.auto_filter.ref = f"A1:{get_column_letter(len(scols))}{ws.max_row}"

    # ---- Sheet 4: Volume matrix (heat map) ----
    src_vm = wb_in["Volume Matrix"]
    ws = wb.create_sheet("Volume matrix")
    vm_rows = list(src_vm.iter_rows(values_only=True))
    header(ws, list(vm_rows[0]), [44, 30, 8] + [10] * (len(vm_rows[0]) - 4) + [14])
    for r in vm_rows[1:]:
        ws.append(list(r))
        for cell in ws[ws.max_row][3:]:
            cell.number_format = "#,##0"
    last = get_column_letter(len(vm_rows[0]))
    ws.conditional_formatting.add(
        f"D2:{last}{ws.max_row}",
        ColorScaleRule(start_type="min", start_color="FFFFFF", mid_type="percentile", mid_value=70,
                       mid_color="FEF08A", end_type="max", end_color="16A34A"),
    )

    # ---- Sheet 5: Legend ----
    ws = wb.create_sheet("Legend")
    ws.column_dimensions["A"].width = 22
    ws.column_dimensions["B"].width = 90
    ws.append(["Colour", "Meaning"])
    for cell in ws[1]:
        cell.fill, cell.font = HEADER_FILL, HEADER_FONT
    legend = [
        ("big", f"★ Big & immediate: Easy KD and at least {BIG_MIN_VOLUME:,} searches/month. Build these first."),
        ("Easy", "Easy KD (Ahrefs). Can rank with a solid page and a few links."),
        ("Medium", "Medium KD. Needs a strong page plus backlinks."),
        ("Hard", "Hard KD. Dominated by big sites; target later or via long-tail variants."),
        ("unknown", "Ahrefs didn't return KD (N/A / sign-up wall). Check before deciding."),
    ]
    for key, text in legend:
        ws.append([PRIORITY_LABEL[key], text])
        ws.cell(row=ws.max_row, column=1).fill = STRONG[key]
        ws.cell(row=ws.max_row, column=1).font = Font(bold=True, color="FFFFFF")
        ws.cell(row=ws.max_row, column=2).fill = FILL[key]
    ws.append([])
    ws.append(["Notes", "Volumes are Ahrefs ranges (<100, >100, >1000, >10,000, >100K, >1M); 'Volume' uses the lower bound so it sorts."])
    ws.append(["", f"Duplicates (same keyword + country from several seeds/lists) were merged: {len(records):,} rows → {len(items):,} keywords."])
    ws.append(["", "Review brand terms (e.g. 'nano banana', 'canva') before treating them as tool opportunities."])
    for r in ws.iter_rows(min_row=2):
        for c in r:
            c.alignment = Alignment(wrap_text=True, vertical="top")

    wb.save(out)
    c = collections.Counter(i["priority"] for i in items)
    print(f"wrote {out}")
    print(f"{len(records)} rows -> {len(items)} unique keyword+country")
    print({PRIORITY_LABEL[k]: c[k] for k in ("big", "Easy", "Medium", "Hard", "unknown")})


if __name__ == "__main__":
    main()
