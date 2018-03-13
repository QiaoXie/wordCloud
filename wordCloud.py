# _*_ coding:utf-8 _*_
from collections import Counter
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator

"""
python3.6
对已分好的词txt生成词云

data文件夹存放词云的字体MFQingShu_Noncommercial-Regular.otf
    以及已经分词的wordcloud.txt
img文件夹存放词云背景图片
    以及生成的词云图
作者：谢宗乔 xiezongqiao@foxmail.com
时间：2018.3.13
"""

# 获取当前文件路径
d = path.dirname(__file__)

isCN = 1  # 默认启用中文分词
back_coloring_path = "img/timg.jpg" # 设置背景图片路径
text_path = 'data/wordcloud.txt' # 设置要分析的文本路径
font_path = 'data/MFQingShu_Noncommercial-Regular.otf'  # 为matplotlib设置中文字体路径没
imgname = "img/WordCloudDefautColors.png"  # 保存的图片名字1(只按照背景图片形状)
back_coloring = imread(path.join(d, back_coloring_path))  # 设置背景图片

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

text = open(text_path, mode='r',encoding='utf-8').read()

print('生成词云中...')

# 生成词云,输入已经分好词的文本
wc.generate(text)

print('绘制中...')
# 从背景图片生成颜色值
image_colors = ImageColorGenerator(back_coloring)
plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.show()

# 保存图片
wc.to_file(path.join(d, imgname))
