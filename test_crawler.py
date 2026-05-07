"""测试爬虫: 一个内容丰富的页面"""
import sys
sys.path.insert(0, "src")
from crawler import fetch_page, html_to_text, extract_title

url = "https://eu4.paradoxwikis.com/Technology"
print(f"测试: {url}")
html = fetch_page(url)
title = extract_title(html)
print(f"标题: {title}")
text = html_to_text(html)
print(f"内容长度: {len(text)} 字符")
print("预览:")
print(text[:800])
