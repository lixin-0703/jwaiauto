import configparser
import os
import time
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class Aitest(unittest.TestCase):
    # 读入配置文件
    def get_config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.environ['HOME'], 'iselenium.ini'))
        return config

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        config = self.get_config()
        # 控制是否采用无界面形式运行自动化测试
        try:
            using_headless = os.environ["using_headless"]
        except KeyError:
            using_headless = None
            print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')

        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print('使用无界面方式运行')
            chrome_options.add_argument("--headless")
        print("获取chroomdriver",config.read(os.path.join(os.environ['HOME'], 'iselenium.ini')))
        print(config.get('driver', 'chrome_driver'))
        self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'),
                                       options=chrome_options)
        self.driver.maximize_window()  # 最大化浏览器
        self.driver.get("http://112.126.56.221:8300/login")  # 通过get()方法，打开一个url站点

    def test_ai(self):
        self._test_login()
        time.sleep(2)
        self._test_book()
    def _test_login(self):
        #输入用户名
        self.driver.find_element_by_name("username").clear()
        self.driver.find_element_by_name("username").send_keys("admin")
        #输入密码
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("123456")
        time.sleep(15)
        #手动输入验证码
        #点击登录按钮
        self.driver.find_element_by_xpath("html/body/div[1]/form/input[3]").click()
        name = self.driver.find_element_by_xpath("html/body/div[1]/div[1]/ul/li[1]").text
        if(name=="管理员"):
            assert True
        print(f"登录用户：",name)
        time.sleep(2)
    def _test_book(self):

        #点击书单管理 .//*[@id='uls']/li[3]/a
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[2]/a").click()
        time.sleep(3)
        #点击书单列表菜单
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[2]/dl/dd[1]/a/span").click()
        time.sleep(3)
        #//*[@id="layui-laypage-1"]/span[4]
        #count = self.driver.find_element_by_xpath("html/body/div[3]/div[2]/div[1]/div[1]/span[4]").text
        self.driver.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[15]/div/a[1]").click()
        #print("书单数量",count)
        #验证书单列表界面是否找到
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[2]").text
        if("书单列表"==name):
            assert True
        print(f"当前界面：", name)
        #点击体裁列表菜单
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[2]/dl/dd[2]/a/span").click()
        time.sleep(3)
        # 验证体裁列表界面是否找到
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[3]").text
        if ("体裁列表" == name):
            assert True
        print(f"当前界面：", name)
        # 点击主题列表菜单
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[2]/dl/dd[3]/a/span").click()
        time.sleep(3)
        # 验证主题列表界面是否找到
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[4]").text
        if ("主题列表" == name):
            assert True
        print(f"当前界面：", name)
        #点击题目管理
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[3]/a").click()
        time.sleep(3)
        #阅读偏好测试题
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[3]/dl/dd[1]/a/span").click()
        time.sleep(3)
        # 验证阅读偏好测试题界面是否找到
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[5]").text
        if ("阅读偏好测试题" == name):
            assert True
        print(f"当前界面：", name)
        # 书单BL测试题目库
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[3]/dl/dd[2]/a/span").click()
        time.sleep(3)
        # 验证书单BL测试题目库界面是否找到
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[6]").text
        if ("书单BL测试题目库" == name):
            assert True
        print(f"当前界面：", name)
        # 三叁测试热身题
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[3]/dl/dd[3]/a/span").click()
        time.sleep(3)
        # 验证三叁测试热身题界面是否找到
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[7]").text
        if ("三叁测试热身题" == name):
            assert True
        print(f"当前界面：", name)
        # 三叁测试动态题
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[3]/dl/dd[4]/a/span").click()
        time.sleep(3)
        # 验证三叁测试动态题界面是否找到
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[8]").text
        if ("三叁测试动态题" == name):
            assert True
        print(f"当前界面：", name)
        # 三叁测试套题
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[3]/dl/dd[5]/a/span").click()
        time.sleep(3)
        # 验证三叁测试套题界面是否找到
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[9]").text
        if ("三叁测试套题" == name):
            assert True
        print(f"当前界面：", name)

if __name__ == "__main__":
    pytest.main(['ai_test.py::Aitest','-v'])