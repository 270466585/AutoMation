import unittest
from Base_page.DriverPage import browser
from Base_page.Warehouse_managementPage.ChukuPage import Chukuguanli
from common import read_Data
from common.logger import Log
from common import Global_function
from common.Global_function import login_url
from random import randint
import time as t

testData=randint(1,50)
testData1=randint(1,50)
testData2='3D01170400'+str(randint(100,999))



class ChuKU(unittest.TestCase):
    log = Log()
    @classmethod
    def setUpClass(cls):
        cls.driver =browser()
        cls.CK = Chukuguanli(cls.driver)
        cls.CK.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)
        cls.CK.assertion_test1()
        cls.CK.assertion_test2()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_CKGL1(self):
        '''出库管理清单管理'''
        '''

        :出库管理清单管理
        :return:
        '''
        self.log.info('------出库管理清单管理：start!---------')
       # self.CK.assertion_test18()
        state = self.CK.assertion_test4()
        self.CK.assertion_test14()
        data = self.CK.assertion_test16()
        try:
            data = int(data[11]) + 1
        except:
            data=int(data[12:14])+1
        try:
            if state == '待出库' or '缺货' or '待发货':
                self.CK.assertion_test15(testData2)
            else:
                print('订单当前状态为：{name},无法添加清单管理！！'.format(name=state))
        except:
            print('订单当前状态为：{name},添加清单操作失败！！'.format(name=state))
        Data = self.CK.assertion_test16()
        try:
            Data=int(Data[11])
            self.assertEqual(data, Data)
        except:
            Data=int(Data[12:14])
            self.assertEqual(Data, data)
        self.CK.assertion_test8()
        self.log.info('------出库管理清单管理：stop!---------')

    def test_CKGL2(self):
        '''查看出库管理单详情'''
        '''

        :查看出库管理单详情
        :return: 
        '''
        self.log.info('------查看出库管理单详情：start!---------')
        self.CK.assertion_test7()
        t.sleep(0.5)
        self.CK.assertion_test8()
        #self.CK.assertion_test23()
        self.log.info('------查看出库管理单详情：stop!---------')

    def test_CKGL3(self):
        '''出库管理单缺货'''
        '''

        :出库管理单缺货
        :return: 
        '''
        self.log.info('------出库管理单缺货：start!---------')
        state = self.CK.assertion_test4()
        try:
            if state =='待出库':
                self.CK.assertion_test9(read_Data.getExcel2(testData, 2))
                t.sleep(0.5)
                self.assertEqual(self.CK.assertion_test4(), '缺货')
            elif state == '缺货':
                self.CK.assertion_test17()
                self.CK.assertion_test9(read_Data.getExcel2(testData, 2))
                t.sleep(0.5)
                self.assertEqual(self.CK.assertion_test4(), '缺货')
            # elif state == '入库取消':
            #     print('订单当前状态为：{name}'.format(name=state))
            else:
                print('订单当前状态为：{name},无法进行缺货操作！！'.format(name=state))
        except:
            print('订单当前状态为：{name},缺货操作失败！！'.format(name=state))
        self.log.info('------出库管理单缺货：stop!---------')

    def test_CKGL4(self):
        '''出库管理单开始发货'''
        '''

        :出库管理单开始发货
        :return: 
        '''
        self.log.info('------出库管理单开始发货：start!---------')
        #self.CK.assertion_test19()
        state = self.CK.assertion_test4()
        try:
            if state =='待出库':
                self.CK.assertion_test9(read_Data.getExcel2(testData, 2))
                t.sleep(0.5)
                self.CK.assertion_test17()
                self.assertEqual(self.CK.assertion_test4(), '待出库')
            elif state == '缺货':
                self.CK.assertion_test17()
                t.sleep(0.5)
                self.assertEqual(self.CK.assertion_test4(), '待出库')
            # elif state == '入库取消':
            #     print('订单当前状态为：{name}'.format(name=state))
            else:
                print('订单当前状态为：{name},无法进行开始发货操作！！'.format(name=state))
        except:
            print('订单当前状态为：{name},开始发货操作失败！！'.format(name=state))
        self.log.info('------出库管理单开始发货：stop!---------')

    def test_CKGL5(self):
        '''出库管理单完成备货'''
        '''

        :出库管理单完成备货
        :return: 
        '''
        self.log.info('------出库管理单完成备货：start!---------')
        #self.CK.assertion_test18()
        state = self.CK.assertion_test4()
        try:
            if state =='待出库':
                self.CK.assertion_test10()
                t.sleep(0.5)
                self.assertEqual(self.CK.assertion_test4(), '待发货')
            elif state == '缺货':
                self.CK.assertion_test17()
                t.sleep(0.5)
                self.CK.assertion_test10()
                self.assertEqual(self.CK.assertion_test4(), '待发货')
            elif state == '待发货':
                print('订单当前状态已经为：{name},无需再次进行完成备货操作！！'.format(name=state))
            else:
                print('订单当前状态为：{name},无法进行完成备货操作！！'.format(name=state))
        except:
            print('订单当前状态为：{name},完成备货操作失败！！'.format(name=state))
        self.log.info('------出库管理单完成备货：stop!---------')

    def test_CKGL6(self):
        '''出库管理单重新发货'''
        '''

        :出库管理单重新发货
        :return: 
        '''
        self.log.info('------出库管理单重新发货：start!---------')
        #self.CK.assertion_test20()
        state = self.CK.assertion_test4()
        try:
            if state =='待出库':
                self.CK.assertion_test10()
                t.sleep(0.5)
                self.CK.assertion_test11()
                self.assertEqual(self.CK.assertion_test4(), '待出库')
            elif state == '待发货':
                self.CK.assertion_test11()
                t.sleep(0.5)
                self.assertEqual(self.CK.assertion_test4(), '待出库')
            # elif state == '待发货':
            #     print('订单当前状态已经为：{name},无需再次进行完成备货操作！！'.format(name=state))
            else:
                print('订单当前状态为：{name},无法进行重新发货操作！！'.format(name=state))
        except:
            print('订单当前状态为：{name},重新发货操作失败！！'.format(name=state))
        self.log.info('------出库管理单重新发货：stop!---------')

    def test_CKGL7(self):
        '''出库管理单物流信息'''
        '''

        :出库管理单物流信息
        :return: 
        '''
        self.log.info('------出库管理单物流信息：start!---------')
        #self.CK.assertion_test20()
        state = self.CK.assertion_test4()
        try:
            if state =='待出库':
                self.CK.assertion_test10()
                t.sleep(0.5)
                self.CK.assertion_test13()
                self.assertEqual(self.CK.assertion_test4(), '待发货')
            elif state == '待发货':
                self.CK.assertion_test13()
                t.sleep(0.5)
                self.assertEqual(self.CK.assertion_test4(), '待发货')
            # elif state == '待发货':
            #     print('订单当前状态已经为：{name},无需再次进行完成备货操作！！'.format(name=state))
            else:
                print('订单当前状态为：{name},无法添加物流信息操作！！'.format(name=state))
        except:
            print('订单当前状态为：{name},物流信息添加失败！！'.format(name=state))
        self.log.info('------出库管理单物流信息：stop!---------')

    def test_CKGL8(self):
        '''出库管理单发货离库'''
        '''

        :出库管理单发货离库
        :return: 
        '''
        self.log.info('------出库管理单发货离库：start!---------')
        #self.CK.assertion_test20()
        state = self.CK.assertion_test4()
        try:
            if state =='待出库':
                self.CK.assertion_test10()
                t.sleep(0.5)
                self.CK.assertion_test12(read_Data.getExcel2(testData,2))
                self.assertEqual(self.CK.assertion_test4(), '已出库')
            elif state == '待发货':
                self.CK.assertion_test12(read_Data.getExcel2(testData, 2))
                t.sleep(0.5)
                self.assertEqual(self.CK.assertion_test4(), '已出库')
            # elif state == '待发货':
            #     print('订单当前状态已经为：{name},无需再次进行完成备货操作！！'.format(name=state))
            else:
                print('订单当前状态为：{name},无法进行发货离库操作！！'.format(name=state))
        except BaseException as msg:
            print('订单当前状态为：{name},发货离库操作失败！！'.format(name=state),msg)
        #self.CK.assertion_test23()
        self.log.info('------出库管理单发货离库：stop!---------')

    def test_CKGL9(self):
        '''出库管理出库批次筛选'''
        '''

        :出库管理出库批次筛选
        :return:
        '''
        self.log.info('------出库管理出库批次筛选：start!---------')
        self.CK.assertion_test6(testData)
        t.sleep(1)
        data = self.CK.assertion_test5()
        order = self.CK.assertion_test3()
        try:
            if int(data[11])>0:
                self.assertIn(str(testData),order)
            else:
                print('模糊输入的出库批次为：{name},筛选结果为:{name1}条,没有筛选出包含{name2}的出库批次'
                      .format(name=testData, name1=data[11], name2=testData))
        except:
            if int(data[12:14])>0:
                self.assertIn(str(testData),order)
            else:
                print('模糊输入的出库批次为：{name},筛选结果为:{name1}条,没有筛选出包含{name2}的出库批次'
                      .format(name=testData,name1=data[11],name2=testData))
        t.sleep(2)

        self.log.info('------出库管理出库批次筛选：stop!---------')





if __name__=='__main__':
    unittest.main()