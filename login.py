import requests
import unittest
import report
from PIL import Image
import time


captcha_url = 'http://l08v45.cn/getVerifyCode.lgf'
captcha_res = requests.request('GET', captcha_url)
with open(r'C:\Users\perry\Desktop\321.png', 'wb') as f:
    f.write(captcha_res.content)
code = captcha_res.cookies['JSESSIONID']

image = Image.open(r'C:\Users\perry\Desktop\321.png')
image.show()
c = input("請輸入驗證碼:")

login_url = "http://l08v45.cn/login.lgf"
payload = "username=admin&password=123456&code=" + c
headers = {
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Accept-Language': "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': "l08v45.cn",
    'Origin': "http://l08v45.cn",
    'cookie': "JSESSIONID=" +code,
    'accept-encoding': "gzip, deflate",
    'content-length': "40",
    'Connection': "keep-alive",
    'X-Requested-With': "XMLHttpRequest"
            }

login_res = requests.request("POST", login_url, data=payload, headers=headers)
r = login_res.status_code
print(login_res.json()['message'])

change_pwd_url = 'http://l08v45.cn//reset_login_pwd.lgf'
change_pwd_data = 'id=&oldPwd=123456&newPwd=123456&confirmPwd=123456'
change_pwd_res = requests.request('POST', change_pwd_url, data=change_pwd_data, headers=headers)
change_pwd_code = change_pwd_res.status_code
print(change_pwd_res.json()['message'])


class Login(unittest.TestCase):
    """登入 """

    #用於測試用例執行前的初始化工作
    def setUp(self):
        pass

    def test_login(self):
        self.assertEqual(200,r)

    def tearDown(self):
        pass


class Change_Pwd(unittest.TestCase):
    """ 修改密碼"""

    #用於測試用例執行前的初始化工作
    def setUp(self):
        print("test start")

    def test_change_Pwd(self):
        self.assertEqual(100,change_pwd_code)

    def tearDown(self):
        print("test end")


if __name__ == '__main__':

    suite=unittest.TestSuite()
    suite.addTest(Login("test_login"))
    suite.addTest(Change_Pwd('test_change_Pwd'))
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    #定義報告存放路徑
    filename='./report/'+ now +'.html'
    fp=open(filename,'wb')
    #定義測試報告
    runner=report.HTMLTestRunner(stream=fp,title='測試報告',tester='Perry')
    runner.run(suite)
    fp.close()#關閉報告檔案





