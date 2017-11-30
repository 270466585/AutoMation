# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By
import time


class Rizhi(BasePage):

    '''
    操作日志页面定位元素
    '''

    Assertion_elm1=(By.XPATH, "//div[@id='ac']/div[1]/div[1]/div[1]")  # 系统设置
    Assertion_elm2 = (By.LINK_TEXT, u'操作日志')  # 操作日志
    Assertion_elm3=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/\
    div[2]/div/div/div[1]/div[1]/div[1]')#title


    def assertion_test1(self):
        self.click(self.Assertion_elm1)
    def assertion_test2(self):
        self.click(self.Assertion_elm2)
    def assertion_test3(self):
        return self.driver.find_element(*self.Assertion_elm3).text
