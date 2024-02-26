from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 初始化WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 日期和货币代号输入
date_input = input("请输入查询日期（格式：YYYYMMDD）: ")
currency_code = input("请输入货币代号（例如：USD, EUR）: ").upper()

# 确保输入的日期格式正确
if len(date_input) != 8 or not date_input.isdigit():
    print("日期格式错误，请输入格式为YYYYMMDD的日期。")
    exit()

# 确保输入的货币代号是有效的
currency_codes = {
    "USD": "美元",
    "EUR": "欧元",
    "JPY": "日元",
    "HKD": "港币",
    "GBP": "英镑",
    "AUD": "澳大利亚元",
    "CAD": "加拿大元",
    "SGD": "新加坡元",
    "CHF": "瑞士法郎",
    "SEK": "瑞典克朗",
    "DKK": "丹麦克朗",
    "NOK": "挪威克朗",
    "KRW": "韩元",
    "MYR": "林吉特",
    "TWD": "新台币",
    "THB": "泰国铢",
    "PHP": "菲律宾比索",
    "RUB": "卢布",
    "NZD": "新西兰元",
    "VND": "越南盾",
    "ZAR": "南非兰特",
    "BRL": "巴西里亚尔",
    "IDR": "印尼卢比",
    "AED": "阿联酋迪拉姆",
    "SAR": "沙特里亚尔",
    "INR": "印度卢比",
    "MXN": "墨西哥比索",
    "CZK": "捷克克朗",
    "PLN": "波兰兹罗提",
    "HUF": "匈牙利福林",
    "TRY": "土耳其里拉",
    "DEM": "德国马克",
    "FIM": "芬兰马克",
    "FRF": "法国法郎",
    "MOP": "澳门元",
    "ESP": "西班牙比塞塔",
    "ITL": "意大利里拉",
    "NLG": "荷兰盾",
    "BEF": "比利时法郎",
    "IDR": "印尼卢比",
}
if currency_code not in currency_codes:
    print(f"货币代号{currency_code}无效。")
    exit()

# 访问中国银行外汇牌价页面
driver.get("https://www.boc.cn/sourcedb/whpj/")

# 等待页面加载完成
driver.implicitly_wait(10)

# 填写日期和货币代号
date_input_element = driver.find_element(By.ID, "erectDate")
date_input_element.send_keys(date_input)
date_input_element = driver.find_element(By.ID, "nothing")
date_input_element.send_keys(date_input)

currency_input_element = driver.find_element(By.ID, "pjname")
currency_input_element.send_keys(currency_codes[currency_code])

# 点击查询按钮
search_button = driver.find_element(By.CSS_SELECTOR, "td[width='30px;'] input.search_btn")
search_button.click()

# 等待页面加载完成
driver.implicitly_wait(10)

# 获取现汇卖出价
try:
    xpath_expression = "/html/body/div/div[4]/table/tbody/tr[2]/td[4]"
    sell_price = driver.find_element(By.XPATH, xpath_expression).text
    print(f"{currency_code}的现汇卖出价为：{sell_price}")
    with open("result.txt", "w") as file:
        file.write(f"{sell_price}\n")
except Exception as e:
    print(f"查询失败：{e}")

# 关闭浏览器
driver.quit()