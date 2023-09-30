import requests
from bs4 import BeautifulSoup

def fetch_links_from_page(sid, page):
    url_template = f"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1={sid}&date=%2000:00:00&page={page}"
    response = requests.get(url_template, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    })
    soup = BeautifulSoup(response.text, "lxml")
    links = [a["href"] for a in soup.find_all("a", href=True) if (f"sid={sid}" in a["href"]) and ("article" in a["href"])]
    return links

def collect_links_for_section(sid, pages):
    all_links = []
    for page_num in range(1, pages + 1):
        links = fetch_links_from_page(sid, page_num)
        all_links.extend(links)
    return list(set(all_links))


