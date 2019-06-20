from selenium import webdriver
from PIL import Image
import pytesseract
import time

driver_path = r'C:\Users\ADMIN\PycharmProjects\chromedriver.exe'
web_url = r'url'
driver = webdriver.Chrome(driver_path)
driver.get(web_url)

driver.maximize_window() #瀏覽器最大化
time.sleep(1)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #滾輪至最底部
time.sleep(1)
driver.find_element_by_xpath('//*[@id="checkcode-input-group"]/input').click()
time.sleep(1)

picture = driver.find_element_by_xpath('//*[@id="checkcode-input-group"]/span/img').get_attribute('src') #獲取圖片連結
driver.get(picture) #開啟圖片連結
element = driver.find_element_by_xpath('/html/body/img')
driver.get_screenshot_as_file(r'C:\Users\ADMIN\Desktop\printscreen.png') #截圖存檔

#定位驗證碼位置
x = element.location['x'] #X軸
y = element.location['y'] #Y軸
width = element.location['x']+element.size['width'] #寬
height = element.location['y']+element.size['height'] #高
a = Image.open(r'C:\Users\ADMIN\Desktop\printscreen.png')
im = a.crop((x,y,width,height)) #截圖檔裡擷取驗證碼
#im.show()
im.save(r'C:\Users\ADMIN\Desktop\code.png') #截取的驗證碼存檔
image = Image.open(r'C:\Users\ADMIN\Desktop\code.png')
# 轉化為灰度圖
imgry = image.convert('L')
#imgry.show()
table = [0 if i < 140 else 1 for i in range(256)]
# 使字型更加突出的顯示
out = imgry.point(table,'1')
#out.show()
captcha = pytesseract.image_to_string(out) #識別驗證碼
print(type(captcha))
