# *-- coding = utf-8 --*
"""
    @project: Day02
    @file：  京东商品页面爬取.py
    @date： 2023/8/30
    @software: PyCharm
    __author__: 'Gaoqiang Liang @ Jiangxi Science and Technology Normal University' 
    ---------  热爱生活！ ---------
"""
import requests


url = 'https://item.jd.com/100062873943.html?cu=true&utm_source=wk.idey.cn&utm_medium=tuiguang&utm_campaign=t_2024175271_&utm_term=905f1d06587b4341ba14a519e3e96a44#crumb-wrap'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

res = requests.get(url, headers)
# 调用该函数，如果返回200，则并不报错，否则就引发异常
res.raise_for_status()
# print(res.status_code)

# 打印出页面的编码信息
# print(res.encoding)
# 看一下返回的页面信息是否正确
# print(res.text[:1000])


def getHTMLText(url, headers):
    try:
        res = requests.get(url, headers)
        res.raise_for_status()
        print(res.text[:1000])
        return res.text
    except:
        print("爬取失败！")

# 测试函数
getHTMLText(url, headers)