# coding:utf-8

import unittest
from Base_page.DriverPage import browser
from Base_page.Order_managementPage.JihuaPage import Rukujihua
from common import read_Data
from common.logger import Log
from common import Global_function
from common.Global_function import login_url
from random import randint
import time as t

testData=randint(1,50)
testData1=randint(1,50)
testData2='3D01171106'+str(randint(100,999))



class Jihua(unittest.TestCase):
    log = Log()
    @classmethod
    def setUpClass(cls):
        cls.driver =browser()
        cls.JH = Rukujihua(cls.driver)
        cls.JH.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)
        cls.JH.assertion_test1()
        cls.JH.assertion_test2()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_RKJH1(self):
        '''创建多件入库'''
        '''

        :创建清单入库
        :return: 
        '''
        self.log.info('------创建清单入库：start!---------')
        data=self.JH.assertion_test3()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:15]
            data2 = int(Data2) + 1
        self.JH.assertion_test5(read_Data.getExcel2(testData,3))
        data3=self.JH.assertion_test3()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:15])
            self.assertEqual(Data3, data2)
        self.log.info('------创建清单入库：stop!---------')

    def test_RKJH2(self):
        '''创建清单入库'''
        '''

        :创建清单入库
        :return: 
        '''
        self.log.info('------创建清单入库：start!---------')
        data=self.JH.assertion_test3()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:15]
            data2 = int(Data2) + 1
        self.JH.assertion_test4(read_Data.getExcel2(testData,3))
        data3=self.JH.assertion_test3()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:15])
            self.assertEqual(Data3, data2)
        self.log.info('------创建清单入库：stop!---------')


    def test_RKJH3(self):
        '''查看入库计划单详情'''
        '''

        :查看计划入库单详情
        :return: 
        '''
        self.log.info('------查看计划入库单详情：start!---------')
        self.JH.assertion_test9()
        t.sleep(0.5)
        #self.assertEqual(self.CC.assertion_test7(),'入库单详情')
        self.JH.assertion_test10()
        self.log.info('------查看计划入库单详情：stop!---------')

    def test_RKJH4(self):
        '''作废入库计划单'''
        '''

        :作废入库就按单
        :return: 
        '''
        self.log.info('------作废入库计划单：start!---------')
        state = self.JH.assertion_test7()
        try:
            if state == '待入库':
                self.JH.assertion_test11(read_Data.getExcel2(testData, 2))
                t.sleep(0.5)
                self.assertEqual(self.JH.assertion_test7(), '作废')
            elif state == '作废':
                self.JH.assertion_test12()
                self.JH.assertion_test11(read_Data.getExcel2(testData, 2))
                t.sleep(0.5)
                self.assertEqual(self.JH.assertion_test7(), '作废')
            elif state == '入库取消':
                print('订单当前状态为：{name}'.format(name=state))
            else:
                print('订单当前状态为：{name},无法作废！！'.format(name=state))
        except:
            print('订单当前状态为：{name},作废操作失败！！'.format(name=state))
        self.log.info('------作废入库计划单：stop!---------')

    def test_RKJH5(self):
        '''重新编辑入库计划单'''
        '''

        :重新编辑入库计划单
        :return: 
        '''
        self.log.info('------重新编辑入库计划单：start!---------')
        state = self.JH.assertion_test7()
        try:
            if state == '待入库':
                self.JH.assertion_test11(read_Data.getExcel2(testData, 2))
                self.JH.assertion_test12()
                self.assertEqual(self.JH.assertion_test7(), '待入库')
            elif state == '作废':
                self.JH.assertion_test12()
                self.assertEqual(self.JH.assertion_test7(), '待入库')
            elif state == '入库取消':
                print('订单当前状态为：{name}'.format(name=state))
            else:
                print('订单当前状态为：{name},无法重新编辑！！'.format(name=state))
        except:
            print('订单当前状态为：{name},编辑操作失败！！'.format(name=state))
        self.log.info('------重新编辑入库计划单：stop!---------')


    def test_RKJH6(self):
        '''添加入库计划清单管理'''
        '''

        :添加清单管理
        :return: 
        '''
        self.log.info('------添加入库计划清单管理：start!---------')
        state = self.JH.assertion_test7()
        self.JH.assertion_test13()
        data = self.JH.assertion_test15()
        try:
            data = int(data[11]) + 1
        except:
            data=int(data[12:14])+1
        try:
            if state == '待入库':
                self.JH.assertion_test14(testData2)
            elif state == '作废':
                self.JH.assertion_test14(testData2)
            elif state == '入库取消':
                self.JH.assertion_test14(testData2)
            else:
                print('订单当前状态为：{name},无法添加清单管理！！'.format(name=state))
        except:
            print('订单当前状态为：{name},添加清单操作失败！！'.format(name=state))
        Data = self.JH.assertion_test15()
        try:
            Data=int(Data[11])
            self.assertEqual(data, Data)
        except:
            Data=int(Data[12:14])
            self.assertEqual(Data, data)
        self.JH.assertion_test10()
        self.log.info('------添加入库计划清单管理：stop!---------')

    def test_RKJH7(self):
        '''入库计划单订单编号筛选'''
        '''

        :入库计划单订单编号筛选
        :return:
        '''
        self.log.info('------入库计划单订单编号筛选：start!---------')
        self.JH.assertion_test16(testData)
        t.sleep(0.5)
        data = self.JH.assertion_test3()
        try:
            if int(data[11])>0:
                order = self.JH.assertion_test6()
                self.assertIn(str(testData),order)
            else:
                print('模糊输入的订单编号为：{name},筛选结果为:{name1}条,没有筛选出包含{name2}的订单编号'
                      .format(name=testData, name1=data[11], name2=testData))
        except:
            if int(data[12:14])>0:
                order = self.JH.assertion_test6()
                self.assertIn(str(testData),order)
            else:
                print('模糊输入的订单编号为：{name},筛选结果为:{name1}条,没有筛选出包含{name2}的订单编号'
                      .format(name=testData,name1=data[11],name2=testData))
        self.log.info('------入库计划单订单编号筛选：stop!---------')



if __name__=='__main__':
    unittest.main()
