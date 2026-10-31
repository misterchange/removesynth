"""Turns seed-keywords.csv into a formatted seed-keywords.xlsx (frozen header, wrapped cells, group colours)."""
import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

HERE = Path(__file__).parent
GROUP_COLORS = {
    "A": "E0F2FE", "B": "E0E7FF", "C": "DCFCE7", "D": "FEF9C3",
    "E": "FFE4E6", "F": "F3E8FF", "G": "FFEDD5", "H": "ECFCCB",
}

rows = list(csv.reader((HERE / "seed-keywords.csv").open(encoding="utf-8-sig")))
header, body = rows[0], [r for r in rows[1:] if any(r)]

wb = Workbook()
ws = wb.active
ws.title = "Seed keywords"
ws.append(header)
for cell in ws[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="0F172A")
    cell.alignment = Alignment(wrap_text=True, vertical="center")

for r in body:
    ws.append(r)
    row = ws.max_row
    group = (r[2][:1] if len(r) > 2 else "")
    fill = GROUP_COLORS.get(group)
    for cell in ws[row]:
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        if fill:
            cell.fill = PatternFill("solid", fgColor=fill)
    if len(r) > 3 and r[3] == "1":
        ws.cell(row=row, column=2).font = Font(bold=True)

widths = [5, 34, 22, 10] + [38] * (len(header) - 5) + [44]
for i, w in enumerate(widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w
ws.freeze_panes = "E2"
ws.auto_filter.ref = f"A1:{get_column_letter(len(header))}{1 + len([r for r in body if len(r) > 3])}"

# A second sheet in "one keyword per row" format — easier to paste into Ahrefs/Semrush and to add volumes.
flat = wb.create_sheet("One per row (add volumes)")
flat.append(["Tool", "Group", "Batch", "Country", "Keyword", "Volume", "KD", "CPC", "SERP: tools or articles?"])
for cell in flat[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="0F172A")
for r in body:
    if len(r) < len(header):
        continue
    for ci in range(4, len(header) - 1):
        for kw in [k.strip() for k in r[ci].split("|") if k.strip()]:
            flat.append([r[1], r[2], r[3], header[ci], kw])
for i, w in enumerate([34, 22, 10, 20, 48, 10, 8, 8, 24], 1):
    flat.column_dimensions[get_column_letter(i)].width = w
flat.freeze_panes = "A2"
flat.auto_filter.ref = f"A1:I{flat.max_row}"

comp_csv = HERE / "competitors.csv"
if comp_csv.exists():
    cs = wb.create_sheet("Competitors")
    for i, r in enumerate(csv.reader(comp_csv.open(encoding="utf-8-sig"))):
        cs.append(r)
        for cell in cs[cs.max_row]:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            if i == 0:
                cell.font = Font(bold=True, color="FFFFFF")
                cell.fill = PatternFill("solid", fgColor="0F172A")
    for i, w in enumerate([30, 14, 34, 60, 60], 1):
        cs.column_dimensions[get_column_letter(i)].width = w
    cs.freeze_panes = "A2"

out = HERE / "seed-keywords-v2.xlsx"
wb.save(out)
print(f"wrote {out}: {len(body)} rows, {flat.max_row - 1} keywords in the one-per-row sheet")
