import re
import sys
import os

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def count_words(content):
    b = re.sub(r'^---\s*\n.*?\n---', '', content, flags=re.DOTALL)
    b = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', b, flags=re.IGNORECASE)
    b = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', b, flags=re.IGNORECASE)
    b = re.sub(r'<svg\b[^<]*(?:(?!<\/svg>)<[^<]*)*<\/svg>', '', b, flags=re.IGNORECASE)
    return len(re.sub(r'<[^>]+>', ' ', b).split())

print("Testing count_words helper...")
