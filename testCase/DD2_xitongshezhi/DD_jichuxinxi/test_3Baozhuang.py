# coding:utf-8

import unittest
from Base_page.DriverPage import browser
from Base_page.System_settingsPage.JichuPage import Jichu
from common import read_Data
from common.logger import Log
from common import Global_function
from common.Global_function import login_url
from random import randint
import time as t
testData=randint(1,50)
testData1=randint(1,50)
testData2=str(180)+str(randint(10000000,99999999))



class JiChu2(unittest.TestCase):
    log = Log()

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.JC = Jichu(cls.driver)
        cls.JC.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)
        cls.JC.assertion_test1()
        cls.JC.assertion_test2()
        cls.JC.assertion_test11()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    '''
        包装设置
    '''

    def test_bz1(self):
        '''添加包装类型'''
        '''

        :添加包装类型
        :return: 
        '''
        self.log.info('------添加包装类型：start!---------')
        data = self.JC.assertion_test8()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) + 1
        self.JC.assertion_test12(read_Data.getExcel2(testData, 0),
                                 read_Data.getExcel2(testData, 1))
        data3 = self.JC.assertion_test8()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------添加包装类型：stop!---------')

    def test_bz2(self):
        '''编辑包装类型'''
        '''

        :编辑包装类型
        :return: 
        '''
        self.log.info('------编辑包装类型：start!---------')
        #self.JC.assertion_test11()
        self.JC.assertion_test15(read_Data.getExcel2(testData1, 0),
                                 read_Data.getExcel2(testData1, 1))
        #self.assertNotEqual(self.JC.assertion_test13(), read_Data.getExcel2(testData1, 2))
        self.log.info('------编辑包装类型：stop!---------')

    def test_bz3(self):
        '''禁用包装类型'''
        '''

        :禁用包装类型
        :return: 
        '''
        self.log.info('------禁用包装类型：start!---------')
        data = self.JC.assertion_test14()
        if data == read_Data.getExcel2(6, 6):
            self.JC.assertion_test16()
        else:
            self.JC.assertion_test16()
            self.JC.assertion_test16()
        self.assertEqual(self.JC.assertion_test7(), read_Data.getExcel2(11, 6))
        self.log.info('------禁用包装类型：stop!---------')

    def test_bz4(self):
        '''启用包装类型'''
        '''

        :启用包装类型
        :return: 
        '''
        self.log.info('------启用包装类型：start!---------')
        data = self.JC.assertion_test14()
        if data == read_Data.getExcel2(11, 6):
            self.JC.assertion_test16()
        else:
            self.JC.assertion_test16()
            self.JC.assertion_test16()
        self.assertEqual(self.JC.assertion_test7(), read_Data.getExcel2(6, 6))
        self.log.info('------启用包装类型：stop!---------')

if __name__=='__main__':
    unittest.main()