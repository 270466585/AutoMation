# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By
import time


class Mokuai(BasePage):

    '''
    模块管理页面定位元素
    '''

    Assertion_elm1=(By.XPATH, "//div[@id='ac']/div[1]/div[1]/div[1]")  # 系统设置
    Assertion_elm2 = (By.LINK_TEXT, u'模块管理')  # 模块管理
    Assertion_elm3=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/\
    div[2]/div/div/div[1]/div[2]/div[1]/a/span/span[1]')# 创建模块
    Assertion_elm4=(By.XPATH,'//div[4]/div[2]/div[2]/div/form/div[1]/span/input[1]')#模块名称
    Assertion_elm5=(By.XPATH,"//form[@id='addModuleForm']/div[2]/span/span/a")#下拉按钮
    Assertion_elm6=(By.XPATH,"//div[7]/div/div[1]")#下拉选项
    Assertion_elm7=(By.CLASS_NAME,'combobox-item')#下拉选项数组
    Assertion_elm8=(By.XPATH,"//div[4]/div[2]/div[2]/div/form/div[3]/span/input[1]")#URL
    Assertion_elm9 = (By.LINK_TEXT, u'保存')  # 保存
    Assertion_elm10 = (By.LINK_TEXT, u'关闭')  # 关闭
    #Assertion_elm10 = (By.LINK_TEXT, u'取消')  # 取消
    Assertion_elm11= (By.LINK_TEXT, u'确定')  # 确定
    Assertion_elm12 = (By.CLASS_NAME, 'pagination-info')  # 获取记录
    Assertion_elm13=(By.XPATH,"//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/\
    div[2]/div[2]/div[2]/div[2]/table/tbody/tr[8]/td[4]/div/dt/img")#操作按钮
    Assertion_elm14=(By.XPATH,"//div[@id='moduleMenu']/div[1]/div[1]")#查看按钮
    Assertion_elm15=(By.XPATH,'//div[5]/div[1]/div[1]')#查看文本
    Assertion_elm16=(By.XPATH,"//div[@id='moduleMenu']/div[2]/div[1]")#编辑按钮
    Assertion_elm17=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[1]/span/input[1]')#编辑模块名称
    Assertion_elm18=(By.XPATH,"//form[@id='editModuleForm']/div[2]/span/span/a")#下拉按钮
    Assertion_elm19=(By.XPATH,'//div[8]/div/div[1]')#下拉选项
    Assertion_elm20=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[3]/span/input[1]')#URL
    Assertion_elm21 = (By.XPATH,"//div[@id='moduleMenu']/div[3]/div[1]")  # 删除按钮
    Assertion_elm22 = (By.XPATH,"//div[@id='moduleMenu']/div[4]/div[1]")  # 上移按钮
    Assertion_elm23 = (By.XPATH,"//div[@id='moduleMenu']/div[5]/div[1]")  # 下移按钮
    Assertion_elm24 = (By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/\
    div[2]/div[2]/table/tbody/tr[8]/td[1]/div')#模块名称文本
    Assertion_elm25 = (By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/\
    table/tbody/tr/td[10]/a/span/span[2]')#翻页
    Assertion_elm26=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/\
    div[2]/div[2]/table/tbody/tr[2]/td[4]/div/dt/img')#模块
    Assertion_elm27 = (By.XPATH, '//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/\
    div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[4]/div/dt/img')  # 角色

    def assertion_test1(self):
        self.click(self.Assertion_elm1)
    def assertion_test2(self):
        self.click(self.Assertion_elm2)
    def assertion_test3(self):#记录
        return self.driver.find_element(*self.Assertion_elm12).text
    def assertion_test4(self,data,url):#创建
        self.click(self.Assertion_elm3)
        self.send_keys(self.Assertion_elm4, data)
        self.click(self.Assertion_elm5)
        self.click(self.Assertion_elm6)
        self.send_keys(self.Assertion_elm8, url)
        time.sleep(0.5)
        self.click(self.Assertion_elm9)
        time.sleep(0.5)
        self.click(self.Assertion_elm11)
        time.sleep(0.5)
    def assertion_test5(self):#查看
        self.click(self.Assertion_elm13)
        self.click(self.Assertion_elm14)
        time.sleep(0.5)
    def assertion_test6(self):#详情
        return self.driver.find_element(*self.Assertion_elm15).text
    def assertion_test7(self):#关闭按钮
        self.click(self.Assertion_elm10)
    def assertion_test8(self,data,url):#编辑
        self.click(self.Assertion_elm13)
        self.click(self.Assertion_elm16)
        self.send_keys(self.Assertion_elm17, data)
        self.click(self.Assertion_elm18)
        self.click(self.Assertion_elm19)
        self.send_keys(self.Assertion_elm20,url)
        time.sleep(0.5)
        self.click(self.Assertion_elm9)
        time.sleep(0.5)
        self.click(self.Assertion_elm11)
        time.sleep(0.5)
    def assertion_test9(self):#模块名称
        return self.driver.find_element(*self.Assertion_elm24).text
    def assertion_test10(self):#删除
        #self.click(self.Assertion_elm25)
        self.click(self.Assertion_elm13)
        self.click(self.Assertion_elm21)
        time.sleep(0.5)
        self.click(self.Assertion_elm11)
        time.sleep(0.5)
        self.click(self.Assertion_elm11)
        time.sleep(0.5)
    def assertion_test11(self,data,url):#创建
        self.click(self.Assertion_elm3)
        self.send_keys(self.Assertion_elm17, data)
        self.click(self.Assertion_elm5)
        self.click(self.Assertion_elm19)
        self.send_keys(self.Assertion_elm20, url)
        time.sleep(0.5)
        self.click(self.Assertion_elm9)
        time.sleep(0.5)
        self.click(self.Assertion_elm11)
        time.sleep(0.5)
    def assertion_test12(self):#上移
        self.click(self.Assertion_elm27)
        self.click(self.Assertion_elm22)
        time.sleep(0.5)
        self.click(self.Assertion_elm11)
        time.sleep(0.5)
    def assertion_test13(self):#下移
        self.click(self.Assertion_elm26)
        self.click(self.Assertion_elm23)
        time.sleep(0.5)
        self.click(self.Assertion_elm11)
        time.sleep(0.5)




