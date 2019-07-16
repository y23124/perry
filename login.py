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
payload = "username=admin&password=123456&code="+c
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
print(login_res.json()['message'])


insertUserLevel_url = 'http://l08v45.cn/userlevel/save.lgf'
searchUserLevel_url = 'http://l08v45.cn/userlevel/list.lgf'


class Login(unittest.TestCase):
    """登入 """
    #用於測試用例執行前的初始化工作
    def setUp(self):
        pass

    def test_login(self):
        self.assertEqual('SUCCESS',login_res.json()['status'], msg=login_res.json())

    def tearDown(self):
        pass


class UserLevel(unittest.TestCase):
    """會員級別新增"""
    def setUp(self):
        pass

    def test_null(self):
        """參數全空"""
        nullUserLevel_data = 'code=&name=&enable='
        nullUserLevel_res = requests.request('POST', insertUserLevel_url, data=nullUserLevel_data, headers=headers)
        self.assertEqual('SUCCESS',nullUserLevel_res.json()['status'], msg=nullUserLevel_res.json())

    def test_type(self):
        """參數類型"""
        typeUserLevel_data = 'code=test&name=test&enable=test'
        typeUserLevel_res = requests.request('POST', insertUserLevel_url, data=typeUserLevel_data, headers=headers)
        self.assertEqual(200,typeUserLevel_res.status_code)

    def test_insert(self):
        """正確參數"""
        insertUserLevel_data = 'code=123&name=perry&enable=true'
        insertUserLevel_res = requests.request('POST', insertUserLevel_url, data=insertUserLevel_data, headers=headers)
        self.assertEqual('SUCCESS',insertUserLevel_res.json()['status'])

    def test_search(self):
        """查詢是否新增"""
        searchUserLevel_data = 'darw=&orderBy=add_time&orderType=desc&queryPage=1&pageSize=10&nameLike=perry&enable='
        searchUserLevel_res = requests.request('POST', searchUserLevel_url, data=searchUserLevel_data,headers=headers)
        self.assertEqual('SUCCESS',searchUserLevel_res.json()['status'])

    def tearDown(self):
        pass



if __name__ == '__main__':

    suite=unittest.TestSuite()
    suite.addTest(Login("test_login"))
    suite.addTest(UserLevel('test_null'))
    suite.addTest(UserLevel('test_type'))
    suite.addTest(UserLevel('test_insert'))
    suite.addTest(UserLevel('test_search'))
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    #定義報告存放路徑
    filename=r'C:\Users\perry\perry\report\Result_'+ now +'.html'
    fp=open(filename,'wb')
    #定義測試報告
    runner=report.HTMLTestRunner(stream=fp,title='測試報告',tester='Perry',verbosity=2)
    runner.run(suite)
    fp.close()#關閉報告檔案





