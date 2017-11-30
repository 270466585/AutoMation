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



class JiChu3(unittest.TestCase):
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
        cls.JC.assertion_test17()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    '''
        SKU设置
    '''

    def test_SKU1(self):
        '''新增SKU'''
        '''

        :新增SKU
        :return: 
        '''
        self.log.info('------新增SKU：start!---------')
        data = self.JC.assertion_test8()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) + 1
        self.JC.assertion_test18(read_Data.getExcel2(testData, 7),
                                 read_Data.getExcel2(testData1, 7),
                                 read_Data.getExcel2(testData, 7), '12345',
                                 read_Data.getExcel2(testData, 7),
                                 read_Data.getExcel2(testData,0),
                                 read_Data.getExcel2(testData,1))
        data3 = self.JC.assertion_test8()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------新增SKU：stop!---------')

    def test_SKU2(self):
        '''编辑SKU'''
        '''

        :编辑SKU
        :return: 
        '''
        self.log.info('------编辑SKU：start!---------')
        self.JC.assertion_test21(read_Data.getExcel2(testData1, 0),
                                 read_Data.getExcel2(testData1, 1))
        #self.assertNotEqual(self.JC.assertion_test19(), read_Data.getExcel2(testData1, 2))
        self.log.info('------编辑SKU：stop!---------')

    def test_SKU3(self):
        '''禁用SKU'''
        '''

        :禁用SKU
        :return: 
        '''
        self.log.info('------禁用SKU：start!---------')
        t.sleep(0.5)
        data = self.JC.assertion_test20()
        if data == read_Data.getExcel2(12, 6):
            self.JC.assertion_test22()
        else:
            self.JC.assertion_test22()
            self.JC.assertion_test22()
        self.assertEqual(self.JC.assertion_test20(), read_Data.getExcel2(11, 6))
        self.log.info('------禁用SKU：stop!---------')

    def test_SKU4(self):
        '''启用SKU'''
        '''

        :启用SKU
        :return: 
        '''
        self.log.info('------启用SKU：start!---------')
        data = self.JC.assertion_test20()
        if data == read_Data.getExcel2(11, 6):
            self.JC.assertion_test22()
        else:
            self.JC.assertion_test22()
            self.JC.assertion_test22()
        self.assertEqual(self.JC.assertion_test20(), read_Data.getExcel2(12, 6))
        self.log.info('------启用SKU：stop!---------')


if __name__=='__main__':
    unittest.main()