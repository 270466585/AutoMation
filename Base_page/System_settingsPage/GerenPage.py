# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By
import time


class Geren(BasePage):

    '''
    个人信息页面定位元素
    '''

    Assertion_elm1=(By.XPATH, "//div[@id='ac']/div[1]/div[1]/div[1]")  # 系统设置
    Assertion_elm2 = (By.LINK_TEXT, u'个人信息')  # 个人信息
    Assertion_elm3=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/\
    div[2]/div/div/div/div[2]/span/input[1]')#用户名称
    Assertion_elm4=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/\
    div[2]/div/div/div/div[2]/a/span/span[1]')#确认修改
    Assertion_elm5 = (By.LINK_TEXT, u'保存')  # 保存
    Assertion_elm6 = (By.LINK_TEXT, u'关闭')  # 关闭
    # Assertion_elm6 = (By.LINK_TEXT, u'取消')  # 取消
    Assertion_elm7 = (By.LINK_TEXT, u'确定')  # 确定
    Assertion_elm8=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/\
    div[2]/div/div/div/div[3]/a/span/span[1]')#修改密码
    Assertion_elm9=(By.XPATH,'//div[3]/div[2]/div[2]/div/form/div[1]/span/input[1]')#原密码
    Assertion_elm10=(By.XPATH,'//div[3]/div[2]/div[2]/div/form/div[2]/span/input[1]')#新密码
    Assertion_elm11=(By.XPATH,'//div[3]/div[2]/div[2]/div/form/div[3]/span/input[1]')#重复新密码
    Assertion_elm12 = (By.ID, 'loginname')  # 用户名
    Assertion_elm13=(By.XPATH,'//div[3]/div[2]/div[2]/div/form/div[1]/span/span/a')#显示原密码

    def assertion_test1(self):
        self.click(self.Assertion_elm1)
    def assertion_test2(self):
        self.click(self.Assertion_elm2)
    def assertion_test3(self,data):#修改用户名称
        self.send_keys(self.Assertion_elm3,data)
        self.click(self.Assertion_elm4)
        time.sleep(0.5)
        self.click(self.Assertion_elm7)
        time.sleep(0.5)
    def assertion_test4(self,data1,data2,data3):#修改密码
        self.click(self.Assertion_elm8)
        self.click(self.Assertion_elm13)
        time.sleep(0.5)
        self.send_keys(self.Assertion_elm9, data1)
        time.sleep(0.5)
        self.send_keys(self.Assertion_elm10, data2)
        time.sleep(0.5)
        self.send_keys(self.Assertion_elm11, data3)
        time.sleep(0.5)
        self.click(self.Assertion_elm5)
        time.sleep(0.5)
        self.click(self.Assertion_elm7)
        time.sleep(0.5)
    def assertion_test5(self):
        return self.driver.find_element(*self.Assertion_elm12).text
