# *-- coding = utf-8 --*
"""
    @project: Day02
    @file：  打开翻页使用selenium.py
    @date： 2023/8/31
    @software: PyCharm
    __author__: 'Gaoqiang Liang @ Jiangxi Science and Technology Normal University' 
    ---------  热爱生活！ ---------
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

path = r'D:\tool\driver\chromedriver.exe'

browser = webdriver.Chrome(path)

url = 'http://www.shanghairanking.cn/rankings/bcur/202311'

browser.get(url=url)
browser.maximize_window()
for i in range(1, 21):
    time.sleep(1)
    if i in [1, 2, 3, 18, 19, 20]:
        alink = browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div/ul/li[9]/a')

    elif i in [4, 17]:
        alink = browser.find_element(By.XPATH,
                                     '/html/body/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div/ul/li[10]/a')
    else:
        alink = browser.find_element(By.XPATH,
                                     '/html/body/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div/ul/li[11]/a')
    alink.click()