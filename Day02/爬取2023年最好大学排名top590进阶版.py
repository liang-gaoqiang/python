# *-- coding = utf-8 --*
"""
    @project: Day02
    @file：  爬取2023年最好大学排名top590进阶版.py
    @date： 2023/8/31
    @software: PyCharm
    __author__: 'Gaoqiang Liang @ Jiangxi Science and Technology Normal University' 
    ---------  热爱生活！ ---------
"""
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


def getFirstText(lst):
    try:
        return lst[0].strip()
    except:
        return ""


def getData(browser, data):
    try:
        for i in range(1, 31):
            """ 排名、学校名称（中文）、学校名称(英文)、双一流/985/211、省市、类型、总分、办学层次"""
            tr = browser.find_element(By.XPATH, '//*[@id="content-box"]/div[2]/table/tbody/tr[' + i.__str__() + ']')
            # tr = browser.find_element(By.XPATH, '//*[@id="content-box"]/div[2]/table/tbody/tr[' + str(i) + ']')
            # randks = tr.find_element(By.XPATH, './td[1]/div/text()')
            # schoolNameInChinese = tr.find_element(By.XPATH, './td[2]/div/div[2]/div[1]/div/div/a/text()')[0].strip().split('/n')[0]
            # schoolNameInEnglish = tr.find_element(By.XPATH, './td[2]/div/div[2]/div[2]/div/div/a/text()')[0].strip()
            # shuangyiliu = tr.find_element(By.XPATH,'./td[2]/div/div[2]/p/text()')
            #
            # if len(shuangyiliu) == 0:
            #     shuangyiliu = None
            # else:
            #     shuangyiliu = shuangyiliu[0]
            #
            # provinces = tr.find_element(By.XPATH,'./td[3]/text()')[0].strip()
            # school_type = tr.find_element(By.XPATH,'./td[4]/text()')[0].strip()
            # scores = tr.find_element(By.XPATH,'./td[5]/text()')[0].strip()
            # banxuecengci = tr.find_element(By.XPATH,'./td[6]/text()')[0].strip()
            # data.append(
            #     [randks, schoolNameInChinese, schoolNameInEnglish, shuangyiliu, provinces, school_type, scores,
            #
            #      banxuecengci]
            # )
            id = tr.find_element(By.XPATH, './td[1]/div').text
            name = tr.find_element(By.XPATH, './td[2]/div/div[2]/div[1]/div/div/a').text
            province = tr.find_element(By.XPATH, './td[3]').text
            type = tr.find_element(By.XPATH, './td[4]').text
            score = tr.find_element(By.XPATH, './td[5]').text
            data.append([id, name, province, type, score])
    except:

        print("不够30条了！")
    return data


def savaToExcel(data):
    with open('爬取2023年最好大学排名top590.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['排名', '学校名称（中文）', '学校名称(英文)', '双一流/985/211', '省市', '类型', '总分', '办学层次'])
        writer.writerows(data)
    print('文件写入成功！')


def main():
    url = 'https://www.shanghairanking.cn/rankings/bcur/202311'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    # 定义chrome驱动地址
    path = (r"D:\tool\driver\chromedriver.exe")
    dataList = []

    # 创建浏览器操作对象
    browser = webdriver.Chrome(executable_path=path)
    browser.get(url=url)
    for i in range(1, 21):
        # time.sleep(3)

        getData(browser, dataList)
        if i in [1, 2, 3, 18, 19, 20]:
            alink = browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div/ul/li[9]/a')

        elif i in [4, 17]:
            alink = browser.find_element(By.XPATH,
                                         '/html/body/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div/ul/li[10]/a')
        else:
            alink = browser.find_element(By.XPATH,
                                         '/html/body/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div/ul/li[11]/a')
        alink.click()
        print("第", i, '页已经读取完成')

    savaToExcel(dataList)


if __name__ == '__main__':
    main()
