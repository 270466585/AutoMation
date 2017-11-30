# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By
import time

class Yonghu(BasePage):

    '''
    用户管理页面定位元素
    '''

    Assertion_elm1=(By.XPATH, "//div[@id='ac']/div[1]/div[1]/div[1]")  # 系统设置
    Assertion_elm2 = (By.LINK_TEXT, u'用户管理')  # 用户管理
    Assertion_elm3=(By.XPATH,'//div[2]/div[3]/div/div/\
    div[2]/div[2]/div/div/div[1]/div[2]/div[1]/a/span/span[1]')#创建用户
    Assertion_elm4=(By.XPATH,'//div[4]/div[2]/div[2]/div/form/div[1]/span/input[1]')#账号
    Assertion_elm5=(By.XPATH,'//div[4]/div[2]/div[2]/div/form/div[2]/span/input[1]')#用户名
    Assertion_elm6=(By.XPATH,"//form[@id='addUserForm']/div[3]/span/span/a")#下拉按钮
    Assertion_elm7=(By.XPATH,'//div[7]/div/div[1]')#下拉选项
    Assertion_elm8 = (By.LINK_TEXT, u'保存')  # 保存
    Assertion_elm9 = (By.LINK_TEXT, u'关闭')  # 关闭
    # Assertion_elm9 = (By.LINK_TEXT, u'取消')  # 取消
    Assertion_elm10 = (By.LINK_TEXT, u'确定')  # 确定
    Assertion_elm11=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/\
    div[2]/div[2]/div[2]/table/tbody/tr[2]/td[5]/div/dt/img')#操作按钮
    Assertion_elm12=(By.XPATH,"//div[@id='userMenu']/div[1]/div[1]")#查看按钮
    Assertion_elm13=(By.XPATH,'//div[5]/div[1]/div[1]')#用户详细Title
    Assertion_elm14=(By.XPATH,'//div[3]/div[2]/div[1]')#编辑用户
    Assertion_elm15=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[2]/span/input[1]')#用户名称
    Assertion_elm16=(By.XPATH,'//div[8]/div/div[2]')#下拉选项
    Assertion_elm17=(By.XPATH,'//div[3]/div[3]/div[1]')#重置密码
    Assertion_elm18=(By.XPATH,'//div[3]/div[4]/div[1]')#用户冻结
    Assertion_elm19=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/\
    div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]/div')#状态
    Assertion_elm20 = (By.CLASS_NAME, 'pagination-info')  # 获取记录
    Assertion_elm21=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/\
    div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]/div')#用户名文本
    Assertion_elm22=(By.XPATH,"//form[@id='editUserForm']/div[3]/span/span/a")#下拉按钮

    def assertion_test1(self):
        self.click(self.Assertion_elm1)
    def assertion_test2(self):
        self.click(self.Assertion_elm2)
    def assertion_test3(self):#获取记录
        return self.driver.find_element(*self.Assertion_elm20).text
    def assertion_test4(self,data1,data2):#创建用户
        self.click(self.Assertion_elm3)
        self.send_keys(self.Assertion_elm4, data1)
        self.send_keys(self.Assertion_elm5, data2)
        self.click(self.Assertion_elm6)
        self.click(self.Assertion_elm7)
        time.sleep(0.5)
        self.click(self.Assertion_elm8)
        time.sleep(0.5)
        self.click(self.Assertion_elm10)
        time.sleep(0.5)
    def assertion_test5(self):#用户详情
        self.click(self.Assertion_elm11)
        self.click(self.Assertion_elm12)
        time.sleep(0.5)
    def assertion_test10(self):  # 关闭详情
        self.click(self.Assertion_elm9)
    def assertion_test6(self):#用户详细title
        return self.driver.find_element(*self.Assertion_elm13).text
    def assertion_test7(self,data1):#编辑用户
        self.click(self.Assertion_elm11)
        self.click(self.Assertion_elm14)
        self.send_keys(self.Assertion_elm15, data1)
        self.click(self.Assertion_elm22)
        self.click(self.Assertion_elm16)
        time.sleep(0.5)
        self.click(self.Assertion_elm8)
        time.sleep(0.5)
        self.click(self.Assertion_elm10)
        time.sleep(0.5)
    def assertion_test8(self):#重置密码
        self.click(self.Assertion_elm11)
        self.click(self.Assertion_elm17)
        time.sleep(0.5)
        self.click(self.Assertion_elm10)
        time.sleep(0.5)
        self.click(self.Assertion_elm10)
        time.sleep(0.5)
    def assertion_test9(self):#冻结用户
        self.click(self.Assertion_elm11)
        self.click(self.Assertion_elm18)
        time.sleep(0.5)
        self.click(self.Assertion_elm10)
        time.sleep(0.5)
        self.click(self.Assertion_elm10)
        time.sleep(0.5)
    def assertion_test11(self):#用户名文本
        return self.driver.find_element(*self.Assertion_elm21).text
    def assertion_test12(self):#状态文本
        return self.driver.find_element(*self.Assertion_elm19).text