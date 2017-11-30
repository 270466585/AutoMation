# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By
import time


class Caidanguanli(BasePage):

    '''
    菜单管理页面定位元素
    '''

    Assertion_elm1=(By.XPATH, "//div[@id='ac']/div[1]/div[1]/div[1]")  # 系统设置
    Assertion_elm2=(By.LINK_TEXT,u'菜单管理') #菜单管理
    Assertion_elm3=(By.CLASS_NAME,'tabs-title'[1])#菜单管理文本
    Assertion_elm4=(By.XPATH,"//div[@id='menuTb']//span[.='创建新的菜单']")#创建菜单
    Assertion_elm5=(By.XPATH,'//div[4]/div[2]/div[2]/div/form/div/span/input[1]')#输入菜单名称
    Assertion_elm6=(By.LINK_TEXT,u'保存')#保存
    Assertion_elm7=(By.LINK_TEXT,u'关闭')#关闭
    Assertion_elm8=(By.LINK_TEXT,u'确定')#确定
    Assertion_elm9=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/\
    div[2]/div[2]/table/tbody/tr[4]/td[3]/div/dt/img')#点击操作按钮
    Assertion_elm10=(By.XPATH,"//div[@id='menuMenu']/div[1]/div[1]")#编辑
    Assertion_elm11=(By.XPATH,'//div[3]/div[2]/div[1]')#删除
    Assertion_elm12=(By.XPATH,'//div[3]/div[3]/div[1]')#上移动
    Assertion_elm16 = (By.XPATH, '//div[3]/div[4]/div[1]')#下移动
    Assertion_elm13=(By.CLASS_NAME,'pagination-info')#获取记录
    Assertion_elm14=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div/span/input[1]')#编辑内容
    Assertion_elm15=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/\
    div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[1]/div')#获取文本
    Assertion_elm17=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/\
    div[2]/div[2]/table/tbody/tr[1]/td[3]/div/dt/img')#下移操作按钮
    Assertion_elm18=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/\
    div[2]/div[2]/table/tbody/tr[2]/td[3]/div/dt/img')#上移操作按钮
    Assertion_elm19=(By.XPATH,'//div[3]/div[3]/div[1]')#下移或上移


    def assertion_test1(self):
        self.click(self.Assertion_elm1)
    def assertion_test2(self):
        self.click(self.Assertion_elm2)
    def assertion_test3(self):
        return self.driver.find_element(*self.Assertion_elm3).text
    def assertion_test4(self):
        self.click(self.Assertion_elm4)
    def assertion_test5(self,data):
        self.send_keys(self.Assertion_elm5,data)
    def assertion_test6(self):
        self.click(self.Assertion_elm6)
    def assertion_test7(self):
        time.sleep(0.5)
        self.click(self.Assertion_elm7)
    def assertion_test8(self):
        time.sleep(0.5)
        self.click(self.Assertion_elm8)
    def assertion_test9(self):
        return self.driver.find_element(*self.Assertion_elm13).text
    def assertion_test10(self):
        self.click(self.Assertion_elm9)
    def assertion_test11(self):
        self.click(self.Assertion_elm10)
    def assertion_test12(self):
        self.click(self.Assertion_elm11)
    def assertion_test13(self):
        self.click(self.Assertion_elm12)
    def assertion_test14(self,data):
        self.send_keys(self.Assertion_elm14,data)
    def assertion_test15(self):
        return self.driver.find_element(*self.Assertion_elm15).text
    def assertion_test16(self):
        self.click(self.Assertion_elm16)
    def assertion_test17(self):#下移
        self.click(self.Assertion_elm17)
        self.click(self.Assertion_elm19)
        self.click(self.Assertion_elm8)
    def assertion_test18(self):#上移
        self.click(self.Assertion_elm18)
        self.click(self.Assertion_elm19)
        self.click(self.Assertion_elm8)

