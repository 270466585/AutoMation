# coding:utf-8

import unittest
from Base_page.DriverPage import browser
from Base_page.System_settingsPage.JuesePage import Juese
from common import read_Data
from common.logger import Log
from common import Global_function
from common.Global_function import login_url
from random import randint
import time as t
testData=randint(1,50)
testData1=randint(1,50)


class JueSe(unittest.TestCase):
    log = Log()

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.JS = Juese(cls.driver)
        cls.JS.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)
        cls.JS.assertion_test1()
        cls.JS.assertion_test2()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_JSGL1(self):
        '''创建角色'''
        '''

        :创建角色
        :return: 
        '''
        self.log.info('------创建角色：start!---------')
        data = self.JS.assertion_test3()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) + 1
        self.JS.assertion_test4(read_Data.getExcel2(testData,0),read_Data.getExcel2(testData,0))
        data3 = self.JS.assertion_test3()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------创建角色：stop!---------')


    def test_JSGL2(self):
        '''查看角色详情'''
        '''

        :查看角色详情
        :return: 
        '''
        self.log.info('------查看详情：start!---------')
        self.JS.assertion_test5()
        self.assertEqual(self.JS.assertion_test6(),read_Data.getExcel2(3,6))
        self.JS.assertion_test11()
        self.log.info('------查看详情：stop!---------')


    def test_JSGL3(self):
        '''编辑角色'''
        '''

        :编辑角色
        :return: 
        '''
        self.log.info('------编辑角色：start!---------')
        self.JS.assertion_test7(read_Data.getExcel2(testData,1),read_Data.getExcel2(testData1,1))
        self.assertEqual(self.JS.assertion_test8(),read_Data.getExcel2(testData,1))
        self.log.info('------编辑角色：stop!---------')


    def test_JSGL4(self):
        '''编辑权限'''
        '''

        :编辑权限
        :return: 
        '''
        self.log.info('------编辑权限：start!---------')
        self.JS.assertion_test9()
        self.log.info('------编辑权限：stop!---------')


    def test_JSGL5(self):
        '''删除角色'''
        '''

        :删除角色
        :return: 
        '''
        self.log.info('------删除角色：start!---------')
        self.JS.assertion_test10()
        self.log.info('------删除角色：stop!---------')
if __name__=='__main__':
    unittest.main()