import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver_path = Service('/Users/perry.yen/PycharmProjects/perry/venv/Lib/site-packages/selenium/webdriver/chrome/chromedriver')
options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver = webdriver.Chrome(options=options, service=driver_path)
web_url = 'http://el-test-admin-console.unionfly.co'
driver.get(web_url)
time.sleep(1)

# language = driver.find_element(by = By.XPATH, value = '//*[@id="root"]/div/div[1]/span')
# time.sleep(5)
# language.click()

# language_zh = driver.find_elements(by=By.CLASS_NAME, value='gx-language-text')
# language_zh.text
# print(language_zh)

# class TestLogin:
#
#     def test_A(username,password):
#         driver.find_element(by=By.ID, value='basic_username').send_keys(username)
#         driver.find_element(by=By.ID, value='basic_password').send_keys(password)
#         driver.find_element(by=By.CLASS_NAME, value='ant-btn').click()
#         time.sleep(2)
#         url = driver.current_url
#         if "verification-codes" in url:
#             result = True
#         else:
#             result = False
#         assert result
#
#     def test_B(self):
#         driver.find_element(by=By.ID, value='basic_username').send_keys("perryyen")
#         driver.find_element(by=By.ID, value='basic_password').send_keys("qazwsx123")
#         driver.find_element(by=By.CLASS_NAME, value='ant-btn').click()
#         time.sleep(3)
#         result =driver.find_element(by=By.CLASS_NAME, value="ant-modal-confirm-title").text
#         assert result == "Error"
#
#     def test_C(self):
#         driver.find_element(by=By.ID, value='basic_username').send_keys("perry.yen")
#         driver.find_element(by=By.ID, value='basic_password').send_keys("qazwsx124")
#         driver.find_element(by=By.CLASS_NAME, value='ant-btn').click()
#         time.sleep(1)
#         result = driver.find_element(by=By.CLASS_NAME, value="ant-modal-confirm-title").text
#         assert result == "Error"
#
#
# class TestRoles:
#
#     login = TestLogin.test_A(username="perry.yen", password="qazwsx123")
#     time.sleep(2)
#     def test_D(self):
#         menu = driver.find_elements(by=By.CLASS_NAME, value="ant-menu-title-content")
#         for system_management in menu:
#             if system_management.text == "System Management":
#                 system_management.click()
#                 time.sleep(1)
#
#         driver.find_element(by=By.CLASS_NAME, value="icon-user-o").click()
#         time.sleep(1)
#
#         role_add_btn = driver.find_elements(by=By.CLASS_NAME, value="ant-btn-primary")
#         for add_role in role_add_btn:
#             if add_role.text == "Add Role":
#                 add_role.click()
#                 time.sleep(1)
#
#         driver.find_element(by=By.ID, value="displayName").send_keys("autotest")
#         driver.find_element(by=By.ID, value="description").send_keys("test")
#         driver.find_element(by=By.CLASS_NAME, value="ant-select-selector").click()
#         time.sleep(2)
#
#         select = driver.find_element(by=By.ID, value="permissions").is_displayed()
#         if select == True:
#             elem = driver.find_element(by=By.CLASS_NAME, value="ant-select-selection-item-content")
#             print(elem.text)
#         time.sleep(2)
#         driver.close()

class TestLoginLock:

    def test_login_lock(selef,usn,pwd):
        driver.find_element(by=By.ID, value="basic_username").send_keys(usn)
        driver.find_element(by=By.ID, value="basic_password").send_keys(pwd)
        driver.find_element(by=By.CLASS_NAME, value="gx-mb-0").click()
        time.sleep(1)
        count = 0

        while True:
            error_msg = driver.find_element(by=By.CLASS_NAME, value="ant-modal-confirm-content").text
            if error_msg == "Invalid administrator account credential! Please re-input your login information.":
                OK = driver.find_elements(by=By.CLASS_NAME, value="ant-btn-primary")

                for OK_btn in OK:
                    if OK_btn.text == "OK":
                        OK_btn.click()

                time.sleep(1)
                count = count + 1
                driver.find_element(by=By.CLASS_NAME, value="gx-mb-0").click()
                time.sleep(1)

            elif error_msg == "User is frozen":
                print("登入錯誤次數：",count,"次，已被凍結")
                break

        driver.close()

run = TestLoginLock()
run.test_login_lock(usn="perry.yen",pwd="qazwsx122")





