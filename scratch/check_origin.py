import openpyxl, sys
sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.load_workbook(r'D:\Nitin\keyword_researcher\proxy-keywords\output\removesynth_seeds_keywords_2026-10-16T15-39-20_FORMATTED.xlsx', read_only=True)
ws = wb['Legend']
print('=== Legend in FORMATTED.xlsx ===')
for r in ws.iter_rows(values_only=True):
    print(r)

print('\n=== Check why removesynth_ACT_NOW_vidhaul.xlsx has vidhaul in name ===')
wb2 = openpyxl.load_workbook(r'D:\Nitin\keyword_researcher\proxy-keywords\output\removesynth_ACT_NOW_vidhaul.xlsx', read_only=True)
print('Sheets in removesynth_ACT_NOW_vidhaul.xlsx:', wb2.sheetnames)
ws2 = wb2['Build list']
for r in list(ws2.iter_rows(values_only=True))[:5]:
    print(r)
