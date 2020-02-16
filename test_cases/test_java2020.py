#-*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from pyvirtualdisplay import Display

#定义测试用例所在目录
#test_dir = './test_cases'
#suit = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

class Test_Java2020(unittest.TestCase):
	def test_java(self):
		#windows下使用
		#dr = webdriver.Chrome('C:\\Users\\Lily\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')
		#dr = webdriver.Chrome()
		#linux下使用
		print("webdriver")
		#chrome_options = Options()
		#chrome_options.set_headless()
		#chrome_options.add_argument('--no-sandbox')
		#chrome_options.add_argument('--disable-dev-shm-usage')
		#chrome_options.add_argument('--headless')
		#chrome_options.add_argument('blink-settings=imagesEnabled=false')
		#chrome_options.add_argument('--disable-gpu')
		print("webdriver开始启动")
		#dr = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=chrome_options)
		#dr = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
		print("webdriver启动中")
		display = Display(visible=0, size=(1200, 800))
		display.start()
		dr = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
		dr.get('http://localhost:8088/router.html/')
		#dr.get('http://192.168.0.66:8088/router.html/')
		print("webdriver启动结束")
		dr.implicitly_wait(30)
		dr.maximize_window()
		print("==1")
		new_reg = dr.find_element_by_xpath('//*[@id="app"]/div/a[1]/button')
		print("==2")
		new_reg_txt = new_reg.text
		self.assertEqual(new_reg_txt,"注册新用户","注册新用户失败！！！")
		print(u"注册新用户成功！")
		print(u"This is Java2020 AutoTest Project!")
		dr.quit()
		display.stop
if __name__ == '__main__':
	unittest.main(verbosity=2)
