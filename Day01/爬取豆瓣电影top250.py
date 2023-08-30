# *-- coding = utf-8 --*
"""
    @project: Day01
    @file：  爬取豆瓣电影top250.py
    @date： 2023/8/30
    @software: PyCharm
    __author__: 'Gaoqiang Liang @ Jiangxi Science and Technology Normal University' 
    ---------  热爱生活！ ---------
"""
import pandas as pd
import requests
from lxml import etree

df = []


def get_data(html, columns):
    xp = etree.HTML(html)
    lis = xp.xpath('//*[@id="content"]/div/div[1]/ol/li')

    for li in lis:
        """ 排名、电影名称、导演、上映年份、制作国家、类型、评分、评价人数、短评、电影链接 """
        randks = li.xpath('./div/div[1]/em/text()')[0]
        filmname = li.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
        directors = li.xpath('div/div[2]/div[2]/p[1]/text()')[0].strip().replace("\xa0\xa0\xa0", "\t").split("\t")[0]
        infor = li.xpath('div/div[2]/div[2]/p[1]/text()')[1].strip().replace('\xa0', '').split('/')
        years, makingCountry, filmtype = infor[0], infor[1], infor[2]
        scores = li.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
        commentnumbers = li.xpath('./div/div[2]/div[2]/div/span[4]/text()')[0][:-3]  # 去掉"人评价"这三个字
        comments = li.xpath('.//p[@class="quote"]/span/text()')
        filmhref = li.xpath('./div/div[2]/div[1]/a/@href')[0]
        # 如果电影没有评论，则comment为None
        if len(comments) == 0:
            comments = None
        else:
            comments = comments[0]

        print(randks, filmname, directors, years, makingCountry, filmtype, scores, commentnumbers, comments, filmhref)

        df.append(
            [randks, filmname, directors, years, makingCountry, filmtype, scores, commentnumbers, comments, filmhref])
        d = pd.DataFrame(df, columns=columns)
        d.to_excel('Python爬取豆瓣电影Top250.xlsx', index=False)


def main():
    columns = ['排名', '电影名称', '导演', '上映年份', '制作国家', '类型', '评分', '评价人数', '短评', '电影链接']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36',
        'Referer': 'https://movie.douban.com/top250'}

    for i in range(0, 251, 25):
        url = "https://movie.douban.com/top250?start={}&filter=".format(str(i))
        res = requests.get(url=url, headers=headers)
        html = res.text
        get_data(html, columns)


main()
