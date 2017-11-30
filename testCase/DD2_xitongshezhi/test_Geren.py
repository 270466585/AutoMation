# coding:utf-8

import unittest
from Base_page.DriverPage import browser
from Base_page.System_settingsPage.GerenPage import Geren
from common import read_Data
from common.logger import Log
from common import Global_function
from common.Global_function import login_url
from random import randint
import time as t
testData=randint(1,50)
testData1=randint(1,50)


class GeRen(unittest.TestCase):
    log = Log()

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.GR = Geren(cls.driver)
        cls.GR.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_GRXX1(self):
        '''

        :修改用户名称
        :return: 
        '''
        self.log.info('------修改用户名称：start!---------')
        self.GR.assertion_test1()
        self.GR.assertion_test2()
        self.GR.assertion_test3(read_Data.getExcel2(7,6))
        self.assertEqual(self.GR.assertion_test5(),read_Data.getExcel2(7,6))
        self.log.info('------修改用户名称：stop!---------')


    def test_GRXX2(self):
        '''

        :修改密码
        :return: 
        '''
        self.log.info('------修改密码：start!---------')
        self.GR.assertion_test1()
        self.GR.assertion_test2()
        self.GR.assertion_test4(read_Data.getExcel2(8,6),
                                read_Data.getExcel2(8,6),
                                read_Data.getExcel2(8,6)
                                )
        print('修改后的密码为：%s' % read_Data.getExcel2(8 , 6))
        self.log.info('------修改密码：stop!---------')




if __name__=='__main__':
    unittest.main()
