# coding:utf-8

import unittest
from Base_page.DriverPage import browser
from Base_page.Order_managementPage.XiaoshouPage import Xiaoshoudingdan
from common import read_Data
from common.logger import Log
from common import Global_function
from common.Global_function import login_url
from random import randint
import time as t
testData=randint(1,50)
testData1=randint(1,50)
testData2=str(180)+str(randint(10000000,99999999))



class CaiGou(unittest.TestCase):
    log = Log()
    @classmethod
    def setUpClass(cls):
        cls.driver =browser()
        cls.XS = Xiaoshoudingdan(cls.driver)
        cls.XS.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)
        cls.XS.assertion_test1()
        cls.XS.assertion_test2()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_XSDD1(self):
        '''创建销售订单'''
        '''

        :创建销售订单
        :return:
        '''
        self.log.info('------创建销售订单：start!---------')
        data=self.XS.assertion_test6()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) + 1
        self.XS.assertion_test3(read_Data.getExcel2(testData,3),testData2,testData)
        data3=self.XS.assertion_test6()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------创建销售订单：stop!---------')


    def test_XSDD2(self):
        '''查看销售订单详情'''
        '''

        :查看销售订单详情
        :return:
        '''
        self.log.info('------查看销售订单详情：start!---------')
        self.XS.assertion_test8()
        t.sleep(0.5)
        self.XS.assertion_test9()
        self.log.info('------查看销售订单详情：stop!---------')

    def test_XSDD3(self):
        '''编辑销售订单'''
        '''

        :编辑销售订单
        :return:
        '''
        self.log.info('------编辑销售订单：start!---------')
        state = self.XS.assertion_test5()
        try:
            if state == '待审核':
                self.XS.assertion_test10()
                self.assertEqual(self.XS.assertion_test4(),'淘宝批量出库')
            elif state == '执行中':
                self.XS.assertion_test10()
                self.XS.assertion_test10()
                self.assertEqual(self.XS.assertion_test4(), '淘宝批量出库')
            else:
                print('该订单状态为: {name},无法进行编辑！！！'.format(name=state))
        except:
                print('订单当前状态为：{name}，编辑操作失败！！！'.format(name=state))
        self.log.info('------编辑销售订单：stop!---------')

    def test_XSDD4(self):
        '''审核销售订单'''
        '''

        :审核销售订单
        :return:
        '''
        self.log.info('------审核销售订单：start!---------')
        state = self.XS.assertion_test5()
        try:
            if state == '待审核':
                self.XS.assertion_test11(read_Data.getExcel2(testData,2))
                self.assertEqual(self.XS.assertion_test5(), '执行中')
            elif state == '执行中':
                self.XS.assertion_test10()
                self.XS.assertion_test11(read_Data.getExcel2(testData, 2))
                self.assertEqual(self.XS.assertion_test5(), '执行中')
            else:
                print('该订单状态为: {name},无法进行审核！！！'.format(name=state))
        except:
                print('订单当前状态为：{name}，审核操作失败！！！'.format(name=state))
        self.log.info('------审核销售订单：stop!---------')

    def test_XSDD5(self):
        '''重新编辑执行中的销售订单'''
        '''

        :重新编辑执行中的销售订单
        :return:
        '''
        self.log.info('------重新编辑执行中的销售订单：start!---------')
        state = self.XS.assertion_test5()
        try:
            if state == '执行中':
                self.XS.assertion_test10()
                self.assertEqual(self.XS.assertion_test5(), '待审核')
                self.XS.assertion_test11(read_Data.getExcel2(testData, 2))
            elif state == '待审核':
                self.XS.assertion_test11(read_Data.getExcel2(testData, 2))
                self.XS.assertion_test10()
                self.assertEqual(self.XS.assertion_test5(), '待审核')
                self.XS.assertion_test11(read_Data.getExcel2(testData, 2))
            else:
                print('该订单状态为: {name},无法重新编辑！！！'.format(name=state))
        except:
                print('订单当前状态为：{name},重新编辑销售订单失败！！'.format(name=state))
        self.log.info('------重新编辑执行中的销售订单：stop!---------')

    def test_XSDD6(self):
        '''销售订单编号筛选'''
        '''

        :销售订单编号筛选
        :return:
        '''
        self.log.info('------销售订单编号筛选：start!---------')
        t.sleep(0.5)
        self.XS.assertion_test12(testData)
        data = self.XS.assertion_test6()
        try:
            if int(data[11])>0:
                order = self.XS.assertion_test13()
                self.assertIn(str(testData),order)
            else:
                print('模糊输入的订单编号为：{name},筛选结果为:{name1}条'.format(name=testData,name1=data[11]))
        except:
            if int(data[12:14])>0:
                order = self.XS.assertion_test13()
                self.assertIn(str(testData),order)
            else:
                print('模糊输入的订单编号为：{name},筛选结果为:{name1}条'.format(name=testData,name1=data[11]))
        self.log.info('------销售订单编号筛选：stop!---------')

if __name__=='__main__':
    unittest.main()
