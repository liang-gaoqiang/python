# *-- coding = utf-8 --*
"""
    @project: Day02
    @file：  爬取2023年最好大学排名top30.py
    @date： 2023/8/30
    @software: PyCharm
    __author__: 'Gaoqiang Liang @ Jiangxi Science and Technology Normal University' 
    ---------  热爱生活！ ---------
"""
import requests
from lxml import etree
import pandas as pd

# 网页改版，导致无法爬取整个数据--只能定向爬取，也即是无法通过简单的改变url地址来获取翻页后的数据了。
df = []
columns = ['排名', '学校名称（中文）', '学校名称(英文)', '双一流/985/211', '省市', '类型', '总分', '办学层次']


def getHTMLText(url, headers):
    try:
        r = requests.get(url=url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败!")


def parasPage(html):
    xp = etree.HTML(html)
    trs = xp.xpath('//*[@id="content-box"]/div[2]/table/tbody/tr')
    lis = xp.xpath('// *[ @ id = "content-box"] / ul / li')
    print(len(lis))
    for tr in trs:
        """ 排名、学校名称（中文）、学校名称(英文)、双一流/985/211、省市、类型、总分、办学层次"""
        randks = tr.xpath('./td[1]/div/text()')[0].strip()
        schoolNameInChinese = tr.xpath('./td[2]/div/div[2]/div[1]/div/div/a/text()')[0].strip().split('/n')[0]
        schoolNameInEnglish = tr.xpath('./td[2]/div/div[2]/div[2]/div/div/a/text()')[0].strip()
        shuangyiliu = tr.xpath('./td[2]/div/div[2]/p/text()')

        if len(shuangyiliu) == 0:
            shuangyiliu = None
        else:
            shuangyiliu = shuangyiliu[0]

        provinces = tr.xpath('./td[3]/text()')[0].strip()
        school_type = tr.xpath('./td[4]/text()')[0].strip()
        scores = tr.xpath('./td[5]/text()')[0].strip()
        banxuecengci = tr.xpath('./td[6]/text()')[0].strip()

        print(randks, schoolNameInChinese, schoolNameInEnglish, shuangyiliu, provinces, school_type, scores, banxuecengci)

        df.append(
            [randks,  schoolNameInChinese, schoolNameInEnglish, shuangyiliu, provinces, school_type, scores, banxuecengci]
        )
        d = pd.DataFrame(df, columns=columns)
        d.to_excel('爬取2023年最好大学排名top30.xlsx', index=False)


def main():
    url = 'http://www.shanghairanking.cn/rankings/bcur/202311'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

    html = getHTMLText(url=url, headers=headers)
    parasPage(html)


main()