from selenium import webdriver
from selenium.webdriver.support.ui import Select
from PIL import Image
import pytesseract
import time

driver_path = r'C:\Users\ADMIN\PycharmProjects\chromedriver.exe'
web_url = r'http://www.khxhm.com/Register'

driver = webdriver.Chrome(driver_path)
driver.get(web_url)

driver.maximize_window() #瀏覽器最大化
time.sleep(1)

register_account = driver.find_element_by_xpath('//*[@id="articles"]/div[2]/form/fieldset[1]/div[2]/div[1]/input')
register_password = driver.find_element_by_xpath('//*[@id="articles"]/div[2]/form/fieldset[1]/div[3]/div[1]/input')
register_confirm_password = driver.find_element_by_xpath('//*[@id="articles"]/div[2]/form/fieldset[1]/div[4]/div[1]/input')
register_wihdraw_password = driver.find_element_by_xpath('//*[@id="articles"]/div[2]/form/fieldset[1]/div[5]/div[1]/input')
register_real_name = driver.find_element_by_xpath('//*[@id="articles"]/div[2]/form/fieldset[1]/div[6]/div[1]/input')
# register_bank = Select(driver.find_element_by_xpath('//*[@id="articles"]/div[2]/form/fieldset[1]/div[7]/div/select'))
# register_bank_province = driver.find_element_by_xpath('//*[@id="articles"]/div[2]/form/fieldset[1]/div[8]/div[1]/input')
# register_bank_city = driver.find_element_by_xpath('//*[@id="articles"]/div[2]/form/fieldset[1]/div[9]/div[1]/input')
# register_bank_account = driver.find_element_by_xpath('//*[@id="articles"]/div[2]/form/fieldset[1]/div[10]/div[1]/input')

register_account.send_keys('perry0522')
register_password.send_keys('aa1234')
register_confirm_password.send_keys('aa1234')
register_wihdraw_password.send_keys('123')
register_real_name.send_keys('perry')
# register_bank.select_by_index(1)
# register_bank_province.send_keys('test')
# register_bank_city.send_keys('test')
# register_bank_account.send_keys('546321')



