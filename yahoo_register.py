from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time


class Yahoo:

    def __init__(self):
        self.url = url
        self.browser = webdriver.Chrome(chromedriver_path)
        self.browser.get(self.url)
        #self.browser.implicitly_wait(30)
        register_page = self.browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/li[1]/a[2]')
        register_page.click()


    def register_url(self):
        register_url = self.browser.current_url
        check_url = re.search('Person', register_url)

        if check_url == None:
            print('fail')
        else:
            print(register_url)


    def pid(self):
        register_pid = self.browser.find_element_by_id('pid')
        register_pid.send_keys(pid_number)
        self.browser.find_element_by_xpath('/html/body').click()

        try:
            WebDriverWait(self.browser, 1).until(lambda x: x.find_element_by_id("pid-error"))
            pid_error = self.browser.find_element_by_id('pid-error').text
            print(pid_error)
        except:
            print('fail')








if __name__ == "__main__":
    chromedriver_path = r'C:\Users\ADMIN\PycharmProjects\chromedriver.exe'
    url = r'https://www.railway.gov.tw/tra-tip-web/tip'
    pid_number = '123'
    a = Yahoo()
    a.pid()