from generate_wordcloud import generate_wordcloud
from link_scraper import collect_links_for_section
from extract_article_details import extract_article_details
if __name__ == '__main__':
    sids = list(range(100, 106))
    all_links = {}

    use_keyword = input("Would you like to use a keyword for filtering? (yes/no): ").strip().lower()

    keyword = None
    if use_keyword == 'yes':
        keyword = input("Please enter the keyword you want to search for: ")

    for sid in sids:
        section_links = collect_links_for_section(sid, 10)
        all_links[sid] = section_links

    articles = []
    for section, links in all_links.items():
        for link in links:
            article_data = extract_article_details(link, keyword)
            if article_data:
                article_data["section"] = section
                article_data["url"] = link
                articles.append(article_data)
    print(articles)
    generate_wordcloud(articles)
