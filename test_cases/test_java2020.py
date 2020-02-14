#-*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

#定义测试用例所在目录
test_dir = './test_cases'
suit = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

class Test_Java2020(unittest.TestCase):
	def test_java(self):
		#dr = webdriver.Chrome('C:\\Users\\Lily\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-gpu')
		chrome_options.add_argument('--disable-dev-shm-usage')
		dr = webdriver.Chrome(options=chrome_options)
		dr.get('http://localhost:8088/router.html#/')
		dr.implicitly_wait(10)
		dr.maximize_window()
		new_reg = dr.find_element_by_xpath('//*[@id="app"]/div/a[1]/button')
		new_reg_txt = new_reg.text
		self.assertEqual(new_reg_txt,"注册新用户","注册新用户失败！！！")
		print(u"注册新用户成功！")
		print(u"This is Java2020 AutoTest Project!")
		dr.quit()
if __name__ == '__main__':
	unittest.main(verbosity=2)
