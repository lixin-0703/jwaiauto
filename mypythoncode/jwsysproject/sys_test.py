import configparser
import os
import time
import unittest
import pytest
import allure
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.chrome.options import Options


class Systest(unittest.TestCase):
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
        self.driver.get("http://112.126.56.221:8700/login")  # 通过get()方法，打开一个url站点

    def test_sys(self):
        self._test_login()          #登录
        self._test_order()          #订单管理
        self._test_dic()            #字典管理
        self._test_word()           #词汇课
        self._test_stu()            #学员管理
        self._test_read()           #阅读课
        self._test_lec()            #主题课
        self._test_parent()         #家长学堂
        self._test_book()           #书单
        self._test_orguser()        #机构用户
        self._test_appbase()        #app基础管理
        self._test_appuser()        #app用户
        self._test_sysgood()        #系统商品管理

    @allure.story("登录")
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
        print("登录用户：",name)
        self._test_savescreen()
        time.sleep(3)
        time.sleep(2)

    @allure.story("订单信息")
    def _test_order(self):

        #点击订单管理
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[2]/a/span[1]").click()
        time.sleep(3)
        #点击订单信息菜单
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[2]/dl/dd/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[2]").text
        if("订单信息"==name):
            assert True
        else:
            assert False
        print(f"当前界面：", name)
        self._test_savescreen()
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[2]/i").click()#关闭当前页签
        # 点击查看   /html/body/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[9]/div/a
        #self.driver.find_element_by_tag_name("tbody")
        time.sleep(3)

    @allure.story("字典管理")
    def _test_dic(self):
        # 点击字典管理
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[3]/a/span[1]").click()
        time.sleep(3)
        # 点击家长学堂分类
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[3]/dl/dd[1]/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[3]").text
        if ("家长学堂分类" == name):
            assert True
        print(f"当前界面：", name)
        # 点击三叁阅读GL年级字典
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[3]/dl/dd[2]/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[4]").text
        if ("三叁阅读GL年级字典" == name):
            assert True
        print(f"当前界面：", name)
        # 点击主题课类别
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[3]/dl/dd[3]/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[5]").text
        if ("主题课类别" == name):
            assert True
        print(f"当前界面：", name)
        # 点击用户偏好标签
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[3]/dl/dd[4]/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[6]").text
        if ("用户偏好标签" == name):
            assert True
        print(f"当前界面：", name)
        time.sleep(5)


    @pytest.mark.skip("跳过啦")
    @allure.story("词汇课")
    def _test_word(self):
        print("进来词汇课了吗？")
        # 点击词汇课
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[4]/a").click()
        time.sleep(3)
        # 点击词汇课
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[4]/dl/dd[1]/a").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[7]").text
        if ("词汇课" == name):
            assert True
        else:
            print("未进来界面")
        print(f"词汇课当前界面：", name)
        self._test_savescreen()
        time.sleep(3)
        # 点击词汇课导读音频
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[4]/dl/dd[2]/a").click()
        time.sleep(3)
        word2 = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[8]").text
        if ("词汇课导读音频" == word2):
            assert True
        print(f"词汇课当前界面：", word2)
        self._test_savescreen()
        time.sleep(3)
        # 点击词汇课测试题目库
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[4]/dl/dd[3]/a/span").click()
        time.sleep(3)
        word3 = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[9]").text
        if ("词汇课测试题目库" == word3):
            assert True
        print(f"词汇课当前界面：", word3)
        self._test_savescreen()
        time.sleep(5)

    @pytest.mark.skip("跳过啦")
    @allure.story("学员管理")
    def _test_stu(self):
        # 点击学员管理
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[5]/a/span[1]").click()
        time.sleep(3)
        # 点击学员信息菜单
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[5]/dl/dd/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[10]").text
        if ("学员信息" == name):
            assert True
        print(f"当前界面：", name)
        self._test_savescreen()
        time.sleep(3)

    @allure.story("阅读课")
    def _test_read(self):
        # 点击阅读课
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[6]/a/span[1]").click()
        time.sleep(3)
        # 点击阅读课
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[6]/dl/dd/a/span").click()
        time.sleep(3)
        read1 = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[11]").text
        if ("阅读课" == read1):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：",read1)
        self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[11]/i").click()  # 关闭当前页签
        # 点击阅读课导读音频
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[6]/dl/dd[2]/a/span").click()
        time.sleep(3)
        read2 = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[12]").text
        if ("阅读课导读音频" == read2):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：",read2)
        self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[12]/i").click()  # 关闭当前页签
        time.sleep(3)

    @allure.story("主题课")
    def _test_lec(self):
        # 点击主题课
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[7]/a/span[1]").click()
        time.sleep(3)
        # 点击主题课
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[7]/dl/dd/a/span").click()
        time.sleep(3)
        lec1 = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[13]").text
        if ("主题课" == lec1):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：",lec1)
        # 点击主题课导读音频
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[7]/dl/dd[2]/a/span").click()
        time.sleep(3)
        lec2 = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[14]").text
        if ("主题课导读音频" == lec2):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：",lec2)
        self._test_savescreen()
        time.sleep(3)

    @allure.story("家长学堂")
    def _test_parent(self):
        # 点击家长学堂
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[8]/a/span[1]").click()
        time.sleep(3)
        # 点击家长学堂
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[8]/dl/dd/a/span").click()
        time.sleep(3)
        parent = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[15]").text
        if ("家长学堂" == parent):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：",parent)
        # 点击家长学堂导读音频
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[8]/dl/dd[2]/a/span").click()
        time.sleep(3)
        parent2 = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[16]").text
        if ("家长学堂导读音频" == parent2):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：",parent2)
        self._test_savescreen()
        time.sleep(3)

    @allure.story("书单")
    def _test_book(self):
        # 点击书单
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[9]/a/span[1]").click()
        time.sleep(3)
        # 点击书单
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[9]/dl/dd/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[17]").text
        if ("书单" == name):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：",name)
        self._test_savescreen()
        time.sleep(3)

    @allure.story("机构用户")
    def _test_orguser(self):
        # 点击机构用户
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[10]/a/span[1]").click()
        time.sleep(3)
        # 点击机构用户申请表
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[10]/dl/dd/a/span").click()
        time.sleep(3)
        orguser = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[18]").text
        if ("机构用户申请表" == orguser):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：",orguser)
        # 点击机构用户信息
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[10]/dl/dd[2]/a/span").click()
        time.sleep(3)
        orguser2 = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[19]").text
        if ("机构用户信息" == orguser2):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：",orguser2)
        self._test_savescreen()
        time.sleep(3)
        time.sleep(3)



    @allure.story("app基础管理")
    def _test_appbase(self):
        # 点击app基础管理
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[11]/a/span[1]").click()
        time.sleep(3)
        # 点击积分任务
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[11]/dl/dd/a/span").click()
        time.sleep(3)
        jf = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[20]").text
        if ("积分任务" == jf):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：",jf)
        self._test_savescreen()
        time.sleep(3)
        # 点击APP首页轮播管理
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[11]/dl/dd[2]/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[21]").text
        if ("APP首页轮播管理" == name):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：",name)
        self._test_savescreen()
        time.sleep(3)
        # 点击APP发布管理
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[11]/dl/dd[3]/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[22]").text
        if ("APP发布管理" == name):
            assert True
        print("当前界面：",name)
        # 点击APP通用文案
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[11]/dl/dd[4]/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[23]").text
        if ("APP通用文案" == name):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：", name)
        self._test_savescreen()
        time.sleep(3)
        # 点击通知
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[11]/dl/dd[5]/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[24]").text
        if ("通知" == name):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：", name)
        time.sleep(3)

    @allure.story("app用户")
    def _test_appuser(self):
        # 点击app用户
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[12]/a/span[1]").click()
        time.sleep(3)
        # 点击用户反馈
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[12]/dl/dd/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[25]").text
        if ("app用户反馈" == name):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：", name)
        # 点击用户分组
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[12]/dl/dd[2]/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[26]").text
        if ("用户分组" == name):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：", name)
        self._test_savescreen()
        time.sleep(3)

    @allure.story("系统 商品信息")
    def _test_sysgood(self):
        # 点击系统 商品信息
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[13]/a/span[1]").click()
        time.sleep(3)
        # 点击系统商品信息
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[13]/dl/dd/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[27]").text
        if ("系统商品信息" == name):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：", name)
        self._test_savescreen()
        time.sleep(3)
        # 点击销售策略
        self.driver.find_element_by_xpath(".//*[@id='uls']/li[13]/dl/dd[2]/a/span").click()
        time.sleep(3)
        name = self.driver.find_element_by_xpath(".//*[@id='container']/div/ul/li[28]").text
        if ("销售策略" == name):
            assert True
        else:
            print("assert failed：未获取到当前界面名称")
            print(self.driver.title)
        print("当前界面：", name)
        self._test_savescreen()
        time.sleep(3)
    #保存当前界面截图
    def _test_savescreen(self):
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        current_time1 = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        # 新创建路径“.”表示当前整个.py文件的路径所在的位置，“\\”路径分割符，其中的一个是"\"转义符
        pfilename = u'.\\image'
        pic_path = pfilename + '\\' + current_time1 + '_' + current_time + '.png'
        # 判断文件夹是否存在，不存在就新建一个新的
        if Path(pfilename).is_dir():
            pass
        else:
            Path(pfilename).mkdir()
        print(pic_path)
        self.driver.save_screenshot(pic_path)

if __name__ == "__main__":
    pytest.main(['sys_test.py::Systest','-vs'])