# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By
import time

class Xiaoshoudingdan(BasePage):

    '''
    销售订单页面定位元素
    '''

    Assertion_elm1=(By.XPATH, "//div[@id='ac']/div[3]/div[1]/div[2]/a[2]")  # 订单管理
    Assertion_elm2=(By.LINK_TEXT,u'销售订单') #销售订单
    Assertion_elm3=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/\
    div[1]/div[2]/div[1]/div[2]/a[2]/span/span[1]') #创建销售订单按钮
    Assertion_elm4=(By.XPATH,"//div[9]/div[2]/div/div/form/table/tbody/tr[4]/td[2]/span/span/a") #客户名称下拉按钮
    Assertion_elm5=(By.XPATH,'//div[12]/div/div[1]') #下拉选项
    Assertion_elm6=(By.XPATH,"//div[9]/div[2]/div/div/form/table/tbody/tr[5]/td[2]/span/span/a") #合同下拉按钮
    Assertion_elm7=(By.XPATH,'//div[13]/div/div') #下拉选项
    Assertion_elm8=(By.XPATH,'//div[9]/div[2]/div/div/form/table/tbody/tr[5]/td[4]/span/input[1]') #备注
    Assertion_elm9=(By.XPATH,'//div[9]/div[2]/div/div/form/table/tbody/tr[6]/td[2]/span/input[1]') #收件人
    Assertion_elm10=(By.XPATH,'//div[9]/div[2]/div/div/form/table/tbody/tr[6]/td[4]/span/input[1]') #联系号码
    Assertion_elm11=(By.XPATH,"//form[@id='addSaleForm']/table/tbody/tr[7]/td[2]/span[1]/span/a") #省下拉按钮
    Assertion_elm12=(By.XPATH,'//div[14]/div/div[1]') #下拉选项
    Assertion_elm13=(By.XPATH,"//form[@id='addSaleForm']/table/tbody/tr[7]/td[2]/span[2]/span/a") #市下拉按钮
    Assertion_elm14=(By.XPATH,'//div[15]/div/div') #下拉按钮
    Assertion_elm15=(By.XPATH,"//form[@id='addSaleForm']/table/tbody/tr[7]/td[2]/span[3]/span/a") #区下拉按钮
    Assertion_elm16=(By.XPATH,'//div[16]/div/div[1]') #下拉选项
    Assertion_elm17=(By.XPATH,'//div[9]/div[2]/div/div/form/table/tbody/tr[8]/td[2]/span/input[1]') #街道地址
    Assertion_elm18=(By.XPATH,'//div[9]/div[2]/div/div/form/table/tbody/tr[9]/td[2]/span/input[1]') #备注
    Assertion_elm19=(By.XPATH,"//td[@id='tbtd']/table/tbody/tr[2]/td[2]/span/span/a") #sku1下拉按钮
    Assertion_elm20=(By.XPATH,'//div[17]/div/div[1]') #下拉选项
    Assertion_elm21=(By.XPATH,'//div[9]/div[2]/div/div/form/table/tbody/\
    tr[11]/td/table/tbody/tr[2]/td[4]/span/input[1]') #销售数量
    Assertion_elm22=(By.XPATH,"//td[@id='tbtd']/table/tbody/tr[2]/td[7]/span/span/a") #日期下拉按钮
    Assertion_elm23=(By.XPATH,"//div[@class='datebox-button']//a[.='今天']") #下拉选项
    Assertion_elm24=(By.XPATH,'//div[9]/div[2]/div/div/form/table/tbody/\
    tr[11]/td/table/tbody/tr[2]/td[9]/span/input[1]') #备注
    Assertion_elm25=(By.XPATH,'//div[9]/div[2]/div/div/form/table/\
    tbody/tr[13]/td[2]/span/input[1]') #其他费用
    Assertion_elm26=(By.XPATH,'//div[9]/div[2]/div/div/form/table/\
    tbody/tr[13]/td[8]/span/input[1]') #备注
    Assertion_elm27=(By.XPATH,'//div[9]/div[2]/div/div/form/table/\
    tbody/tr[15]/td[2]/span/input[1]') #备注
    Assertion_elm28 = (By.LINK_TEXT, u'保存')  # 保存
    Assertion_elm29 = (By.LINK_TEXT, u'关闭')  # 关闭
    Assertion_elm30 = (By.LINK_TEXT, u'确定')  # 确定
    Assertion_elm42 = (By.LINK_TEXT, u'确认')  # 确认
    Assertion_elm31=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/\
    div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/div') #客户名称文本
    Assertion_elm32=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/\
    div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[5]/div') #状态文本
    Assertion_elm33 = (By.CLASS_NAME, 'pagination-info')  # 获取记录文本
    Assertion_elm34=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/\
    div/div/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[6]/div/dt/img') #操作按钮
    Assertion_elm35=(By.XPATH,'//div[5]/div[1]/div[1]') #查看详情
    Assertion_elm36=(By.XPATH,'//div[5]/div[2]/div[1]') #编辑按钮/审核后二次编辑
    Assertion_elm37=(By.XPATH,"//form[@id='editSaleForm']/table/tbody/tr[4]/td[2]/span/span/a") #编辑客户名称下拉
    Assertion_elm38=(By.XPATH,'//div[13]/div/div[2]') #下拉按钮
    Assertion_elm39=(By.XPATH,'//div[5]/div[3]/div[1]') #审核按钮
    Assertion_elm40=(By.XPATH,'//div[10]/div[2]/div/div/form/div[2]/span/textarea') #审核信息
    Assertion_elm41=(By.XPATH,".//div[@class='panel-header']/div[1]/div[1]")#详情title文本
    Assertion_elm43=(By.XPATH,"//input[@id='saleOrderId']")#订单编号筛选
    Assertion_elm44=(By.XPATH,"//div[@id='saleTb']//span[.='查询']")#查询按钮
    Assertion_elm45=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/\
    div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/div')#订单编号文本
    "//div[@class='panel-header-noborder]//div[.='销售订单详情']"
    ".//div[@class='panel-header']/div[1]/div[1]"



    def assertion_test1(self):
        self.click(self.Assertion_elm1)
    def assertion_test2(self):
        self.click(self.Assertion_elm2)
        time.sleep(1)
    def assertion_test3(self,data,data1,data2):#创建销售订单
        self.click(self.Assertion_elm3)
        self.click(self.Assertion_elm4)
        self.click(self.Assertion_elm5)
        self.click(self.Assertion_elm6)
        self.click(self.Assertion_elm7)
        self.send_keys(self.Assertion_elm8,data)
        self.send_keys(self.Assertion_elm9,data)
        self.send_keys(self.Assertion_elm10,data1)#手机号
        self.click(self.Assertion_elm11)
        self.click(self.Assertion_elm12)
        self.click(self.Assertion_elm13)
        self.click(self.Assertion_elm14)
        self.click(self.Assertion_elm15)
        self.click(self.Assertion_elm16)
        self.send_keys(self.Assertion_elm17, data)
        self.send_keys(self.Assertion_elm18, data)
        self.click(self.Assertion_elm19)
        self.click(self.Assertion_elm20)
        self.send_keys(self.Assertion_elm21, data2)
        self.click(self.Assertion_elm22)
        self.click(self.Assertion_elm23)
        self.send_keys(self.Assertion_elm24, data)
        self.send_keys(self.Assertion_elm25, data2)
        self.send_keys(self.Assertion_elm26, data)
        self.send_keys(self.Assertion_elm27, data)
        time.sleep(0.5)
        self.click(self.Assertion_elm28)
        time.sleep(0.5)
        self.click(self.Assertion_elm30)
    def assertion_test4(self):#客户名称文本
        return self.driver.find_element(*self.Assertion_elm31).text
    def assertion_test5(self):#状态文本
        return self.driver.find_element(*self.Assertion_elm32).text
    def assertion_test6(self):#获取记录文本
        return self.driver.find_element(*self.Assertion_elm33).text
    def assertion_test7(self):#详情title文本
        return self.driver.find_element(*self.Assertion_elm41).text
    def assertion_test8(self):  # 查看详情
        self.click(self.Assertion_elm34)
        self.click(self.Assertion_elm35)
    def assertion_test9(self):  # 关闭按钮
        self.click(self.Assertion_elm29)
    def assertion_test10(self):  # 编辑销售单
        self.click(self.Assertion_elm34)
        self.click(self.Assertion_elm36)
        time.sleep(0.5)
        self.click(self.Assertion_elm37)
        time.sleep(0.5)
        self.click(self.Assertion_elm38)
        time.sleep(0.5)
        self.click(self.Assertion_elm28)
        time.sleep(0.5)
        self.click(self.Assertion_elm30)
        time.sleep(0.5)
    def assertion_test11(self,data):  # 审核销售单
        self.click(self.Assertion_elm34)
        self.click(self.Assertion_elm39)
        self.send_keys(self.Assertion_elm40, data)
        self.click(self.Assertion_elm42)
        self.click(self.Assertion_elm30)
    def assertion_test12(self,data):  # 订单编号筛选
        self.send_keys(self.Assertion_elm43, data)
        self.click(self.Assertion_elm44)
    def assertion_test13(self):#订单编号文本
        return self.driver.find_element(*self.Assertion_elm45).text




