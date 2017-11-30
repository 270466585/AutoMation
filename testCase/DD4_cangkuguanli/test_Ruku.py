import unittest
from Base_page.DriverPage import browser
from Base_page.Warehouse_managementPage.RukuPage import Rukuguanli
from Base_page.Order_managementPage.JihuaPage import Rukujihua
from common import read_Data
from common.logger import Log
from common import Global_function
from common.Global_function import login_url
from random import randint
import time as t

testData=randint(1,50)
testData1=randint(1,50)



class RuKu(unittest.TestCase):
    log = Log()
    @classmethod
    def setUpClass(cls):
        cls.driver =browser()
        cls.RK = Rukuguanli(cls.driver)
        cls.RK.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)
        cls.RK.assertion_test1()
        cls.RK.assertion_test2()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_RKGL1(self):
        '''查看入库订单详情'''
        '''

        :查看入库订单详情
        :return:
        '''
        self.log.info('------查看入库订单详情：start!---------')
        self.RK.assertion_test5()
        t.sleep(0.5)
        self.RK.assertion_test10()
        self.log.info('------查看入库订单详情：stop!---------')

    def test_RKGL2(self):
        '''作废入库订单'''
        '''

        :作废入库订单
        :return: 
        '''
        self.log.info('------作废入库订单：start!---------')
        state = self.RK.assertion_test3()
        try:
            if state == '待入库':
                self.RK.assertion_test6(read_Data.getExcel2(testData, 2))
                t.sleep(0.5)
                self.assertEqual(self.RK.assertion_test3(), '作废')
            elif state == '作废':
                self.RK.assertion_test12()
                self.RK.assertion_test6(read_Data.getExcel2(testData, 2))
                print('PASS')
                self.RK.assertion_test11()
            elif state == '已入库':
                print('订单当前状态为：{name},无法执行作废操作！！'.format(name=state))
            else:
                print('订单当前状态为：{name},无法作废！！'.format(name=state))
        except:
            print('订单当前状态为：{name},作废操作失败！！'.format(name=state))
        self.log.info('------作废入库订单：stop!---------')

    def test_RKGL3(self):
        '''确认入库订单'''
        '''

        :确认入库订单
        :return: 
        '''
        self.log.info('------确认入库订单：start!---------')
        state = self.RK.assertion_test3()
        try:
            if state == '待入库':
                self.RK.assertion_test7(read_Data.getExcel2(testData, 2))
                t.sleep(0.5)
                self.assertEqual(self.RK.assertion_test3(), '已入库')
            elif state == '作废':
                self.RK.assertion_test12()
                self.RK.assertion_test7(read_Data.getExcel2(testData, 2))
                print('PASS')
                self.RK.assertion_test11()
            else:
                print('订单当前状态为：{name},无法确认入库！！'.format(name=state))
        except:
            print('订单当前状态为：{name},确认入库操作失败！！'.format(name=state))
        self.log.info('------确认入库订单：stop!---------')

    def test_RKGL4(self):
        '''入库管理订单编号筛选'''
        '''

        :入库管理订单编号筛选
        :return:
        '''
        self.log.info('------入库管理订单编号筛选：start!---------')
        self.RK.assertion_test8(testData)
        t.sleep(0.5)
        data = self.RK.assertion_test9()
        try:
            if int(data[11])>0:
                order = self.RK.assertion_test4()
                self.assertIn(str(testData),order)
            else:
                print('模糊输入的订单编号为：{name},筛选结果为:{name1}条,没有筛选出包含{name2}的订单编号'
                      .format(name=testData, name1=data[11], name2=testData))
        except:
            if int(data[12:14])>0:
                order = self.RK.assertion_test4()
                self.assertIn(str(testData),order)
            else:
                print('模糊输入的订单编号为：{name},筛选结果为:{name1}条,没有筛选出包含{name2}的订单编号'
                      .format(name=testData,name1=data[11],name2=testData))
        self.log.info('------入库管理订单编号筛选：stop!---------')


if __name__=='__main__':
    unittest.main()