# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By



class Loginpage(BasePage):

    '''
    登录页面的定位元素
    '''
    username_loc = (By.ID, '_easyui_textbox_input1')  # 输入账号
    password_loc = (By.ID, '_easyui_textbox_input2')  # 输入密码
    submit_loc = (By.CLASS_NAME, 'l-btn-text')  # 提交登录
    Assertion_text1 = (By.XPATH, 'html/body/div[3]/div[1]')  # 账号密码为空
    Assertion_text2 = (By.XPATH, 'html/body/div[3]/div[1]')  # 账号为空，密码正确
    Assertion_text3 = (By.CLASS_NAME, 'tooltip-content')  # 账号正确，密码为空
    Assertion_text4 = (By.XPATH, 'html/body/div[3]/div[2]/div[2]')  # 账号正确，密码错误
    Assertion_text6 = (By.ID, 'loginname')  # 验证登陆后，用户名
    Assertion_text8 = (By.LINK_TEXT,'确定')
    Assertion_text9 = (By.LINK_TEXT, '注销')
    Assertion_url = 'http://testsupply.c29a3fa0912b04d208465201aca95c8ce.cn-shenzhen.alicontainer.com/'  # 退出登录断言


    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)
    def input_password(self, password):
        '''输入密码框'''
        self.send_keys(self.password_loc, password)
    def click_submit(self):
        '''登录按钮'''
        self.click(self.submit_loc)
    def assertion_text1(self):
        return self.driver.find_element(*self.Assertion_text1).text
    def assertion_text2(self):
        return self.driver.find_element(*self.Assertion_text2).text
    def assertion_text3(self):
        return self.driver.find_element(*self.Assertion_text3).text
    def assertion_text4(self):
        text=self.driver.find_element(*self.Assertion_text4).text
        self.click(self.Assertion_text8)
        return text
    def assertion_text6(self):
        return self.driver.find_element(*self.Assertion_text6).text
    def assertion_text7(self):
        try:
            self.click(self.Assertion_text9)
        except AssertionError as e:
            with open('/Users/Macx/PycharmProjects/GYL_project/Log/BaseException.log','w+') as file:
                file.write(e)
        else:
            self.click(self.Assertion_text8)



