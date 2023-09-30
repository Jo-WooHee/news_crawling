import requests
from bs4 import BeautifulSoup

def extract_article_details(url, keyword=None):
    selectors = {
        "title": "#title_area > span",
        "date": "#ct > div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_datestamp > div:nth-child(1) > span",
        "main": "#dic_area"
    }

    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    })
    soup = BeautifulSoup(response.text, "lxml")

    article_data = {}
    for key, selector in selectors.items():
        elements = soup.select(selector)
        article_data[key] = " ".join([element.text for element in elements])

    if keyword and (keyword not in article_data["title"] and keyword not in article_data["main"]):
        return None
    else:
        return article_data
