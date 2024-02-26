'''
读取https://www.11meigui.com/tools/currency网站表格中的1，2，5列，将其保存到一个csv文件中
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import pdb

# 创建一个空的DataFrame
df1 = pd.DataFrame(columns=['Nation', 'Currency_name', 'Currency_code'])

# 设置WebDriver的路径
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 打开网页
url = 'https://www.11meigui.com/tools/currency'
driver.get(url)

# 等待页面加载完成
driver.implicitly_wait(10)

# 定位到页面上所有的表格
for i in range(1, 6): # 一共有5个表格
    # 定位到当前表格
    currency_table_xpth = f'/html/body/main/div/table/tbody/tr[2]/td/table[{i}]'
    currency_table = driver.find_element(By.XPATH, currency_table_xpth)
    # 获取当前表格有多少行
    rows = currency_table.find_elements(By.CSS_SELECTOR, 'tr')
    len_row = len(rows)

    # 遍历表格的每一行, 并将货币代码和名称存储到字典中
    for j in range(3, len_row + 1):
        nation = currency_table.find_element(By.XPATH, f'/html/body/main/div/table/tbody/tr[2]/td/table[{i}]/tbody/tr[{j}]/td[1]').text
        currency_name = currency_table.find_element(By.XPATH, f'/html/body/main/div/table/tbody/tr[2]/td/table[{i}]/tbody/tr[{j}]/td[2]').text
        currency_code = currency_table.find_element(By.XPATH, f'/html/body/main/div/table/tbody/tr[2]/td/table[{i}]/tbody/tr[{j}]/td[5]').text
        df_tmp = pd.DataFrame([{'Nation': nation, 'Currency_name': currency_name,
                                'Currency_code':currency_code}])
        df1 = pd.concat([df_tmp,df1], ignore_index=True)

# 关闭浏览器
driver.quit()

# 将DataFrame保存到csv文件中
df1.to_csv('./面试准备/北京世游笔试/11meigui.csv', index=False)