from selenium import webdriver

# 定义一个taobao类
class taobao_infos:

    # 对象初始化
    def __init__(self):
        self.url = url
        self.browser = webdriver.Chrome(chromedriver_path)

    # 登录淘宝
    def login(self):
        # 打开网页
        self.browser.get(self.url)

        register_parent = self.browser.find_element_by_id('parentAccount')
        register_parent.send_keys('perry_04')

        register_account = self.browser.find_element_by_xpath('//*[@id="articles"]/div[2]/form/fieldset[1]/div[2]/div[1]/input')
        register_account.send_keys('perry')

        register_password = self.browser.find_element_by_xpath('//*[@id="articles"]/div[2]/form/fieldset[1]/div[3]/div[1]/input')
        register_password.send_keys('aa1234')

        register_confirm_password = self.browser.find_element_by_xpath('//*[@id="articles"]/div[2]/form/fieldset[1]/div[4]/div[1]/input')
        register_confirm_password.send_keys('aa1234')

        register_wihdraw_password = self.browser.find_element_by_xpath('//*[@id="articles"]/div[2]/form/fieldset[1]/div[5]/div[1]/input')
        register_wihdraw_password.send_keys('123')

        register_real_name = self.browser.find_element_by_xpath('//*[@id="articles"]/div[2]/form/fieldset[1]/div[6]/div[1]/input')
        register_real_name.send_keys('perry')

        register_vcode = self.browser.find_element_by_xpath('//*[@id="checkcode-input-group"]/input')
        register_vcode.send_keys('1234')

        register_submit = self.browser.find_element_by_xpath('//*[@id="btn-submit"]')
        register_submit.click()


if __name__ == "__main__":
    chromedriver_path = r'C:\Users\ADMIN\PycharmProjects\chromedriver.exe'  # 改成你的chromedriver的完整路径地址
    url = r'http://www.rfben.com/Register'
    a = taobao_infos()
    a.login()  # 登录