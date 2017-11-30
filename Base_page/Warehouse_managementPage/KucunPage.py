# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By
import time

class Kucunguanli(BasePage):

    '''
    库存管理页面定位元素
    '''

    Assertion_elm1=(By.XPATH, "//div[@id='ac']/div[2]/div[1]/div[1]")  # 仓库管理
    Assertion_elm2=(By.LINK_TEXT,u'库存管理') #库存管理
    Assertion_elm3=(By.XPATH,"//div[@id='stockTb']/div[1]/div/table/tbody/tr[1]/td[3]/span/span/a")#sku筛选下拉按钮
    Assertion_elm4=(By.XPATH,'//div[3]/div/div[4]')#下拉选项
    Assertion_elm5=(By.XPATH,"//div[@id='stockTb']/div[1]/div/table/tbody/tr[1]/td[5]/span/span/a")#仓库筛选下拉按钮
    Assertion_elm6=(By.XPATH,'//div[4]/div/div[3]')#下拉选项
    Assertion_elm7=(By.XPATH,"//div[@id='stockTb']//span[.='查询']")#查询按钮
    Assertion_elm8 = (By.CLASS_NAME, 'pagination-info')  # 获取记录
    Assertion_elm9=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/\
    div[2]/div[2]/div[2]/table/tbody/tr/td[1]/div')#sku文本
    Assertion_elm10=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/\
    div[2]/div[2]/div[2]/table/tbody/tr/td[7]/div')#仓库文本

    def assertion_test1(self):
        self.click(self.Assertion_elm1)

    def assertion_test2(self):
        self.click(self.Assertion_elm2)
        time.sleep(1)

    def assertion_test3(self):  #获取记录文本
        return self.driver.find_element(*self.Assertion_elm8).text

    def assertion_test4(self):#SKU筛选
        self.click(self.Assertion_elm3)
        self.click(self.Assertion_elm4)
        self.click(self.Assertion_elm7)
        time.sleep(0.5)

    def assertion_test5(self):#仓库筛选
        self.click(self.Assertion_elm5)
        self.click(self.Assertion_elm6)
        self.click(self.Assertion_elm7)
        time.sleep(0.5)

    def assertion_test6(self):  #SKU文本
        return self.driver.find_element(*self.Assertion_elm9).text

    def assertion_test7(self):  #仓库文本
        return self.driver.find_element(*self.Assertion_elm10).text

