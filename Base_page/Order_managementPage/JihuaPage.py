# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By
import time

class Rukujihua(BasePage):

    '''
    入库计划页面定位元素
    '''

    Assertion_elm1=(By.XPATH, "//div[@id='ac']/div[3]/div[1]/div[2]/a[2]")  # 订单管理
    Assertion_elm2=(By.LINK_TEXT,u'入库计划') #入库计划
    Assertion_elm3=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/a[2]/span/span[1]')#创建入库计划单
    Assertion_elm4=(By.XPATH,"//form[@id='chooseTypeForm']/div/span/span/a")#入库类型下拉按钮
    Assertion_elm5=(By.XPATH,'//div[12]/div/div[1]')#清单入库
    Assertion_elm6=(By.XPATH,'//div[12]/div/div[2]')#多件入库
    Assertion_elm7=(By.XPATH,"//div[@class='dialog-button']/a[1]/span/span")#下一步按钮
    #清单
    Assertion_elm8=(By.XPATH,"//table[@class='add_tb']/tbody/tr[4]/td[2]/span/span/a")#仓库下拉按钮
    Assertion_elm9=(By.XPATH,"//div[12]/div/div[1]")#下拉选项
    Assertion_elm10=(By.XPATH,"//table[@class='add_tb']/tbody/tr[5]/td[2]/span/span/a")#到达时间下拉按钮
    Assertion_elm11=(By.XPATH,"//div[@class='datebox-button']//a[.='今天']")#下拉选项
    Assertion_elm12=(By.XPATH,'//div[9]/div[2]/div/div/form/table/tbody/tr[5]/td[4]/span/input[1]')#备注1
    Assertion_elm13=(By.XPATH,'//div[9]/div[2]/div/div/form/table/tbody/tr[7]/td[2]/span/input[1]')#备注2
    #多件
    Assertion_elm14=(By.XPATH,"//table[@class='add_tb']/tbody/tr[4]/td[2]/span/span/a")#到达时间下拉按钮
    Assertion_elm15=(By.XPATH,"//div[@class='datebox-button']//a[.='今天']")#下拉选项
    Assertion_elm16=(By.XPATH,'//div[9]/div[2]/div/div/form/table/tbody/tr[4]/td[4]/span/input[1]')#备注1
    Assertion_elm17=(By.XPATH,'//div[9]/div[2]/div/div/form/table/tbody/tr[6]/td[2]/span/input[1]')#备注2
    Assertion_elm18 = (By.LINK_TEXT, u'保存')  # 保存
    Assertion_elm19 = (By.LINK_TEXT, u'关闭')  # 关闭
    Assertion_elm20 = (By.LINK_TEXT, u'确定')  # 确定
    Assertion_elm21 = (By.LINK_TEXT, u'确认')  # 确认
    Assertion_elm22 =(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/\
    div[2]/div[2]/table/tbody/tr[1]/td[1]/div')#订单编号文本
    Assertion_elm23 =(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/\
    div[2]/div[2]/table/tbody/tr[1]/td[2]/div')#状态文本
    Assertion_elm24 =(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/\
    div[2]/div[2]/table/tbody/tr[1]/td[3]/div')#仓库文本
    Assertion_elm25 =(By.XPATH,"//tr[@id='datagrid-row-r1-2-0']/td[9]/div/dt/img")#操作按钮
    Assertion_elm26 =(By.XPATH,'//div[5]/div[1]/div[1]')#查看详情
    Assertion_elm27 =(By.XPATH,'//div[5]/div[2]/div[2]')#作废按钮
    Assertion_elm28 =(By.XPATH,'//div[10]/div[2]/div/div/form/div[2]/span/textarea')#作废信息'
    Assertion_elm29 =(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/\
    div[2]/div[2]/div[2]/table/tbody/tr[1]/td[8]/div/a[2]')#清单管理按钮
    Assertion_elm30 =(By.XPATH,"//div[@id='skuItemTb']//span[.='添加货品']")#添加货品
    Assertion_elm31 =(By.XPATH,'//div[13]/div[2]/div[2]/div/form/div[1]/span/input[1]')#序列号
    Assertion_elm32 =(By.XPATH,'//div[13]/div[2]/div[2]/div/form/div[2]/span/input[1]')#Mac
    Assertion_elm33 =(By.XPATH,'//div[13]/div[2]/div[2]/div/form/div[3]/span/input[1]')#批次
    Assertion_elm34 =(By.XPATH,"//form[@id='addSkuItemForm']/div[4]/span/span/a")#是否检查下拉按钮
    Assertion_elm35 =(By.XPATH,'//div[16]/div/div[2]')#下拉选项
    Assertion_elm36 =(By.XPATH,"//input[@id='storageOrderId']")#订单编号筛选
    Assertion_elm37 =(By.XPATH,"//div[@id='storeplanTb']//span[.='查询']")#查询按钮
    Assertion_elm38 = (By.XPATH, ".//*[@id='storeplanDialog']/div/div[1]/div/div[3]/div[1]")  # 添加清单记录文本
    Assertion_elm39 = (By.CLASS_NAME, 'pagination-info')  # 获取记录


    def assertion_test1(self):
        self.click(self.Assertion_elm1)
    def assertion_test2(self):
        self.click(self.Assertion_elm2)
        time.sleep(1)
    def assertion_test3(self):
        return self.driver.find_element(*self.Assertion_elm39).text
    def assertion_test4(self,data):#创建清单入库
        self.click(self.Assertion_elm3)
        time.sleep(0.5)
        self.click(self.Assertion_elm4)
        time.sleep(0.5)
        self.click(self.Assertion_elm5)
        self.click(self.Assertion_elm7)
        self.click(self.Assertion_elm8)
        self.click(self.Assertion_elm9)
        self.click(self.Assertion_elm10)
        self.click(self.Assertion_elm11)
        self.send_keys(self.Assertion_elm12, data)
        self.send_keys(self.Assertion_elm13, data)
        time.sleep(0.5)
        self.click(self.Assertion_elm18)
        time.sleep(0.5)
        self.click(self.Assertion_elm20)
        time.sleep(0.5)
    def assertion_test5(self,data):#创建多件入库
        self.click(self.Assertion_elm3)
        time.sleep(0.5)
        self.click(self.Assertion_elm4)
        time.sleep(0.5)
        self.click(self.Assertion_elm6)
        self.click(self.Assertion_elm7)
        self.click(self.Assertion_elm14)
        self.click(self.Assertion_elm15)
        self.send_keys(self.Assertion_elm16, data)
        self.send_keys(self.Assertion_elm17, data)
        time.sleep(0.5)
        self.click(self.Assertion_elm18)
        time.sleep(0.5)
        self.click(self.Assertion_elm20)
        time.sleep(0.5)
    def assertion_test6(self):#编号文本
        return self.driver.find_element(*self.Assertion_elm22).text
    def assertion_test7(self):#状态文本
        return self.driver.find_element(*self.Assertion_elm23).text
    def assertion_test8(self):#仓库文本
        return self.driver.find_element(*self.Assertion_elm24).text
    def assertion_test9(self):#查看订单详情
        self.click(self.Assertion_elm25)
        self.click(self.Assertion_elm26)
        time.sleep(0.5)
    def assertion_test10(self):#关闭按钮
        self.click(self.Assertion_elm19)
    def assertion_test11(self,data):#作废订单
        self.click(self.Assertion_elm25)
        self.click(self.Assertion_elm27)
        self.send_keys(self.Assertion_elm28,data)
        time.sleep(0.5)
        self.click(self.Assertion_elm21)
        time.sleep(0.5)
        self.click(self.Assertion_elm20)
        time.sleep(0.5)
    def assertion_test12(self):#重新编辑订单
        self.click(self.Assertion_elm25)
        self.click(self.Assertion_elm27)
        time.sleep(0.5)
        self.click(self.Assertion_elm18)
        time.sleep(0.5)
        self.click(self.Assertion_elm20)
        time.sleep(0.5)
    def assertion_test13(self):#进入清单管理
        time.sleep(0.5)
        self.click(self.Assertion_elm29)
        time.sleep(0.5)
    def assertion_test14(self,data):#添加货品清单
        self.click(self.Assertion_elm30)
        time.sleep(1)
        self.send_keys(self.Assertion_elm31, data)
        self.send_keys(self.Assertion_elm32, data)
        self.send_keys(self.Assertion_elm33, data)
        time.sleep(0.5)
        self.click(self.Assertion_elm34)
        time.sleep(0.5)
        self.click(self.Assertion_elm35)
        time.sleep(0.5)
        self.click(self.Assertion_elm18)
        time.sleep(0.5)
        self.click(self.Assertion_elm20)
        time.sleep(0.5)
    def assertion_test15(self):#清单记录文本
        return self.driver.find_element(*self.Assertion_elm38).text
    def assertion_test16(self,data):#入库计划订单编号筛选
        self.send_keys(self.Assertion_elm36, data)
        self.click(self.Assertion_elm37)
        time.sleep(0.5)


