import sys
import os
import pandas as pd

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

excel_path = r'D:\Nitin\keyword_researcher\proxy-keywords\output\removesynth_ACT_NOW_vidhaul.xlsx'
df = pd.read_excel(excel_path)
for idx, r in df.iterrows():
    tool = r.get('Tool')
    tool_type = r.get('Type')
    priority = r.get('Priority')
    total_vol = r.get('Total volume (our 7 countries)')
    us_vol = r.get('US')
    top_kws = r.get('Top easy keywords')
    print(f"[{priority}] {tool} ({tool_type}) -> Total: {total_vol} | US: {us_vol}")
    print(f"    Keywords: {str(top_kws)[:200]}")
