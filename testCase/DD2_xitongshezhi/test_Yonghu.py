# coding:utf-8

import unittest
from Base_page.DriverPage import browser
from Base_page.System_settingsPage.YonghuPage import Yonghu
from common import read_Data
from common.logger import Log
from common import Global_function
from common.Global_function import login_url
from random import randint
import time as t
testData=randint(1,50)
testData1=randint(1,50)


class YongHu(unittest.TestCase):
    log = Log()

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.YH = Yonghu(cls.driver)
        cls.YH.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)
        cls.YH.assertion_test1()
        cls.YH.assertion_test2()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_YHGL1(self):
        '''创建用户'''
        '''

        :创建用户
        :return: 
        '''
        self.log.info('------创建用户：start!---------')
        data = self.YH.assertion_test3()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) + 1
        self.YH.assertion_test4(read_Data.getExcel2(testData,0),read_Data.getExcel2(testData,0))
        data3 = self.YH.assertion_test3()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------创建用户：stop!---------')


    def test_YHGL2(self):
        '''用户详情'''
        '''

        :用户详情
        :return: 
        '''
        self.log.info('------查看用户详情：start!---------')
        self.YH.assertion_test5()
        self.assertEqual(self.YH.assertion_test6(),read_Data.getExcel2(4,6))
        self.YH.assertion_test10()
        self.log.info('------查看用户详情：stop!---------')


    def test_YHGL3(self):
        '''编辑用户'''
        '''

        :编辑用户
        :return: 
        '''
        self.log.info('------编辑用户：start!---------')
        self.YH.assertion_test7(read_Data.getExcel2(testData,1))
        self.assertEqual(self.YH.assertion_test11(),read_Data.getExcel2(testData,1))
        self.log.info('------编辑用户：stop!---------')


    def test_YHGL4(self):
        '''重置密码'''
        '''

        :重置密码
        :return: 
        '''
        self.log.info('------重置密码：start!---------')
        self.YH.assertion_test8()
        print (self.YH.assertion_test12())
        self.log.info('------重置密码：stop!---------')


    def test_YHGL5(self):
        '''冻结用户'''
        '''

        :冻结用户
        :return: 
        '''
        self.log.info('------冻结用户：start!---------')
        data=self.YH.assertion_test12()
        if data==read_Data.getExcel2(6,6):
            self.YH.assertion_test9()
        else:
            self.YH.assertion_test9()
            self.YH.assertion_test9()
        self.assertEqual(self.YH.assertion_test12(),read_Data.getExcel2(5,6))
        self.log.info('------冻结用户：stop!---------')


    def test_YHGL6(self):
        '''激活用户'''
        '''

        :激活用户
        :return: 
        '''
        self.log.info('------激活用户：start!---------')
        data = self.YH.assertion_test12()
        if data == read_Data.getExcel2(5, 6):
            self.YH.assertion_test9()
        else:
            self.YH.assertion_test9()
            self.YH.assertion_test9()
        self.assertEqual(self.YH.assertion_test12(), read_Data.getExcel2(6, 6))
        self.log.info('------激活用户：stop!---------')

if __name__=='__main__':
    unittest.main()