# coding:utf-8

import unittest
from Base_page.DriverPage import browser
from Base_page.LoginPage import Loginpage
from common import read_Data
from common.logger import Log
from common.Global_function import login_url





class Login_logout(unittest.TestCase):

    log=Log()
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.Login=Loginpage(cls.driver)
        cls.Login.open(login_url,u'登录')
        cls.driver.implicitly_wait(5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_logout1(self):
        '''用户名密码为空'''
        '''
        
        :param username: null
        :param password: null
        :param text:请输入用户名
        :return: 
        '''
        self.log.info('------用户名密码为空：start!---------')
        self.Login.input_username(read_Data.getExcel1(1,0))
        self.Login.input_password(read_Data.getExcel1(1,1))
        self.Login.click_submit()
        self.assertEqual(self.Login.assertion_text1(),read_Data.getExcel1(1,2))
        self.log.info('------用户名密码为空：stop!---------')


    def test_login_logout2(self):
        '''用户名为空，密码正确'''
        '''
        用户名为空，密码正确
        :param username: null
        :param password: 123456
        :param text:请输入用户名
        :return: 
        '''
        self.log.info('------用户名为空，密码正确：start!---------')
        self.Login.input_username(read_Data.getExcel1(2, 0))
        self.Login.input_password(read_Data.getExcel1(2, 1))
        self.Login.click_submit()
        self.assertEqual(self.Login.assertion_text1(), read_Data.getExcel1(2, 2))
        self.log.info('------用户名为空，密码正确：stop!---------')


    def test_login_logout3(self):
        '''用户名正确，密码为空'''
        '''
        用户名正确，密码为空
        :param username: zhaoqiao
        :param password: null
        :param text:请输入密码
        :return: 
        '''
        self.log.info('------用户名正确，密码为空：start!---------')
        self.Login.input_username(read_Data.getExcel1(3, 0))
        self.Login.input_password(read_Data.getExcel1(3, 1))
        self.Login.click_submit()
        self.assertEqual(self.Login.assertion_text3(), read_Data.getExcel1(3, 2))
        self.log.info('------用户名正确，密码为空：stop!---------')


    def test_login_logout4(self):
        '''用户名密码为大写'''
        '''
        
        :param username: ZHAOQIAO
        :param password: 123456
        :param text:用户名或者密码错误!
        :return: 
        '''
        self.log.info('------用户名密码为大写：start!---------')
        self.Login.input_username(read_Data.getExcel1(4, 0))
        self.Login.input_password(read_Data.getExcel1(4, 1))
        self.Login.click_submit()
        self.assertEqual(self.Login.assertion_text4(), read_Data.getExcel1(4, 2))
        self.log.info('------用户名密码为大写：stop!---------')


    def test_login_logout5(self):
        '''用户名密码正确'''
        '''
 
        :param username: zhaoqiao
        :param password: 123456
        :param text:赵大乔
        :return: 
        '''
        self.log.info('------用户名密码正确：start!---------')
        self.Login.input_username(read_Data.getExcel1(5, 0))
        self.Login.input_password(read_Data.getExcel1(5, 1))
        self.Login.click_submit()
        self.assertEqual(self.Login.assertion_text6(), read_Data.getExcel1(5, 2))
        self.log.info('------用户名密码正确：stop!---------')


    def test_login_logout6(self):
        '''退出登录'''
        '''
        :param logout:
        :return: 
        '''
        self.log.info('------退出登录：start!---------')
        self.Login.assertion_text7()
        self.log.info('------退出登录：stop!---------')


if __name__=='__main__':
    unittest.main()

