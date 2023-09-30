from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(articles):
    # 모든 기사 제목을 합침
    titles = " ".join([article['title'] for article in articles])
    font_path = "./NotoSansKR-VariableFont_wght.ttf"

    # Word Cloud를 생성.
    wordcloud = WordCloud(width=800, height=400, background_color="white", font_path=font_path).generate(titles)

    # Word Cloud 이미지를 보여줌.
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
