# *-- coding = utf-8 --*
"""
    @project: Day01
    @file：  豆瓣电影top250数据分析.py
    @date： 2023/8/30
    @software: PyCharm
    __author__: 'Gaoqiang Liang @ Jiangxi Science and Technology Normal University' 
    ---------  热爱生活！ ---------
"""
import matplotlib.pyplot as plt
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, WordCloud
from collections import Counter


data = pd.read_excel('Python爬取豆瓣电影Top250.xlsx')
print(data.columns)


# 下面进行第一个数据分析：绘制不同年份的电影上映次数
years = data['上映年份'].isnull().sum()
print(years)
# 处理上映年份格式不正确的行
year = []
for i in data['上映年份']:
    i = i[:4]
    year.append(i)

data['上映年份'] = year
# 去除掉重复的年份并按照从小到大的顺序排序
x1 = list(data['上映年份'].value_counts().sort_index().index)
print(x1)
# 计算出不同年份出现的次数也即是不同年份下电影上映的次数
y1 = list(data['上映年份'].value_counts().sort_index().values)
print(y1)


def getzoombar(data):
    year_counts = data['上映年份'].value_counts()
    year_counts.columns = ['上映年份', '数量']
    year_counts = year_counts.sort_index()
    c = (
        Bar()
        .add_xaxis(list(year_counts.index))
        .add_yaxis('上映数量', year_counts.values.tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title='各年份上映电影数量'),
            yaxis_opts=opts.AxisOpts(name='上映数量'),
            xaxis_opts=opts.AxisOpts(name='上映年份'),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_='inside')],)
        ).render('上映年份.html')


getzoombar(data)

# 各地区上映电影数量前十柱状图


def getcountrybar(data):
    country_counts = data['制作国家'].value_counts()
    country_counts.columns = ['制作国家', '数量']
    country_counts = country_counts.sort_values(ascending=True)
    c = (
        Bar()
        .add_xaxis(list(country_counts.index)[-10:])
        .add_yaxis('地区上映数量', country_counts.values.tolist()[-10:])
        .reversal_axis()
        .set_global_opts(
        title_opts=opts.TitleOpts(title='地区上映电影数量'),
        yaxis_opts=opts.AxisOpts(name='制作国家'),
        xaxis_opts=opts.AxisOpts(name='上映数量'),
        )
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        ).render('各地区上映电影数量前十柱状图.html')


getcountrybar(data)


# 评价电影人数最高的前20个


def getscorebar(data):
    df = data.sort_values(by='评价人数', ascending=True)
    c = (
        Bar()
        .add_xaxis(df['电影名称'].values.tolist()[-20:])
        .add_yaxis('评价人数', df['评价人数'].values.tolist()[-20:])
        .reversal_axis()
        .set_global_opts(
            title_opts=opts.TitleOpts(title='电影评价人数'),
            yaxis_opts=opts.AxisOpts(name='电影名称'),
            xaxis_opts=opts.AxisOpts(name='人数'),
            datazoom_opts=opts.DataZoomOpts(type_='inside'),
            )
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        ).render('评价电影人数最高的前20个.html')

getscorebar(data)


# 绘制评分直方图
plt.figure(figsize=(10, 6))
plt.title("评分直方图")
plt.hist(list(data['评分']), bins=8, facecolor='blue', edgecolor='black', alpha=0.7)
plt.show()


# 排名与评分分布情况
plt.figure(figsize=(10, 5), dpi=100)
plt.xlabel("电影排名:1-250")
plt.ylabel('电影评分:5-10')
plt.scatter(data.index, data['评分'])
plt.show()


colors = ''.join([i for i in data['类型']]).strip().split()
c = dict(Counter(colors))
f = zip(c.keys(), c.values())
words = sorted(f)
print(c)


c3 = (
    WordCloud()
    .add(
        "",
        words,
        word_size_range=[20, 100],
        textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-自定义文字样式"))
    .render("电影类型词云图.html")
)

