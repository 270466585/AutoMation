# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By
import time

class Juese(BasePage):

    '''
    角色管理页面定位元素
    '''

    Assertion_elm1=(By.XPATH, "//div[@id='ac']/div[1]/div[1]/div[1]")  # 系统设置
    Assertion_elm2 = (By.LINK_TEXT, u'角色管理')  # 角色管理
    Assertion_elm3=(By.CSS_SELECTOR,'span.l-btn-text')#创建角色
    Assertion_elm4=(By.XPATH,'//div[4]/div[2]/div[2]/div/form/div[1]/span/input[1]')#角色名称
    Assertion_elm5=(By.XPATH,'//div[4]/div[2]/div[2]/div/form/div[2]/span/textarea')#角色描述
    Assertion_elm6 = (By.LINK_TEXT, u'保存')  # 保存
    Assertion_elm7 = (By.LINK_TEXT, u'关闭')  # 关闭
    #Assertion_elm7 = (By.LINK_TEXT, u'取消')  # 取消
    Assertion_elm8= (By.LINK_TEXT, u'确定')  # 确定
    Assertion_elm9 = (By.CLASS_NAME, 'pagination-info')  # 获取记录
    Assertion_elm10=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/\
    div[2]/div[2]/div[2]/table/tbody/tr[2]/td[3]/div/dt/img')#操作按钮
    Assertion_elm11=(By.XPATH,".//*[@id='roleMenu']/div[1]")#查看按钮
    Assertion_elm12=(By.XPATH,'//div[5]/div[1]/div[1]')# 详情title
    Assertion_elm13=(By.XPATH,".//*[@id='roleMenu']/div[2]")#编辑按钮
    Assertion_elm14=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[1]/span/input[1]')#编辑名称
    Assertion_elm15=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[2]/span/textarea')#编辑描述
    Assertion_elm16=(By.XPATH,".//*[@id='roleMenu']/div[3]")#编辑权限
    Assertion_elm17=(By.CLASS_NAME,'moduleitem')#name 多选框
    Assertion_elm18=(By.XPATH,".//*[@type='checkbox']")# type 多选框
    Assertion_elm19=(By.XPATH,".//*[@id='roleMenu']/div[4]")#删除按钮
    Assertion_elm20=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/\
    div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]/div')#角色名称文本


    def assertion_test1(self):
        self.click(self.Assertion_elm1)
    def assertion_test2(self):
        self.click(self.Assertion_elm2)
    def assertion_test3(self):
        return self.driver.find_element(*self.Assertion_elm9).text
    def assertion_test4(self,data1,data2):#创建
        self.click(self.Assertion_elm3)
        self.send_keys(self.Assertion_elm4, data1)
        self.send_keys(self.Assertion_elm5, data2)
        time.sleep(0.5)
        self.click(self.Assertion_elm6)
        time.sleep(0.5)
        self.click(self.Assertion_elm8)
        time.sleep(0.5)
    def assertion_test5(self):#查看详情
        self.click(self.Assertion_elm10)
        self.click(self.Assertion_elm11)
        time.sleep(0.5)
    def assertion_test6(self):#详情title
        return self.driver.find_element(*self.Assertion_elm12).text
    def assertion_test11(self):  # 关闭详情
        self.click(self.Assertion_elm7)
    def assertion_test7(self,data1,data2):#编辑角色
        self.click(self.Assertion_elm10)
        self.click(self.Assertion_elm13)
        self.send_keys(self.Assertion_elm14, data1)
        self.send_keys(self.Assertion_elm15, data2)
        time.sleep(0.5)
        self.click(self.Assertion_elm6)
        time.sleep(0.5)
        self.click(self.Assertion_elm8)
        time.sleep(0.5)
    def assertion_test8(self):#角色名称文本
        return self.driver.find_element(*self.Assertion_elm20).text
    def assertion_test9(self):#编辑权限
        self.click(self.Assertion_elm10)
        self.click(self.Assertion_elm16)
        # data=self.driver.find_elements(*self.Assertion_elm18)
        # for data1 in data:
        #     if data1==data[10]:
        #         time.sleep(0.8)
        self.click(self.Assertion_elm18)
        time.sleep(0.5)
        self.click(self.Assertion_elm6)
        time.sleep(0.5)
        self.click(self.Assertion_elm8)
        time.sleep(0.5)
    def assertion_test10(self):  # 删除角色
        self.click(self.Assertion_elm10)
        self.click(self.Assertion_elm19)
        time.sleep(0.5)
        self.click(self.Assertion_elm8)
        time.sleep(0.5)
        self.click(self.Assertion_elm8)
        time.sleep(0.5)