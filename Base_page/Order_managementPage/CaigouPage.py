# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By
import time

class Caigoudingdan(BasePage):

    '''
    采购订单页面定位元素
    '''

    Assertion_elm1=(By.XPATH, "//div[@id='ac']/div[3]/div[1]/div[2]/a[2]")  # 订单管理
    Assertion_elm2=(By.LINK_TEXT,u'采购订单') #采购订单
    Assertion_elm3=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/\
    div/div[1]/div[2]/div[1]/div[2]/a[2]/span/span[1]')#创建采购订单
    Assertion_elm4=(By.XPATH,"//form[@id='addPurchaseForm']/table/tbody/tr[4]/td[2]/span/span/a")#入库仓库下拉按钮
    Assertion_elm5=(By.XPATH,'//div[13]/div/div[1]')#下拉选项
    Assertion_elm6=(By.XPATH,'//div[10]/div[2]/div/div/form/table/tbody/tr[5]/td[2]/span/input[1]')#备注
    Assertion_elm7=(By.XPATH,"//form[@id='addPurchaseForm']/table/tbody/tr[7]/td[2]/span/span/a")#供应商下拉按钮
    Assertion_elm8=(By.XPATH,'//div[14]/div/div[1]')#下拉选项
    Assertion_elm9=(By.XPATH,"//form[@id='addPurchaseForm']/table/tbody/tr[8]/td[2]/span/span/a")#合同下拉按钮
    Assertion_elm10=(By.XPATH,'//div[15]/div/div')#下拉选项
    Assertion_elm11=(By.XPATH,'//div[10]/div[2]/div/div/form/table/tbody/tr[8]/td[4]/span/input[1]')#备注
    Assertion_elm12=(By.XPATH,"//form[@id='addPurchaseForm']//a[.='重置']")#重置按钮
    Assertion_elm13=(By.XPATH,"//td[@id='tbtd']/table/tbody/tr[2]/td[2]/span/span/a")#sku1下拉按钮
    Assertion_elm14=(By.XPATH,'//div[22]/div/div[1]')#下拉选项
    Assertion_elm15=(By.XPATH,'//div[10]/div[2]/div/div/form/table/tbody/\
    tr[10]/td/table/tbody/tr[2]/td[4]/span/input[1]')#采购数量
    Assertion_elm16=(By.XPATH,"//td[@id='tbtd']/table/tbody/tr[2]/td[8]/span/span/a")#交付时间下拉按钮
    Assertion_elm17=(By.XPATH,"//div[@class='datebox-button']//a[.='今天']")#下拉选项
    Assertion_elm18=(By.XPATH,'//div[10]/div[2]/div/div/form/table/tbody/\
    tr[10]/td/table/tbody/tr[2]/td[9]/span/input[1]')#备注
    Assertion_elm19=(By.XPATH,'//div[10]/div[2]/div/div/form/table/tbody/tr[12]/td[2]/span/input[1]')#备注
    Assertion_elm20 = (By.LINK_TEXT, u'保存')  # 保存
    Assertion_elm21 = (By.LINK_TEXT, u'关闭')  # 关闭
    Assertion_elm22 = (By.LINK_TEXT, u'确定')  # 确定
    Assertion_elm38 = (By.LINK_TEXT, u'确认')  # 确认
    Assertion_elm23 = (By.CLASS_NAME, 'pagination-info')  # 获取记录
    Assertion_elm24 = (By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/\
    div/div/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]/div') #仓库名称文本
    Assertion_elm25 = (By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/\
    div/div/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[5]/div') #状态文本
    Assertion_elm26 = (By.XPATH,"//tr[@id='datagrid-row-r1-2-0']/td[7]/div/dt/img") #操作按钮
    Assertion_elm27 = (By.XPATH,'//div[5]/div[1]/div[1]') #查看详情
    Assertion_elm28 = (By.XPATH,'//div[10]/div[1]/div[1]') # 订单详情title文本
    Assertion_elm29 = (By.XPATH,'//div[5]/div[2]/div[1]') #编辑
    Assertion_elm30 = (By.XPATH,"//form[@id='editPurchaseForm']/table/tbody/tr[4]/td[2]/span/span/a") #编辑出库下拉按钮
    Assertion_elm31 = (By.XPATH,"//div[20]/div/div[2]") #下拉选项
    Assertion_elm32 = (By.XPATH,'//div[5]/div[3]/div[1]') #审核按钮
    Assertion_elm33 = (By.XPATH,'//div[17]/div[2]/div/div/form/div[2]/span/textarea') #审核信息
    Assertion_elm34 = (By.XPATH,'//div[5]/div[3]/div[1]') #完成采购
    Assertion_elm35 = (By.XPATH,'//div[11]/div[2]/div/div/form/div[2]/span/textarea') #完成信息
    Assertion_elm36 = (By.XPATH,"//input[@id='purchaseOrderId']")#筛选
    Assertion_elm37 = (By.XPATH,"//div[@id='purchaseTb']//span[.='查询']")#查询按钮
    Assertion_elm39 = (By.XPATH, "//input[@id='purchaseOrderId']")  # 订单编号筛选
    Assertion_elm40 = (By.XPATH, "//div[@id='purchaseTb']//span[.='查询']")  # 查询按钮
    Assertion_elm41 = (By.XPATH, '//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/\
    div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/div')  # 订单编号文本


    def assertion_test1(self):
        self.click(self.Assertion_elm1)
    def assertion_test2(self):
        self.click(self.Assertion_elm2)
    def assertion_test3(self):
        return self.driver.find_element(*self.Assertion_elm23).text
    def assertion_test4(self,data,data1,data2,data3,data4):#创建订单
        self.click(self.Assertion_elm3)
        self.click(self.Assertion_elm4)
        self.click(self.Assertion_elm5)
        self.send_keys(self.Assertion_elm6,data)
        self.click(self.Assertion_elm7)
        self.click(self.Assertion_elm8)
        self.click(self.Assertion_elm9)
        self.click(self.Assertion_elm10)
        self.send_keys(self.Assertion_elm11, data1)
        self.click(self.Assertion_elm13)
        self.click(self.Assertion_elm12)#重置
        time.sleep(1)
        self.click(self.Assertion_elm13)
        self.click(self.Assertion_elm14)
        self.send_keys(self.Assertion_elm15, data2)
        self.click(self.Assertion_elm16)
        self.click(self.Assertion_elm17)
        self.send_keys(self.Assertion_elm19, data3)
        self.send_keys(self.Assertion_elm19, data4)
        time.sleep(0.5)
        self.click(self.Assertion_elm20)
        time.sleep(0.5)
        self.click(self.Assertion_elm22)
    def assertion_test5(self):#仓库名称文本
        return self.driver.find_element(*self.Assertion_elm24).text
    def assertion_test6(self):#采购订单订单状态文本
        return self.driver.find_element(*self.Assertion_elm25).text
    def assertion_test7(self):# 订单详情title文本
        return self.driver.find_element(*self.Assertion_elm28).text
    def assertion_test8(self):  # 查看详情
        try:
            self.driver.find_element(*self.Assertion_elm26).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm26)
            self.click(self.Assertion_elm27)
    def assertion_test9(self):  # 关闭按钮
        self.click(self.Assertion_elm21)
    def assertion_test10(self):  # 编辑采购订单
        time.sleep(1)
        self.click(self.Assertion_elm26)
        time.sleep(1)
        self.click(self.Assertion_elm29)
        time.sleep(3)
        self.click(self.Assertion_elm30)
        time.sleep(0.5)
        self.click(self.Assertion_elm31)
        time.sleep(0.5)
        self.click(self.Assertion_elm20)
        time.sleep(0.5)
        self.click(self.Assertion_elm22)
    def assertion_test11(self,data):  # 审核采购订单
        try:
            self.driver.find_element(*self.Assertion_elm26).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm26)
            self.click(self.Assertion_elm32)
            self.send_keys(self.Assertion_elm33, data)
            time.sleep(0.5)
            self.click(self.Assertion_elm38)
            time.sleep(0.5)
            self.click(self.Assertion_elm22)
    def assertion_test12(self,data):  # 订单编号筛选
        self.send_keys(self.Assertion_elm39, data)
        self.click(self.Assertion_elm40)
    def assertion_test13(self):#订单编号文本
        return self.driver.find_element(*self.Assertion_elm41).text



