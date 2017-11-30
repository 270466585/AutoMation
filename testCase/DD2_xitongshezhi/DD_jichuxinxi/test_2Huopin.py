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


class JiChu1(unittest.TestCase):
    log = Log()
    @classmethod
    def setUpClass(cls):
        cls.driver=browser()
        cls.JC = Jichu(cls.driver)
        cls.JC.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)
        cls.JC.assertion_test1()
        cls.JC.assertion_test2()
        cls.JC.assertion_test10()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    '''
    货品类别设置
    '''
    def test_hp1(self):
        '''添加货品类别'''
        '''

        :添加货品类别
        :return: 
        '''
        self.log.info('------添加货品类别：start!---------')
        data = self.JC.assertion_test8()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) + 1
        self.JC.assertion_test3(read_Data.getExcel2(testData,0),
                                read_Data.getExcel2(testData,1))
        data3 = self.JC.assertion_test8()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------添加货品类别：stop!---------')


    def test_hp2(self):
        '''编辑货品类别'''
        '''

        :编辑货品类别
        :return: 
        '''
        self.log.info('------编辑货品类别：start!---------')
        #data=self.JC.assertion_test9()
        self.JC.assertion_test4(read_Data.getExcel2(testData,0),
                                read_Data.getExcel2(testData,1))
        # if self.JC.assertion_test9()==data:
        #     print u'货品类别编辑失败'
        # elif self.JC.assertion_test9()==read_Data.getExcel2(testData1,1):
        #     self.assertEqual(self.JC.assertion_test9(),read_Data.getExcel2(testData1,1))
        # else:
        #     self.assertNotEqual(self.JC.assertion_test9(), read_Data.getExcel2(testData1, 1))
        #     print u'当前位置文本为：%s,预期文本为：%s'%(self.JC.assertion_test9(),read_Data.getExcel2(testData1, 1))
        # try:
        #     self.assertIn(read_Data.getExcel2(testData1, 0),self.JC.assertion_test9())
        # except:
        #     self.assertIn(read_Data.getExcel2(testData1, 1), self.JC.assertion_test9())
        self.log.info('------编辑货品类别：stop!---------')


    def test_hp3(self):
        '''禁用货品类别'''
        '''

        :禁用货品类别
        :return: 
        '''
        self.log.info('------禁用货品类别：start!---------')
        data=self.JC.assertion_test7()
        if data==read_Data.getExcel2(6,6):
            self.JC.assertion_test5()
        else:
            self.JC.assertion_test5()
            self.JC.assertion_test5()
        self.assertEqual(self.JC.assertion_test7(), read_Data.getExcel2(11, 6))
        self.log.info('------禁用货品类别：stop!---------')

    def test_hp4(self):
        '''启用货品类别'''
        '''

        :启用货品类别
        :return: 
        '''
        self.log.info('------启用货品类别：start!---------')
        data = self.JC.assertion_test7()
        if data == read_Data.getExcel2(11, 6):
            self.JC.assertion_test5()
        else:
            self.JC.assertion_test5()
            self.JC.assertion_test5()
        self.assertEqual(self.JC.assertion_test7(), read_Data.getExcel2(6, 6))
        self.log.info('------启用货品类别：stop!---------')

if __name__=='__main__':
    unittest.main()