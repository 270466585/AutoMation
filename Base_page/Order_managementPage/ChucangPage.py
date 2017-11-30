# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By
import time

class Chucangruku(BasePage):

    '''
    出厂入库页面定位元素
    '''

    Assertion_elm1=(By.XPATH, "//div[@id='ac']/div[3]/div[1]/div[2]/a[2]")  # 订单管理
    Assertion_elm2=(By.LINK_TEXT,u'出厂入库') #出厂入库
    Assertion_elm3=(By.XPATH, '//div[2]/div[3]/div/div/div[2]/div[2]/div/div/\
    div[1]/div[2]/div[1]/div[2]/a[2]/span/span[1]') #创建入库单
    Assertion_elm4=(By.XPATH, "//form[@id='addStorageForm']/table/tbody/tr[4]/td[2]/span/span/a")#采购订单下拉按钮
    Assertion_elm5=(By.XPATH, "//div[12]/div/div[1]")#下拉选项
    Assertion_elm6=(By.XPATH, "//form[@id='addStorageForm']/table/tbody/tr[6]/td[2]/span/span/a")#仓库下拉按钮
    Assertion_elm7=(By.XPATH, "//div[13]/div/div[1]")#下拉选项
    Assertion_elm8=(By.XPATH, "//form[@id='addStorageForm']/table/tbody/tr[7]/td[2]/span/span/a")#到达时间下拉按钮
    Assertion_elm9=(By.XPATH, "//div[@class='datebox-button']//a[.='今天']")#下拉选项
    Assertion_elm10=(By.XPATH, '//div[9]/div[2]/div/div/form/table/tbody/tr[7]/td[4]/span/input[1]')#备注1
    Assertion_elm11=(By.XPATH, '//div[9]/div[2]/div/div/form/table/tbody/tr[9]/\
    td/table/tbody/tr[2]/td[5]/span/input[1]')#计划到货数
    Assertion_elm12=(By.XPATH, '//div[9]/div[2]/div/div/form/table/tbody/tr[9]/\
    td/table/tbody/tr[2]/td[6]/input')#备注2
    Assertion_elm13=(By.XPATH, '//div[9]/div[2]/div/div/form/table/tbody/tr[11]/td[2]/span/input[1]')#备注3
    Assertion_elm14 = (By.LINK_TEXT, u'保存')  # 保存
    Assertion_elm15 = (By.LINK_TEXT, u'关闭')  # 关闭
    Assertion_elm16 = (By.LINK_TEXT, u'确定')  # 确定
    Assertion_elm17 = (By.LINK_TEXT, u'确认')  # 确认
    Assertion_elm18 = (By.CLASS_NAME, 'pagination-info')  # 获取记录
    Assertion_elm19=(By.XPATH, '//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/\
    div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/div')#订单编号文本
    Assertion_elm20=(By.XPATH, '//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/\
    div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/div')#状态文本
    Assertion_elm21=(By.XPATH, '//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/\
    div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]/div')#库区文本
    Assertion_elm22=(By.XPATH, "//tr[@id='datagrid-row-r1-2-0']/td[9]/div/dt/img")#操作按钮
    Assertion_elm23=(By.XPATH, '//div[5]/div[1]/div[1]')#查看入库单详情
    Assertion_elm24=(By.XPATH, '//div[10]/div[1]/div[1]')#详情title文本
    Assertion_elm25=(By.XPATH, '//div[5]/div[2]/div[1]')#作废按钮或重新编辑
    Assertion_elm26=(By.XPATH, '//div[10]/div[2]/div/div/form/div[2]/span/textarea')#作废信息
    Assertion_elm27=(By.XPATH, "//form[@id='editStorageForm']/table/tbody/tr[6]/td[2]/span/span/a")#重新编辑库区下拉按钮
    Assertion_elm28=(By.XPATH, "//div[14]/div/div[2]")#下拉选项
    Assertion_elm29=(By.XPATH, "//input[@id='storageOrderId']")#订单编号筛选
    Assertion_elm30=(By.XPATH, "//div[@id='storageTb']//span[.='查询']")#查询按钮
    Assertion_elm31=(By.XPATH, "//tr[@id='datagrid-row-r1-2-0']//a[.='清单管理']")#清单管理
    Assertion_elm32=(By.XPATH, "//div[@id='skuItemTb']//span[.='添加货品']")#添加货品
    Assertion_elm33=(By.XPATH, '//div[13]/div[2]/div[2]/div/form/div[1]/span/input[1]')#序列号
    Assertion_elm34=(By.XPATH, '//div[13]/div[2]/div[2]/div/form/div[2]/span/input[1]')#MAC地址
    Assertion_elm35=(By.XPATH, '//div[13]/div[2]/div[2]/div/form/div[3]/span/input[1]')#生成批次
    Assertion_elm36=(By.XPATH, "//form[@id='addSkuItemForm']/div[4]/span/span/a")#检验下拉按钮
    Assertion_elm37=(By.XPATH, '//div[16]/div/div[2]')#下拉选项
    Assertion_elm38=(By.XPATH, ".//*[@id='storageDialog']/div/div[1]/div/div[3]/div[1]")#添加清单记录文本




    def assertion_test1(self):
        self.click(self.Assertion_elm1)
    def assertion_test2(self):
        self.click(self.Assertion_elm2)
        time.sleep(1)
    def assertion_test3(self):
        return self.driver.find_element(*self.Assertion_elm18).text
    def assertion_test4(self,data,data1):#创建入库单
        self.click(self.Assertion_elm3)
        self.click(self.Assertion_elm4)
        self.click(self.Assertion_elm5)
        self.click(self.Assertion_elm6)
        self.click(self.Assertion_elm7)
        self.click(self.Assertion_elm8)
        self.click(self.Assertion_elm9)
        self.send_keys(self.Assertion_elm10,data)
        self.send_keys(self.Assertion_elm11, data1)
        self.send_keys(self.Assertion_elm12, data)
        self.send_keys(self.Assertion_elm13, data)
        time.sleep(0.5)
        self.click(self.Assertion_elm14)
        time.sleep(0.5)
        self.click(self.Assertion_elm16)
        time.sleep(0.5)
    def assertion_test5(self):#查看入库单详情
        self.click(self.Assertion_elm22)
        self.click(self.Assertion_elm23)
        time.sleep(0.5)
    def assertion_test6(self):#关闭按钮
        self.click(self.Assertion_elm15)
        time.sleep(0.5)
    def assertion_test7(self):#详情title文本
        return self.driver.find_element(*self.Assertion_elm24).text
    def assertion_test8(self):#订单编号文本
        return self.driver.find_element(*self.Assertion_elm19).text
    def assertion_test9(self):#状态文本
        return self.driver.find_element(*self.Assertion_elm20).text
    def assertion_test10(self):#库区文本
        return self.driver.find_element(*self.Assertion_elm21).text
    def assertion_test11(self,data):#作废入库单
        self.click(self.Assertion_elm22)
        self.click(self.Assertion_elm25)
        self.send_keys(self.Assertion_elm26,data)
        time.sleep(0.5)
        self.click(self.Assertion_elm17)
        time.sleep(0.5)
        self.click(self.Assertion_elm16)
        time.sleep(0.5)
    def assertion_test12(self):#重新编辑入库单
        self.click(self.Assertion_elm22)
        self.click(self.Assertion_elm25)
        time.sleep(1)
        self.click(self.Assertion_elm27)
        time.sleep(0.5)
        self.click(self.Assertion_elm28)
        time.sleep(0.5)
        self.click(self.Assertion_elm14)
        time.sleep(0.5)
        self.click(self.Assertion_elm16)
        time.sleep(0.5)
    def assertion_test13(self,data):#入库单筛选
        self.send_keys(self.Assertion_elm29, data)
        self.click(self.Assertion_elm30)
        time.sleep(0.5)
    def assertion_test16(self):#进入清单管理
        self.click(self.Assertion_elm31)
        time.sleep(0.5)
    def assertion_test14(self,data):#添加货品清单
        self.click(self.Assertion_elm32)
        time.sleep(1)
        self.send_keys(self.Assertion_elm33, data)
        self.send_keys(self.Assertion_elm34, data)
        self.send_keys(self.Assertion_elm35, data)
        self.click(self.Assertion_elm36)
        self.click(self.Assertion_elm37)
        time.sleep(0.5)
        self.click(self.Assertion_elm14)
        time.sleep(0.5)
        self.click(self.Assertion_elm16)

    def assertion_test15(self):#清单记录文本
        return self.driver.find_element(*self.Assertion_elm38).text



