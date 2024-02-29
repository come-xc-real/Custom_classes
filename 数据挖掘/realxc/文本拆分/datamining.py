import jieba
from draw import Histogram
import matplotlib
matplotlib.rc("font",family='YouYuan')

with open('test (2).txt', 'r', encoding='utf-8') as file:
    content = file.read()
sentences = content.split('。')  # 根据句号将文本分割成句子

all_result = {}
for sentence in sentences:

    if sentence:
        seg_list = jieba.cut(sentence)
        seg_list = [word for word in seg_list if word]
        for seg in seg_list:
            if seg in all_result.keys():
                all_result[seg] += 1
            else:
                all_result.update({seg: 1})

with open('output.txt', 'w', encoding='utf-8') as output_file:
    for segment, counts in all_result.items():
        output_file.write(segment + '------' + str(counts) + "\n")


top_20 = {key: value for key, value in sorted(all_result.items(), key=lambda item: item[1], reverse=True)[:20]}


histogram = Histogram(top_20)
histogram.draw()
