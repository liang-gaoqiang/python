# *-- coding = utf-8 --*
"""
    @project: Day02
    @file：  亚马逊商品页面爬取.py
    @date： 2023/8/30
    @software: PyCharm
    __author__: 'Gaoqiang Liang @ Jiangxi Science and Technology Normal University' 
    ---------  热爱生活！ ---------
"""
import requests


def getHTMLText(url, headers):
    try:
        res = requests.get(url=url, headers=headers)
        res.encoding = res.apparent_encoding
        res.raise_for_status()

        return res.text
    except:
        print("爬取失败！")


url = 'https://www.amazon.cn/dp/B01MF959DX?ref_=Oct_DLandingS_D_33411f4a_1&th=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

html = getHTMLText(url, headers)
print(html[:1000])


