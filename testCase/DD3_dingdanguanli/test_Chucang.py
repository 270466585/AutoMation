# coding:utf-8

import unittest
from Base_page.DriverPage import browser
from Base_page.Order_managementPage.ChucangPage import Chucangruku
from common import read_Data
from common.logger import Log
from common import Global_function
from common.Global_function import login_url
from random import randint
import time as t

testData=randint(1,50)
testData1=randint(1,50)
testData2='3D01171106'+str(randint(100,999))



class Chucang(unittest.TestCase):
    log = Log()
    @classmethod
    def setUpClass(cls):
        cls.driver =browser()
        cls.CC = Chucangruku(cls.driver)
        cls.CC.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)
        cls.CC.assertion_test1()
        cls.CC.assertion_test2()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_CCRK1(self):
        '''创建入库单'''
        '''

        :创建入库单
        :return: 
        '''
        self.log.info('------创建入库单：start!---------')
        data=self.CC.assertion_test3()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) + 1
        self.CC.assertion_test4(read_Data.getExcel2(testData,3),
                                testData)
        data3=self.CC.assertion_test3()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------创建入库单：stop!---------')

    def test_CCRK2(self):
        '''查看入库单详情'''
        '''

        :查看入库单详情
        :return: 
        '''
        self.log.info('------查看入库单详情：start!---------')
        self.CC.assertion_test5()
        t.sleep(0.5)
        #self.assertEqual(self.CC.assertion_test7(),'入库单详情')
        self.CC.assertion_test6()
        self.log.info('------查看入库单详情：stop!---------')

    def test_CCRK3(self):
        '''作废入库单'''
        '''

        :作废入库单
        :return: 
        '''
        self.log.info('------作废入库单：start!---------')
        state = self.CC.assertion_test9()
        try:
            if state == '待入库':
                self.CC.assertion_test11(read_Data.getExcel2(testData, 2))
                t.sleep(0.5)
                self.assertEqual(self.CC.assertion_test9(), '作废')
            elif state == '作废':
                self.CC.assertion_test12()
                self.CC.assertion_test11(read_Data.getExcel2(testData, 2))
                t.sleep(0.5)
                self.assertEqual(self.CC.assertion_test9(), '作废')
            elif state == '入库取消':
                print('订单当前状态为：{name}'.format(name=state))
            else:
                print('订单当前状态为：{name},无法作废！！'.format(name=state))
        except:
            print('订单当前状态为：{name},作废操作失败！！'.format(name=state))
        self.log.info('------作废入库单：stop!---------')

    def test_CCRK4(self):
        '''重新编辑入库单'''
        '''

        :重新编辑入库单
        :return: 
        '''
        self.log.info('------重新编辑入库单：start!---------')
        state = self.CC.assertion_test9()
        try:
            if state == '待入库':
                self.CC.assertion_test11(read_Data.getExcel2(testData, 2))
                self.CC.assertion_test12()
                self.assertEqual(self.CC.assertion_test9(), '待入库')
            elif state == '作废':
                self.CC.assertion_test12()
                self.assertEqual(self.CC.assertion_test9(), '待入库')
            elif state == '入库取消':
                print('订单当前状态为：{name}'.format(name=state))
            else:
                print('订单当前状态为：{name},无法重新编辑！！'.format(name=state))
        except:
            print('订单当前状态为：{name},编辑操作失败！！'.format(name=state))
        self.log.info('------重新编辑入库单：stop!---------')

    def test_CCRK5(self):
        '''添加清单管理'''
        '''

        :添加清单管理
        :return: 
        '''
        self.log.info('------添加清单管理：start!---------')
        state = self.CC.assertion_test9()
        self.CC.assertion_test16()
        data = self.CC.assertion_test15()
        try:
            try:
                data = int(data[11]) + 1
            except:
                data=int(data[12:14])+1
            try:
                if state == '待入库':
                    self.CC.assertion_test14(testData2)
                elif state == '作废':
                    self.CC.assertion_test14(testData2)
                elif state == '入库取消':
                    self.CC.assertion_test14(testData2)
                else:
                    print('订单当前状态为：{name},无法添加清单管理！！'.format(name=state))
            except:
                print('订单当前状态为：{name},添加清单操作失败！！'.format(name=state))
            Data = self.CC.assertion_test15()
            try:
                Data=int(Data[11])
                self.assertEqual(data, Data)
            except:
                Data=int(Data[12:14])
                self.assertEqual(Data, data)
            self.CC.assertion_test6()
        except BaseException:
            self.CC.assertion_test6()
            self.CC.assertion_test6()
            print('添加清单管理失败')
        self.log.info('------添加清单管理：stop!---------')

    def test_CCRK6(self):
        '''入库单订单编号筛选'''
        '''

        :入库单订单编号筛选
        :return:
        '''
        self.log.info('------入库单订单编号筛选：start!---------')
        self.CC.assertion_test13(testData)
        t.sleep(0.5)
        data = self.CC.assertion_test3()
        try:
            if int(data[11])>0:
                order = self.CC.assertion_test8()
                self.assertIn(str(testData),order)
            else:
                print('模糊输入的订单编号为：{name},筛选结果为:{name1}条,没有筛选出包含{name2}的订单编号'
                      .format(name=testData, name1=data[11], name2=testData))
        except:
            if int(data[12:14])>0:
                order = self.CC.assertion_test8()
                self.assertIn(str(testData),order)
            else:
                print('模糊输入的订单编号为：{name},筛选结果为:{name1}条,没有筛选出包含{name2}的订单编号'
                      .format(name=testData,name1=data[11],name2=testData))
        self.log.info('------入库单订单编号筛选：stop!---------')

if __name__=='__main__':
    unittest.main()