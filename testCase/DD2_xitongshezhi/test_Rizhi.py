# coding:utf-8

import unittest
from Base_page.DriverPage import browser
from Base_page.System_settingsPage.RizhiPage import Rizhi
from common import read_Data
from common.logger import Log
from common import Global_function
from common.Global_function import login_url
from random import randint
import time as t
testData=randint(1,50)
testData1=randint(1,50)


class RiZhi(unittest.TestCase):
    log = Log()

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.RZ = Rizhi(cls.driver)
        cls.RZ.open(login_url, u'登录')
        cls.driver.implicitly_wait(5)
        Global_function.login(cls)
        t.sleep(0.5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_CZRZ1(self):
        '''操作日志'''
        '''

        :操作日志
        :return: 
        '''
        self.log.info('------操作日志：start!---------')
        self.RZ.assertion_test1()
        self.RZ.assertion_test2()
        self.assertEqual(self.RZ.assertion_test3(),read_Data.getExcel2(10,6))
        self.log.info('------操作日志：stop!---------')


if __name__=='__main__':
    unittest.main()