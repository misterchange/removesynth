import sys
import pandas as pd

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

csv_path = r'D:\Nitin\keyword_researcher\proxy-keywords\output\removesynth_seeds_keywords_2026-10-16T15-39-20.csv'
df = pd.read_csv(csv_path)
print("Total keywords in database:", len(df))

df['kw_lower'] = df['keyword'].astype(str).str.lower()
df['volume'] = pd.to_numeric(df['volume'], errors='coerce').fillna(0)

topics = {
    'synthid': df[df['kw_lower'].str.contains('synthid|synth id', regex=True)],
    'ai_info_label': df[df['kw_lower'].str.contains('ai info|made with ai|ai label|rotulo de ia|ai-info', regex=True)],
    'exif_metadata': df[df['kw_lower'].str.contains('exif|metadata foto|photo metadata|remove metadata|remover metadados', regex=True)],
    'gemini_banana': df[df['kw_lower'].str.contains('nano banana|gemini watermark|banana ai', regex=True)],
    'video_watermark': df[df['kw_lower'].str.contains('watermark.*video|video.*watermark|watermark remover|remove watermark', regex=True)],
    'questions': df[df['kw_lower'].str.startswith(('how ', 'what ', 'can ', 'why ', 'does ', 'is ', 'como ', 'que '))]
}

for name, subset in topics.items():
    print(f"\n=== TOPIC: {name} (Total: {len(subset)}) ===")
    top = subset.sort_values(by='volume', ascending=False).head(15)
    for idx, r in top.iterrows():
        print(f"  {r['keyword']} | Vol: {int(r['volume'])} | KD: {r.get('difficulty', 'N/A')} | Country: {r.get('country', 'N/A')}")
