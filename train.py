from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
register_vcode = driver.find_element_by_xpath('//*[@id="checkcode-input-group"]/input')
register_submit = driver.find_element_by_xpath('//*[@id="btn-submit"]')

register_account.send_keys('perry0522')
time.sleep(1)
register_password.send_keys('aa1234')
time.sleep(1)
register_confirm_password.send_keys('aa1234')
time.sleep(1)
register_wihdraw_password.send_keys('123')
time.sleep(1)
register_real_name.send_keys('perry')
time.sleep(1)
register_vcode.click()
time.sleep(1.5)

picture = driver.find_element_by_xpath('//*[@id="checkcode-input-group"]/span/img').get_attribute('src') #獲取圖片連結
chrome_options = Options() # 啟動無頭模式
chrome_options.add_argument('--headless') #規避google bug
chrome_options.add_argument('--disable-gpu')
co = webdriver.Chrome(driver_path,options=chrome_options)
co.get(picture) #開啟圖片連結
element = co.find_element_by_xpath('/html/body/img')
co.get_screenshot_as_file(r'C:\Users\ADMIN\Desktop\printscreen.png') #截圖存檔

#定位驗證碼位置
x = element.location['x']
y = element.location['y']
width = element.location['x']+element.size['width']
height = element.location['y']+element.size['height']
a = Image.open(r'C:\Users\ADMIN\Desktop\printscreen.png')
im = a.crop((x,y,width,height)) #擷取驗證碼
#im.show()
im.save(r'C:\Users\ADMIN\Desktop\code.png') #截取驗證碼存檔
image = Image.open(r'C:\Users\ADMIN\Desktop\code.png')
imgry = image.convert('L') # 轉化為灰度圖
#imgry.show()
table = [0 if i < 140 else 1 for i in range(256)]
out = imgry.point(table,'1') # 使字型更加突出的顯示
#out.show()
captcha = pytesseract.image_to_string(out) #識別驗證碼
print(captcha)

register_vcode.send_keys(captcha)
time.sleep(1)
register_submit.click()



