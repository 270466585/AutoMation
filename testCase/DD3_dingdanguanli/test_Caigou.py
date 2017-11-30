# coding:utf-8

import unittest
from Base_page.DriverPage import browser
from Base_page.Order_managementPage.CaigouPage import Caigoudingdan
from common import read_Data
from common.logger import Log
from common import Global_function
from common.Global_function import login_url
from random import randint
import time as t

testData=randint(1,50)
testData1=randint(1,50)



class CaiGou(unittest.TestCase):
    log = Log()
    @classmethod
    def setUpClass(cls):
        cls.driver =browser()
        cls.CG = Caigoudingdan(cls.driver)
        cls.CG.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)
        cls.CG.assertion_test1()
        cls.CG.assertion_test2()
        t.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_CGDD1(self):
        '''创建采购订单'''
        '''

        :创建采购订单
        :return: 
        '''
        self.log.info('------创建采购订单：start!---------')
        data=self.CG.assertion_test3()
        try:
            data1 = int(data[11]) + 1
        except:
            Data2 = data[12:14]
            data2 = int(Data2) + 1
        self.CG.assertion_test4(read_Data.getExcel2(testData,3),
                                read_Data.getExcel2(testData, 3),
                                testData,
                                read_Data.getExcel2(testData, 3),
                                read_Data.getExcel2(testData, 3))
        data3=self.CG.assertion_test3()
        try:
            data31 = int(data3[11])
            self.assertEqual(data1, data31)
        except:
            Data3 = int(data3[12:14])
            self.assertEqual(Data3, data2)
        self.log.info('------创建采购订单：stop!---------')

    def test_CGDD2(self):
        '''查看采购订单详情'''
        '''

        :查看采购订单详情
        :return:
        '''
        self.log.info('------查看采购订单详情：start!---------')
        self.CG.assertion_test8()
        t.sleep(0.5)
        #self.assertEqual(self.CG.assertion_test7(),'采购订单详情')
        self.CG.assertion_test9()
        self.log.info('------查看采购订单详情：stop!---------')

    def test_XSDD3(self):
        '''编辑采购订单'''
        '''

        :编辑采购订单
        :return:
        '''
        self.log.info('------编辑采购订单：start!---------')
        state = self.CG.assertion_test6()
        try:
            if state == '待审核':
                self.CG.assertion_test10()
                self.assertEqual(self.CG.assertion_test5(),'天府新谷退换库')
            elif state == '执行中':
                self.CG.assertion_test10()
                self.CG.assertion_test10()
                self.assertEqual(self.CG.assertion_test5(), '天府新谷退换库')
        except:
            if state == '已完成':
                print('该订单状态为已完成，无法编辑！！')
            else:
                print('订单当前状态为：{name}，编辑采购订单失败！！'.format(name=state))
        self.log.info('------编辑采购订单：stop!---------')

    def test_XSDD4(self):
        '''审核采购订单'''
        '''

        :审核采购订单
        :return:
        '''
        self.log.info('------审核采购订单：start!---------')
        state = self.CG.assertion_test6()
        try:
            if state == '待审核':
                self.CG.assertion_test11(read_Data.getExcel2(testData,2))
                self.assertEqual(self.CG.assertion_test6(), '执行中')
            elif state == '执行中':
                self.CG.assertion_test10()
                self.CG.assertion_test11(read_Data.getExcel2(testData, 2))
                self.assertEqual(self.CG.assertion_test6(), '执行中')
                print('订单当前状态为：{name}'.format(name=state))
        except BaseException as msg:
            if state == '已完成':
                print('该订单状态为已完成，无需审核！！')
            else:
                print('订单当前状态为：{name}，审核采购订单失败！！'.format(name=state))
            with open('/Users/Macx/PycharmProjects/GYL_project/Log/BaseException.log', 'w+') as file:
                file.write(str(msg))
        self.log.info('------审核采购订单：stop!---------')

    def test_XSDD5(self):
        '''重新编辑执行中的采购订单'''
        '''

        :重新编辑执行中的采购订单
        :return:
        '''
        self.log.info('------重新编辑执行中的采购订单：start!---------')
        state = self.CG.assertion_test6()
        try:
            if state == '执行中':
                self.CG.assertion_test10()
                self.assertEqual(self.CG.assertion_test6(), '待审核')
            elif state == '待审核':
                self.CG.assertion_test11(read_Data.getExcel2(testData, 2))
                self.CG.assertion_test10()
                self.assertEqual(self.CG.assertion_test6(), '待审核')
        except:
            if state == '已完成':
                print('该订单状态为已完成，无法重新编辑！！')
            else:
                print('订单当前状态为：{name}'.format(name=state))
        self.log.info('------重新编辑执行中的采购订单：stop!---------')


    def test_XSDD6(self):
        '''采购订单编号筛选'''
        '''

        :采购订单编号筛选
        :return:
        '''
        self.log.info('------采购订单编号筛选：start!---------')
        self.CG.assertion_test12(testData)
        t.sleep(0.5)
        data = self.CG.assertion_test3()
        try:
            if int(data[11])>0:
                order = self.CG.assertion_test13()
                self.assertIn(str(testData),order)
            else:
                print('模糊输入的采购订单编号为：{name},筛选结果为:{name1}条,没有筛选出包含{name2}的订单编号'
                      .format(name=testData, name1=data[11], name2=testData))
        except:
            if int(data[12:14])>0:
                order = self.CG.assertion_test13()
                self.assertIn(str(testData),order)
            else:
                print('模糊输入的采购订单编号为：{name},筛选结果为:{name1}条,没有筛选出包含{name2}的订单编号'
                      .format(name=testData,name1=data[11],name2=testData))
        self.log.info('------采购订单编号筛选：stop!---------')

if __name__=='__main__':
    unittest.main()
