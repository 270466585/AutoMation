# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By
import time

class Rukuguanli(BasePage):

    '''
    入库管理页面定位元素
    '''

    Assertion_elm1=(By.XPATH, "//div[@id='ac']/div[2]/div[1]/div[1]")  # 仓库管理
    Assertion_elm2=(By.LINK_TEXT,u'入库管理') #入库管理
    Assertion_elm3=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/\
    div[2]/div[2]/table/tbody/tr[1]/td[2]/div')#状态文本
    Assertion_elm4=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/\
    div[2]/div[2]/table/tbody/tr[1]/td[1]/div')#订单编号文本
    Assertion_elm5=(By.XPATH,"//tr[@id='datagrid-row-r1-2-0']/td[9]/div/dt/img")#操作按钮
    Assertion_elm6=(By.XPATH,'//div[5]/div[1]/div[1]')#查看详情
    Assertion_elm7=(By.XPATH,'//div[5]/div[2]/div[1]')#作废
    Assertion_elm8=(By.XPATH,'//div[10]/div[2]/div/div/form/div[2]/span/textarea')#作废信息
    Assertion_elm9=(By.XPATH,'//div[5]/div[3]/div[1]')#确认入库
    Assertion_elm10=(By.XPATH,'//div[10]/div[2]/div/div/form/div[2]/span/textarea')#确认入库信息
    Assertion_elm11=(By.XPATH,"//input[@id='inventoryOrderId']")#订单筛选
    Assertion_elm12=(By.XPATH,"//div[@id='inventoryTb']//span[.='查询']")#查询按钮
    Assertion_elm13 = (By.LINK_TEXT, u'保存')  # 保存
    Assertion_elm14 = (By.LINK_TEXT, u'关闭')  # 关闭
    Assertion_elm15 = (By.LINK_TEXT, u'确定')  # 确定
    Assertion_elm16 = (By.LINK_TEXT, u'确认')  # 确认
    Assertion_elm17 = (By.CLASS_NAME, 'pagination-info')  # 获取记录
    Assertion_elm18=(By.XPATH,"//div[@id='inventoryTb']/div[1]/div/table/tbody/tr[2]/td[6]/span/span/a")#状态筛选下拉
    Assertion_elm19=(By.XPATH,'//div[9]/div/div[1]')#还原
    Assertion_elm20=(By.XPATH,'//div[9]/div/div[2]')#待入库
    Assertion_elm21=(By.XPATH,'//div[9]/div/div[3]')#已入库
    Assertion_elm22=(By.XPATH,'//div[9]/div/div[4]')#作废
    Assertion_elm23=(By.XPATH,'//div[9]/div/div[5]')#撤回



    def assertion_test1(self):
        self.click(self.Assertion_elm1)
    def assertion_test2(self):
        self.click(self.Assertion_elm2)
        time.sleep(1)
    def assertion_test3(self):#状态文本
        return self.driver.find_element(*self.Assertion_elm3).text
    def assertion_test4(self):#订单编号文本
        return self.driver.find_element(*self.Assertion_elm4).text
    def assertion_test5(self):#查看入库管理单详情
        self.click(self.Assertion_elm5)
        self.click(self.Assertion_elm6)
        time.sleep(0.5)
    def assertion_test6(self,data):#作废入库管理单
        self.click(self.Assertion_elm5)
        self.click(self.Assertion_elm7)
        self.send_keys(self.Assertion_elm8,data)
        time.sleep(0.5)
        self.click(self.Assertion_elm16)
        time.sleep(0.5)
        self.click(self.Assertion_elm15)
        time.sleep(0.5)
    def assertion_test7(self,data):#确认入库
        self.click(self.Assertion_elm5)
        self.click(self.Assertion_elm9)
        self.send_keys(self.Assertion_elm10,data)
        time.sleep(0.5)
        self.click(self.Assertion_elm16)
        time.sleep(0.5)
        self.click(self.Assertion_elm15)
        time.sleep(0.5)
    def assertion_test8(self,data):#入库管理订单编号筛选
        self.send_keys(self.Assertion_elm11,data)
        self.click(self.Assertion_elm12)
        time.sleep(0.5)
    def assertion_test9(self):
        return self.driver.find_element(*self.Assertion_elm17).text
    def assertion_test10(self):#关闭按钮
        self.click(self.Assertion_elm14)
    def assertion_test11(self):#筛选还原
        self.click(self.Assertion_elm18)
        self.click(self.Assertion_elm19)
        self.click(self.Assertion_elm12)
        time.sleep(0.5)
    def assertion_test12(self):#待入库筛选
        self.click(self.Assertion_elm18)
        self.click(self.Assertion_elm20)
        self.click(self.Assertion_elm12)
        time.sleep(0.5)
    def assertion_test13(self):#已入库筛选
        self.click(self.Assertion_elm18)
        self.click(self.Assertion_elm21)
        self.click(self.Assertion_elm12)
        time.sleep(0.5)
    def assertion_test14(self):#作废筛选
        self.click(self.Assertion_elm18)
        self.click(self.Assertion_elm22)
        self.click(self.Assertion_elm12)
        time.sleep(0.5)
    def assertion_test15(self):#撤回筛选
        self.click(self.Assertion_elm18)
        self.click(self.Assertion_elm23)
        self.click(self.Assertion_elm12)
        time.sleep(0.5)
