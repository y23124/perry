from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re
import time


class Taiwan_railway:

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


    def pid_error(self):
        register_pid = self.browser.find_element_by_id('pid')
        register_pid.send_keys(pid_number)
        self.browser.find_element_by_xpath('/html/body').click()

        try:
            WebDriverWait(self.browser, 1).until(lambda x: x.find_element_by_id("pid-error"))
            pid_error = self.browser.find_element_by_id('pid-error').text
            print(pid_error)
        except:
            print('fail')


    def password_error(self):
        register_password = self.browser.find_element_by_id('pwd')
        for p in password:
            register_password.send_keys(p)
            self.browser.find_element_by_xpath('/html/body').click()

            try:
                WebDriverWait(self.browser, 1).until(lambda x: x.find_element_by_id("pwd-error"))
                password_error = self.browser.find_element_by_id('pwd-error').text
                print(password_error)
            except:
                print('fail')

            time.sleep(1)
            register_password.clear()


    def show_password(self):
        register_password = self.browser.find_element_by_id('pwd')
        register_password.send_keys('aaa12345')

        show_password = self.browser.find_element_by_id('SHBtn')
        show_password.click()

        self.browser.get_screenshot_as_file(r'C:\Users\ADMIN\Desktop\printscreen.png')
        element = self.browser.find_element_by_class_name('input-wrapper')

        x = element.location['x']
        y = element.location['y']
        width = element.location['x'] + element.size['width']
        height = element.location['y'] + element.size['height']

        a = Image.open(r'C:\Users\ADMIN\Desktop\printscreen.png')
        im = a.crop((x, y, width, height))
        im.save(r'C:\Users\ADMIN\Desktop\pwd.png')


    def sex_default(self):
        #male = self.browser.find_element_by_xpath('//*[@id="myForm"]/div[5]/div/div/label[1]')
        #female = self.browser.find_element_by_xpath('//*[@id="myForm"]/div[5]/div/div/label[2]')
        male_check = self.browser.find_element_by_id('gender1').is_selected()
        female_check = self.browser.find_element_by_id('gender2').is_selected()

        if male_check == True and female_check == False:
            print('default')
        else:
            print('fail')


if __name__ == "__main__":
    chromedriver_path = r'C:\Users\ADMIN\PycharmProjects\chromedriver.exe'
    url = r'https://www.railway.gov.tw/tra-tip-web/tip'
    pid_number = '123'
    password = ['aaaaaaaa','12345678','aa1234','aaaa123456789']
    a = Taiwan_railway()
    a. sex_default()