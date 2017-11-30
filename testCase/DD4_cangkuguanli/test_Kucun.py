import unittest
from Base_page.DriverPage import browser
from Base_page.Warehouse_managementPage.KucunPage import Kucunguanli
from common.logger import Log
from common import Global_function
from common.Global_function import login_url
import time as t




class KuCun(unittest.TestCase):
    log = Log()
    @classmethod
    def setUpClass(cls):
        cls.driver =browser()
        cls.KC = Kucunguanli(cls.driver)
        cls.KC.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)
        cls.KC.assertion_test1()
        cls.KC.assertion_test2()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_KCGL1(self):
        '''库存管理SKU筛选'''
        '''

        :库存管理SKU筛选
        :return:
        '''
        self.log.info('------库存管理SKU筛选：start!---------')
        self.KC.assertion_test4()
        t.sleep(1)
        data = self.KC.assertion_test3()
        SKU = self.KC.assertion_test6()
        try:
            if int(data[11])>0:
                self.assertEqual(SKU,'3D88')
            else:
                print('没有筛选到名为：{name} 的SKU！！'.format(name=SKU))
        except:
            if int(data[12:14])>0:
                self.assertEqual(SKU, '3D88')
            else:
                print('没有筛选到名为：{name} 的SKU！！'.format(name=SKU))

        self.log.info('------库存管理SKU筛选：stop!---------')

    def test_KCGL2(self):
        '''库存管理仓库筛选'''
        '''

        :库存管理仓库筛选
        :return:
        '''
        self.log.info('------库存管理仓库筛选：start!---------')
        self.KC.assertion_test5()
        t.sleep(1)
        data = self.KC.assertion_test3()
        Warehouse = self.KC.assertion_test7()
        try:
            if int(data[11])>0:
                self.assertEqual(Warehouse,'天府新谷退换库')
            else:
                print('没有筛选到名为：{name} 的仓库！！'.format(name=Warehouse))
        except:
            if int(data[12:14])>0:
                self.assertEqual(Warehouse, '天府新谷退换库')
            else:
                print('没有筛选到名为：{name} 的仓库！！'.format(name=Warehouse))

        self.log.info('------库存管理仓库筛选：stop!---------')


if __name__=='__main__':
    unittest.main()