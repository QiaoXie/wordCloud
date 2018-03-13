import codecs
from collections import Counter
def readLines(filename):
    data = []
    word = ''
    with codecs.open(filename, 'r', encoding = 'utf-8') as f:
        txt =  f.read()
        for line in txt:
            word = word + line
            if line == ' ':
                data.append(word)
                word = ''
    return data
cnt = Counter()
data_list = readLines('data/lastRead.txt')
for word in data_list[1:10000]:
     cnt[word] += 1

# wc.generate_from_frequencies(cnt.most_common(1000))
# wc.generate_from_frequencies(txt_freq)
# txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
# (wordcloud对中文分词支持不好,建议启用中文分词),也可以我们计算好词频后使用generate_from_frequencies函数