# coding:utf-8
from Base_page.LoginPage import Loginpage
from common import read_Data
import time as t

'''
该页面和内容方法适合整个自动化
'''
login_url = "http://testsupply20171114.c29a3fa0912b04d208465201aca95c8ce.cn-shenzhen.alicontainer.com/login"


def login(self):
    '''
    
    :param self: 登陆
    :return: 
    '''
    self.LOGIN=Loginpage(self.driver)
    self.LOGIN.input_username(read_Data.getExcel1(5, 0))
    self.LOGIN.input_password(read_Data.getExcel1(5, 1))
    self.LOGIN.click_submit()
    t.sleep(1)
