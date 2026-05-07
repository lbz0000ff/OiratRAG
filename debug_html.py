"""调试: html_to_text 到底找到了什么"""
import sys
sys.path.insert(0, "src")
from crawler import fetch_page, html_to_text
from bs4 import BeautifulSoup

url = "https://eu4.paradoxwikis.com/Technology"
html = fetch_page(url)
soup = BeautifulSoup(html, "html.parser")

# 直接测试 find_all
content = soup.select_one("#mw-content-text, .mw-parser-output")
if content:
    found = content.find_all(["h2", "h3", "h4", "p", "li", "pre"])
    print(f"find_all 找到 {len(found)} 个目标元素")
    if found:
        for el in found[:5]:
            print(f"  <{el.name}>: {el.get_text(strip=True)[:80]}")
    else:
        # 递归测试
        print(f"递归 find_all 所有标签类型: {set(el.name for el in content.find_all())}")
else:
    print("content 不存在!")
