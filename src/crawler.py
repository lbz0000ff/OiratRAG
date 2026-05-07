"""Wiki 爬虫 - 爬取 EU4 Wiki 页面并保存为 Markdown"""

import os
import re
import time
import json
from pathlib import Path
from urllib.parse import urljoin

import cloudscraper
from bs4 import BeautifulSoup


BASE_URL = "https://eu4.paradoxwikis.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
RAW_DIR = Path(__file__).parent.parent / "data" / "raw"
CHUNKS_DIR = Path(__file__).parent.parent / "data" / "chunks"

# 全局会话（复用连接 + 绕过 Cloudflare）
_scraper = None
def get_scraper():
    global _scraper
    if _scraper is None:
        _scraper = cloudscraper.create_scraper()
    return _scraper


def fetch_page(url: str) -> str:
    """获取页面 HTML（使用 cloudscraper 绕过 Cloudflare）"""
    scraper = get_scraper()
    resp = scraper.get(url, headers=HEADERS, timeout=20)
    resp.raise_for_status()
    # 检查是否被 Cloudflare 拦截
    if "Please enable JavaScript" in resp.text[:500]:
        raise RuntimeError(f"Cloudflare 拦截: {url}")
    return resp.text


def html_to_text(html: str, page_url: str = "") -> str:
    """将 wiki 页面 HTML 转为纯文本 Markdown"""
    soup = BeautifulSoup(html, "html.parser")

    # 定位主内容区（只用 id，避免 class 重复匹配）
    content = soup.select_one("#mw-content-text")
    if content is None:
        content = soup.select_one("#bodyContent, main")
    if content is None:
        content = soup.body
    if content is None:
        return ""

    lines = []
    for el in content.find_all(["h2", "h3", "h4", "p", "li", "pre"]):
        tag = el.name
        text = el.get_text(strip=True)
        if not text:
            continue

        if tag.startswith("h"):
            level = int(tag[1]) + 1  # h2 -> ##, h3 -> ###
            lines.append(f"{'#' * level} {text}")
            lines.append("")
        elif tag == "p":
            lines.append(text)
            lines.append("")
        elif tag == "li":
            # 检测是否在有序/无序列表中
            parent = el.find_parent(["ol", "ul"])
            prefix = "1. " if parent and parent.name == "ol" else "- "
            lines.append(f"{prefix}{text}")
        elif tag == "pre":
            lines.append(f"```\n{text}\n```")
            lines.append("")

    return "\n".join(lines)


def extract_title(html: str) -> str:
    """提取页面标题"""
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.select_one("h1#firstHeading, .firstHeading h1")
    if h1:
        return h1.get_text(strip=True)
    return "untitled"


def get_subpage_links(html: str, base: str = BASE_URL) -> list[str]:
    """从页面中提取子页面链接（EU4 Wiki 的相对路径）"""
    soup = BeautifulSoup(html, "html.parser")
    links = set()
    for a in soup.select("#mw-content-text a[href]"):
        href = a["href"]
        # 只保留 Wiki 内容页面的链接，排除特殊页面
        if href.startswith("/") and ":" not in href and not href.startswith("//"):
            full = urljoin(base, href)
            # 去重、去锚点
            full = full.split("#")[0]
            if full.startswith(BASE_URL) and full != base:
                links.add(full)
    return list(links)


def save_page(url: str, text: str, title: str):
    """保存页面内容到 data/raw/"""
    safe_name = re.sub(r"[^\w\-]", "_", url.replace(BASE_URL, "").strip("/") or "index")
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = RAW_DIR / f"{safe_name}.md"
    path.write_text(text, encoding="utf-8")
    return path


def crawl(start_urls: list[str], max_pages: int = 50, delay: float = 1.0):
    """爬取 EU4 Wiki 页面，广度优先"""
    visited = set()
    queue = list(start_urls)
    count = 0

    while queue and count < max_pages:
        url = queue.pop(0)
        if url in visited:
            continue
        visited.add(url)

        print(f"[{count + 1}/{max_pages}] 爬取: {url}")
        try:
            html = fetch_page(url)
            title = extract_title(html)
            text = html_to_text(html, url)
            page_path = save_page(url, text, title)
            print(f"  ✅ 已保存: {page_path.name} (标题: {title})")

            # 提取更多链接
            sub_links = get_subpage_links(html)
            for link in sub_links:
                if link not in visited:
                    queue.append(link)

            count += 1
            time.sleep(delay)
        except Exception as e:
            print(f"  ❌ 失败: {e}")

    print(f"\n完成！共爬取 {count} 个页面，保存在 {RAW_DIR}/")
    return count


if __name__ == "__main__":
    # 从 EU4 Wiki 的几个核心板块开始
    start_pages = [
        # f"{BASE_URL}/Europa_Universalis_4",
        # f"{BASE_URL}/Countries",
        # f"{BASE_URL}/Government",
        # f"{BASE_URL}/Technology",
        # f"{BASE_URL}/Ideas",
        # f"{BASE_URL}/Trade",
        # f"{BASE_URL}/Warfare",
        # f"{BASE_URL}/Missions",
        # f"{BASE_URL}/Events",
        # f"{BASE_URL}/Decisions",
        # f"{BASE_URL}/Institutions",
        # f"{BASE_URL}/Holy_Roman_Empire",
        # f"{BASE_URL}/Religions",
        # f"{BASE_URL}/Ages",
        f"{BASE_URL}/Diplomacy",
    ]
    crawl(start_pages, max_pages=30)
