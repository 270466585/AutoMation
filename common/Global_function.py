# coding:utf-8
from Base_page.LoginPage import Loginpage
from common import read_Data
import time as t

'''
该页面和内容方法适合整个自动化
'''
login_url = "#################"


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
