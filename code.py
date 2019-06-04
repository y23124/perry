from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


class Yahoo:

    def __init__(self):
        self.url = url
        self.browser = webdriver.Chrome(chromedriver_path)


    def register(self):
        self.browser.get(self.url)

        register_firstName = self.browser.find_element_by_id('usernamereg-firstName')
        register_firstName.send_keys('曉明')
        time.sleep(0.5)

        register_lastName = self.browser.find_element_by_id('usernamereg-lastName')
        register_lastName.send_keys('王')
        time.sleep(0.5)

        register_email = self.browser.find_element_by_id('usernamereg-yid')
        register_email.send_keys('test123')
        time.sleep(0.5)

        register_password = self.browser.find_element_by_id('usernamereg-password')
        register_password.send_keys('123456789')
        time.sleep(0.5)

        register_shortCountryCode = Select(self.browser.find_element_by_name('shortCountryCode'))
        op = register_shortCountryCode.first_selected_option
        if op.text != '台灣 ‪(+886)‬':
            register_shortCountryCode.select_by_value('TW')
        time.sleep(0.5)

        register_phone = self.browser.find_element_by_id('usernamereg-phone')
        register_phone.send_keys('0912345679')
        time.sleep(0.5)

        register_month = Select(self.browser.find_element_by_id('usernamereg-month'))
        register_month.select_by_value('6')
        time.sleep(0.5)

        register_day = self.browser.find_element_by_id('usernamereg-day')
        register_day.send_keys('8')
        time.sleep(0.5)

        register_year = self.browser.find_element_by_id('usernamereg-year')
        register_year.send_keys('1990')
        time.sleep(0.5)

        register_sex = self.browser.find_element_by_id('usernamereg-freeformGender')
        register_sex.send_keys('男性')
        time.sleep(0.5)

        register_submit = self.browser.find_element_by_id('reg-submit-button')
        register_submit.click()


if __name__ == "__main__":
    chromedriver_path = r'C:\Users\Administrator\PycharmProjects\perry\chromedriver.exe'
    url = r'https://login.yahoo.com/account/create?.src=twfp&.lang=zh-Hant-TW&.intl=tw&.done=https%3A%2F%2Ftw.yahoo.com%2F&specId=yidReg'
    a = Yahoo()
    a.register()