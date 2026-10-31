import openpyxl
import json

wb = openpyxl.load_workbook('research/seed-keywords-v2.xlsx', data_only=True)
ws = wb['Seed keywords']

tools_data = []

headers = [cell.value for cell in ws[1]]
print("Headers:", headers)

for row in ws.iter_rows(min_row=2, values_only=True):
    if not row[1]:
        continue
    tool_name = str(row[1]).strip()
    group = str(row[2]).strip() if len(row) > 2 and row[2] else ''
    batch = str(row[3]).strip() if len(row) > 3 and row[3] else ''
    us_keywords = str(row[4]).strip() if len(row) > 4 and row[4] else ''
    in_keywords = str(row[5]).strip() if len(row) > 5 and row[5] else ''
    extra = str(row[-1]).strip() if row[-1] else ''
    
    tools_data.append({
        'tool': tool_name,
        'group': group,
        'batch': batch,
        'us_keywords': us_keywords,
        'in_keywords': in_keywords,
        'extra': extra
    })

print(f"Total tools in Seed keywords: {len(tools_data)}")
for t in tools_data[:15]:
    print(f"- {t['tool']} ({t['group']}): {t['us_keywords']}")

with open('scratch/excel_keywords_summary.json', 'w', encoding='utf-8') as f:
    json.dump(tools_data, f, indent=2, ensure_ascii=False)
