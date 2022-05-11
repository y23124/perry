import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# driver_path = Service('/Users/perry.yen/PycharmProjects/perry/venv/Lib/site-packages/selenium/webdriver/chrome/chromedriver')
# options = Options()
# options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
# driver = webdriver.Chrome(options=options, service=driver_path)
# web_url = 'http://el-test-admin-console.unionfly.co'
# driver.get(web_url)
# time.sleep(2)
#
# driver.find_element(by=By.ID, value='basic_username').send_keys("perry.yen")
# driver.find_element(by=By.ID, value='basic_password').send_keys("qazwsx123")
# driver.find_element(by=By.CLASS_NAME, value='ant-btn').click()
# time.sleep(2)
# r = driver.find_elements(by=By.CLASS_NAME, value="ant-menu-title-content")
# for i in r:
#     if i.text == "System Management":
#         print(i.text)


from test_login import TestRoles

driver_path = Service('/Users/perry.yen/PycharmProjects/perry/venv/Lib/site-packages/selenium/webdriver/chrome/chromedriver')
options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver = webdriver.Chrome(options=options, service=driver_path)
web_url = 'http://el-test-admin-console.unionfly.co'
driver.get(web_url)
time.sleep(2)



