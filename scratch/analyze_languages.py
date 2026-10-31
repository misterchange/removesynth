import openpyxl, sys

sys.stdout.reconfigure(encoding='utf-8')
wb = openpyxl.load_workbook(r'D:\Nitin\keyword_researcher\proxy-keywords\output\removesynth_seeds_keywords_2026-10-16T15-39-20_FORMATTED.xlsx')

print('--- VOLUME MATRIX SHEET ---')
ws_vol = wb['Volume matrix']
for r in list(ws_vol.iter_rows(values_only=True))[:15]:
    print(r)

ws_kw = wb['All keywords']
country_stats = {}
for r in list(ws_kw.iter_rows(values_only=True))[1:]:
    kw = r[0]
    country = r[1]
    vol = r[2] if isinstance(r[2], (int, float)) else 0
    kd = str(r[4])
    if not country: continue
    if country not in country_stats:
        country_stats[country] = {'total_vol': 0, 'easy_vol': 0, 'kws': 0, 'easy_kws': 0, 'top_easy_kws': []}
    country_stats[country]['total_vol'] += vol
    country_stats[country]['kws'] += 1
    if 'Easy' in kd:
        country_stats[country]['easy_vol'] += vol
        country_stats[country]['easy_kws'] += 1
        if vol >= 1000:
            country_stats[country]['top_easy_kws'].append((kw, vol))

print('\n--- COUNTRY BREAKDOWN & EASY OPPORTUNITY ---')
for c, d in sorted(country_stats.items(), key=lambda x: x[1]['total_vol'], reverse=True):
    top_samples = sorted(d['top_easy_kws'], key=lambda x: x[1], reverse=True)[:5]
    print(f"\nCountry: {c}")
    print(f"  Total Search Volume: {d['total_vol']:,}")
    print(f"  Easy Volume (KD <= 10): {d['easy_vol']:,}")
    print(f"  Total Keywords: {d['kws']} (Easy Keywords: {d['easy_kws']})")
    print(f"  Top Easy Keywords: {top_samples}")
