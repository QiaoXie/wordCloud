# _*_ coding:utf-8 _*_
import codecs
import os
import jieba
from collections import Counter
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator

"""
python3.6
分词并生成词云

data/news文件夹下是待分词的新闻txt
data/stopWords.txt是停用词
生成的词云图片保存在img文件夹下 wordCloud_jieba.png
作者：谢宗乔 xiezongqiao@foxmail.com
时间：2018.3.13
"""
# 获取当前文件路径
p = path.dirname(__file__)

news_path = path.join(p, 'data/news') # 待分词的新闻路径
stop_path = path.join(p, 'data/stopWords.txt') # 停用词路径
back_coloring_path = "img/timg.jpg"  # 设置背景图片路径
font_path = 'data/MFQingShu_Noncommercial-Regular.otf'  # 为matplotlib设置中文字体路径
imgname = "img/wordCloud_jieba.png"  # 保存的图片名字
back_coloring = imread(path.join(p, back_coloring_path))  # 设置背景图片

# 设置词云属性
wc = WordCloud( font_path = font_path,  # 设置字体
               background_color = "white",  # 背景颜色
               max_words = 2000,  # 词云显示的最大词数
               mask = back_coloring,  # 设置背景图片
               max_font_size = 100,  # 字体最大值
               random_state = 42,
               width = 1000,
               height = 860,
               margin = 2,
               # 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
               )


def each_file(file_path):
    # 遍历指定目录，显示目录下的所有文件名
    pathDir = os.listdir(file_path)
    child = []
    for allDir in pathDir:
        child.append(os.path.join('%s/%s' %(file_path,allDir)))
    return child


def read_txt(file_path):
    # 读取txt文件
    data = []
    with codecs.open(file_path, mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            data.append(line.strip())
    f.close()
    return data


def rm_stopwords(data):
    # 去除停用词
    with codecs.open(stop_path, mode='r', encoding='utf-8') as f:
         stop_list = {}.fromkeys([line.strip() for line in f])
    result = [word for word in list(data) if word not in stop_list]
    for i in result:
        if i == '\u3000':
            result.remove(i)
    return result


def cut_word(txtList):
    # 结巴分词
    word = []
    for txt in txtList:
        wordList = list(jieba.cut(txt))
        word.extend(rm_stopwords(wordList))
    return word


# 读取txt并分词
data_pathList = each_file(news_path)
resultWord = []
for dir in data_pathList:
    resultWord.extend(cut_word(read_txt(dir)))

# 计算词频
cnt = Counter()
for word in resultWord:
     cnt[word] += 1

# list 转 dict
s = []
cnt_list = cnt.most_common()
for x in cnt_list:
    s.append(list(x))
result = dict(s)

print('生成词云中...')

# 该参数为dict类型
wc.generate_from_frequencies(result)

print('绘制中...')

# 保存图片
wc.to_file(path.join(p, imgname))

# 从背景图片生成颜色值
image_colors = ImageColorGenerator(back_coloring)
plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.show()


