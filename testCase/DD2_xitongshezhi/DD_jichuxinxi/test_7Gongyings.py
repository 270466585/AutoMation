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



class JiChu6(unittest.TestCase):
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
        cls.JC.assertion_test35()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    '''
        供应商管理
    '''

    def test_gyl1(self):
        '''添加供应商'''
        '''

        :添加供应商
        :return: 
        '''
        self.log.info('------添加供应商：start!---------')
        data = self.JC.assertion_test8()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) + 1
        self.JC.assertion_test36(read_Data.getExcel2(testData, 0),
                                 read_Data.getExcel2(testData, 0), testData2,
                                 read_Data.getExcel2(testData, 0),
                                 read_Data.getExcel2(testData, 0),
                                 read_Data.getExcel2(testData,1))
        data3 = self.JC.assertion_test8()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------添加供应商：stop!---------')


    def test_gyl2(self):
        '''编辑供应商'''
        '''

        :编辑供应商
        :return: 
        '''
        self.log.info('------编辑供应商：start!---------')
        self.JC.assertion_test39(read_Data.getExcel2(testData, 0),
                                 read_Data.getExcel2(testData,1))
        self.assertEqual(self.JC.assertion_test37(), read_Data.getExcel2(testData1, 2))
        self.log.info('------编辑供应商：stop!---------')


    def test_gyl3(self):
        '''禁用供应商'''
        '''

        :禁用供应商
        :return: 
        '''
        self.log.info('------禁用供应商：start!---------')
        data = self.JC.assertion_test38()
        if data == read_Data.getExcel2(12, 6):
            self.JC.assertion_test40()
        else:
            self.JC.assertion_test40()
            self.JC.assertion_test40()
        #self.assertEqual(self.JC.assertion_test38(), read_Data.getExcel2(11, 6))
        self.log.info('------禁用供应商：stop!---------')


    def test_gyl4(self):
        '''启用供应商'''
        '''

        :启用供应商
        :return: 
        '''
        self.log.info('------启用供应商：start!---------')
        data = self.JC.assertion_test38()
        if data == read_Data.getExcel2(11, 6):
            self.JC.assertion_test40()
        else:
            self.JC.assertion_test40()
            self.JC.assertion_test40()
        self.assertEqual(self.JC.assertion_test38(), read_Data.getExcel2(12, 6))
        self.log.info('------启用供应商：stop!---------')

if  __name__=='__main__':
    unittest.main()