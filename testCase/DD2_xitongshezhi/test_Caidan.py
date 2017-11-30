# coding:utf-8

import unittest
from Base_page.DriverPage import browser
from Base_page.System_settingsPage.CaidanPage import Caidanguanli
from common import read_Data
from common.logger import Log
from common import Global_function
from common.Global_function import login_url
from random import randint
import time as t
testData=randint(1,50)
testData1=randint(1,50)


class CaiDan(unittest.TestCase):
    log = Log()
    @classmethod
    def setUpClass(cls):
        cls.driver =browser()
        cls.CD = Caidanguanli(cls.driver)
        cls.CD.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)
        cls.CD.assertion_test1()
        cls.CD.assertion_test2()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_CDGL1(self):
        '''创建菜单'''
        '''

        :创建菜单
        :return: 
        '''
        self.log.info('------创建菜单：start!---------')
        data=self.CD.assertion_test9()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) + 1
        self.CD.assertion_test4()#点击创建新菜单
        self.CD.assertion_test5(read_Data.getExcel2(testData,0))#输入内容
        t.sleep(0.8)
        self.CD.assertion_test6()#点击保存
        t.sleep(0.8)
        self.CD.assertion_test8()#点击确定
        data3=self.CD.assertion_test9()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------创建菜单：stop!---------')


    def test_CDGL2(self):
        '''菜单编辑'''
        '''
        :菜单编辑
        :return: 
        '''
        self.log.info('------编辑菜单：start!---------')
        self.CD.assertion_test10()
        self.CD.assertion_test11()
        self.CD.assertion_test14(read_Data.getExcel2(testData1,0))
        self.CD.assertion_test6()
        self.CD.assertion_test8()
        self.assertEqual(self.CD.assertion_test15(),read_Data.getExcel2(testData1,0))
        self.log.info('------编辑菜单：stop!---------')


    def test_CDGL3(self):
        '''菜单删除'''
        '''
        :菜单删除
        :return: 
        '''
        self.log.info('------删除菜单：start!---------')
        data = self.CD.assertion_test9()
        try:
            data1 = int(data[11]) - 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) - 1
        self.CD.assertion_test10()
        self.CD.assertion_test12()
        self.CD.assertion_test8()
        self.CD.assertion_test8()
        data3 = self.CD.assertion_test9()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------删除菜单：stop!---------')


    def test_CDGL4(self):
        '''菜单下移'''
        '''
        :菜单下移
        :return: 
        '''
        self.log.info('------菜单下移：start!---------')
        self.CD.assertion_test17()
        self.log.info('------菜单下移：stop!---------')


    def test_CDGL5(self):
        '''菜单上移'''
        '''
        :菜单上移
        :return: 
        '''
        self.log.info('------菜单上移：start!---------')
        self.CD.assertion_test18()
        self.log.info('------菜单上移：stop!---------')

if __name__=='__main__':
    unittest.main()