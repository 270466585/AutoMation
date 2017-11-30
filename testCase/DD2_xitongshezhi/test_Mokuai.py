# coding:utf-8

import unittest
from Base_page.DriverPage import browser
from Base_page.System_settingsPage.MokuaiPage import Mokuai
from common import read_Data
from common.logger import Log
from common import Global_function
from common.Global_function import login_url
from random import randint
import time as t
testData=randint(1,50)
testData1=randint(1,50)



class MoKuai(unittest.TestCase):
    log = Log()

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.MK = Mokuai(cls.driver)
        cls.MK.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)
        cls.MK.assertion_test1()
        cls.MK.assertion_test2()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_CDGL1(self):
        '''创建模块'''
        '''

        :创建模块
        :return: 
        '''
        self.log.info('------创建模块：start!---------')
        data = self.MK.assertion_test3()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) + 1
        self.MK.assertion_test4(read_Data.getExcel2(testData,0),read_Data.getExcel2(testData,5))
        data3 = self.MK.assertion_test3()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------创建模块：stop!---------')


    def test_CDGL2(self):
        '''查看模块'''
        '''

        :查看模块
        :return: 
        '''
        self.log.info('------查看模块：start!---------')
        self.MK.assertion_test5()
        data=self.MK.assertion_test6()
        self.assertEqual(self.MK.assertion_test6(),read_Data.getExcel2(1,6))
        self.MK.assertion_test7()
        self.log.info('------查看模块：stop!---------')


    def test_CDGL3(self):
        '''编辑模块'''
        '''

        :编辑模块
        :return: 
        '''
        self.log.info('------编辑模块：start!---------')
        self.MK.assertion_test8(read_Data.getExcel2(testData1,0),read_Data.getExcel2(testData,5))
        self.assertNotEqual(self.MK.assertion_test9(),read_Data.getExcel2(testData1,0))
        self.log.info('------编辑模块：stop!---------')


    def test_CDGL4(self):
        '''删除模块'''
        '''

        :删除模块
        :return: 
        '''
        self.log.info('------删除模块：start!---------')
        data = self.MK.assertion_test3()
        try:
            data1 = int(data[11]) - 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) - 1
        self.MK.assertion_test10()
        data3 = self.MK.assertion_test3()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------删除模块：stop!---------')


    def test_CDGL5(self):
        '''上移模块'''
        '''

        :上移模块
        :return: 
        '''
        self.log.info('------上移模块：start!---------')
        self.MK.assertion_test12()
        self.log.info('------上移模块：stop!---------')

    def test_CDGL6(self):
        '''下移模块'''
        '''

        :下移模块
        :return: 
        '''
        self.log.info('------下移模块：start!---------')
        self.MK.assertion_test13()
        self.log.info('------下移模块：stop!---------')


if __name__=='__main__':
    unittest.main()