from wordcloud import WordCloud


with open('output.txt', 'r', encoding='utf-8') as file:
    content = file.read()

all_seg = content.split("\n")

text = ' '.join(all_seg)


wordcloud = WordCloud(font_path='SimHei.ttf', width=800, height=400, background_color='white', max_words=1000).generate(text)

wordcloud.to_file('wordcloud.png')