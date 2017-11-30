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



class JiChu8(unittest.TestCase):
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
        cls.JC.assertion_test47()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    '''
        合同管理
        '''

    def test_ht1(self):
        '''添加供应链合同'''
        '''

        :添加供应链合同
        :return: 
        '''
        self.log.info('------添加供应链合同：start!---------')
        #self.JC.assertion_test47()
        data = self.JC.assertion_test8()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) + 1
        self.JC.assertion_test48(read_Data.getExcel2(testData,0),
                                 read_Data.getExcel2(testData,0),
                                 read_Data.getExcel2(testData,1),
                                 read_Data.getExcel2(testData,1))
        data3 = self.JC.assertion_test8()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------添加供应链合同：stop!---------')

    def test_ht2(self):
        '''添加客户合同'''
        '''

        :添加客户合同
        :return: 
        '''
        self.log.info('------添加客户合同：start!---------')
        data = self.JC.assertion_test8()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) + 1
        self.JC.assertion_test49(read_Data.getExcel2(testData1,0),
                                 read_Data.getExcel2(testData1,0),
                                 read_Data.getExcel2(testData1,1),
                                 read_Data.getExcel2(testData1,1))
        data3 = self.JC.assertion_test8()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------添加客户合同：stop!---------')

    def test_ht3(self):
        '''

        :编辑合同
        :return: 
        '''
        self.log.info('------编辑合同：start!---------')
        #data = self.JC.assertion_test50()
        self.JC.assertion_test52(read_Data.getExcel2(testData, 0),
                                 read_Data.getExcel2(testData, 1))
        # if self.JC.assertion_test50() == data:
        #     print u'合同编辑失败'
        # else:
        #     self.assertNotEqual(self.JC.assertion_test50(), read_Data.getExcel2(testData, 2))
        self.log.info('------编辑合同：stop!---------')

    def test_ht4(self):
        '''禁用合同'''
        '''

        :禁用合同
        :return: 
        '''
        self.log.info('------禁用合同：start!---------')
        data = self.JC.assertion_test51()
        if data == read_Data.getExcel2(12, 6):
            self.JC.assertion_test53()
        else:
            self.JC.assertion_test53()
            self.JC.assertion_test53()
        self.assertEqual(self.JC.assertion_test51(), read_Data.getExcel2(11, 6))
        self.log.info('------禁用合同：stop!---------')

    def test_ht5(self):
        '''启用合同'''
        '''

        :启用合同
        :return: 
        '''
        self.log.info('------启用合同：start!---------')
        data = self.JC.assertion_test51()
        if data == read_Data.getExcel2(11, 6):
            self.JC.assertion_test53()
        else:
            self.JC.assertion_test53()
            self.JC.assertion_test53()
        self.assertEqual(self.JC.assertion_test51(), read_Data.getExcel2(12, 6))
        self.log.info('------启用合同：stop!---------')


if __name__ == '__main__':
    unittest.main()