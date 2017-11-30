# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By
import time
class Chukuguanli(BasePage):

    '''
    出库管理页面定位元素
    '''

    Assertion_elm1=(By.XPATH, "//div[@id='ac']/div[2]/div[1]/div[1]")  # 仓库管理
    Assertion_elm2=(By.LINK_TEXT,u'出库管理') #出库管理
    Assertion_elm3=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/\
    div[2]/div[2]/table/tbody/tr[1]/td[1]/div')#批次编号文本
    Assertion_elm4=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/\
    div[2]/div[2]/table/tbody/tr[1]/td[4]/div')#状态文本
    Assertion_elm5=(By.XPATH,"//input[@id='deliveryOrderId']")#批次筛选
    Assertion_elm6=(By.XPATH,"//div[@id='deliveryTb']/div[2]/a/span/span[2]")#查询按钮
    Assertion_elm7=(By.XPATH,"//tr[@id='datagrid-row-r1-2-0']/td[7]/div/dt/img")#操作按钮
    Assertion_elm8=(By.XPATH,"//div[@id='deliveryMenu']/div[1]/div[1]")#查看详情按钮
    Assertion_elm9=(By.XPATH,'//div[5]/div[2]/div[1]')#缺货按钮
    Assertion_elm10=(By.XPATH,'//div[10]/div[2]/div/div/form/div[2]/span/textarea')#缺货信息
    Assertion_elm29=(By.XPATH,'//div[5]/div[2]/div[1]')#开始发货
    Assertion_elm11=(By.XPATH,'//div[5]/div[3]/div[1]')#完成备货按钮
    Assertion_elm12=(By.XPATH,'//div[5]/div[2]/div[1]')#重新发货
    Assertion_elm13=(By.XPATH,'//div[5]/div[3]/div[1]')#发货离库
    Assertion_elm14=(By.XPATH,'//div[10]/div[2]/div/div/form/div[3]/span/input[1]')#运单号
    Assertion_elm15=(By.XPATH,"//div[@id='d2']/span/span/a")#快递下拉按钮
    Assertion_elm16=(By.XPATH,'//div[13]/div/div[1]')#下拉选项
    Assertion_elm17=(By.XPATH,'//div[10]/div[2]/div/div/form/div[5]/span/textarea')#发货信息
    Assertion_elm18=(By.XPATH,'//div[5]/div[4]/div[1]')#物流信息
    Assertion_elm19=(By.XPATH,'//div[10]/div[2]/div[2]/div/form/div[1]/input[2]')#自提按钮
    Assertion_elm30 = (By.XPATH,'//div[10]/div[2]/div/div/form/div[2]/input[1]')  # 物流按钮
    Assertion_elm20 = (By.CLASS_NAME, 'pagination-info')  # 获取记录
    Assertion_elm21 = (By.LINK_TEXT, u'保存')  # 保存
    Assertion_elm22 = (By.LINK_TEXT, u'关闭')  # 关闭
    Assertion_elm23 = (By.LINK_TEXT, u'确定')  # 确定
    Assertion_elm24 = (By.LINK_TEXT, u'确认')  # 确认
    Assertion_elm25=(By.XPATH,"//tr[@id='datagrid-row-r1-2-0']//a[.='清单管理']")#清单管理
    Assertion_elm26=(By.XPATH,"//div[@id='ddTb']/a[1]/span")#添加货品
    Assertion_elm27=(By.XPATH,'//div[12]/div[2]/div[2]/div/form/div[1]/span/input[1]')#序列号
    Assertion_elm28=(By.XPATH,'//div[9]/div[2]/div/div[1]/div/div[3]/div[1]')#清单记录
    Assertion_elm31=(By.XPATH,"//div[@id='deliveryTb']/div[1]/div/table/tbody/tr[2]/td[6]/span/span/a")#状态筛选下拉按钮
    Assertion_elm32=(By.XPATH,'//div[9]/div/div[2]')#待出库
    Assertion_elm33=(By.XPATH,'//div[9]/div/div[3]')#缺货
    Assertion_elm34=(By.XPATH,'//div[9]/div/div[4]')#待发货
    Assertion_elm35=(By.XPATH,'//div[9]/div/div[5]')#已出库
    Assertion_elm36=(By.XPATH,"//div[9]/div/div[6]")#取消出库
    Assertion_elm37 = (By.XPATH, "//div[9]/div/div[1]")  # 还原


    def assertion_test1(self):
        self.click(self.Assertion_elm1)
    def assertion_test2(self):
        self.click(self.Assertion_elm2)
        time.sleep(1)
    def assertion_test3(self):#订单编号文本
        return self.driver.find_element(*self.Assertion_elm3).text
    def assertion_test4(self):#状态文本
        return self.driver.find_element(*self.Assertion_elm4).text
    def assertion_test5(self):#获取记录
        return self.driver.find_element(*self.Assertion_elm20).text
    def assertion_test6(self,data):#订单编号筛选
        self.send_keys(self.Assertion_elm5,data)
        self.click(self.Assertion_elm6)
        time.sleep(0.5)
    def assertion_test7(self):#查看详情
        self.click(self.Assertion_elm7)
        self.click(self.Assertion_elm8)
        time.sleep(0.5)
    def assertion_test8(self):#关闭按钮
        self.click(self.Assertion_elm22)
    def assertion_test9(self,data):#缺货
        self.click(self.Assertion_elm7)
        time.sleep(0.5)
        self.click(self.Assertion_elm9)
        time.sleep(0.5)
        self.send_keys(self.Assertion_elm10,data)
        time.sleep(0.5)
        self.click(self.Assertion_elm24)
        time.sleep(0.5)
        self.click(self.Assertion_elm23)
        time.sleep(0.5)
    def assertion_test17(self):#开始发货
        self.click(self.Assertion_elm7)
        time.sleep(0.5)
        self.click(self.Assertion_elm29)
        time.sleep(0.5)
        self.click(self.Assertion_elm23)
        time.sleep(0.5)
        self.click(self.Assertion_elm23)
        time.sleep(0.5)
    def assertion_test10(self):#完成备货
        self.click(self.Assertion_elm7)
        self.click(self.Assertion_elm11)
        time.sleep(0.5)
        self.click(self.Assertion_elm23)
        time.sleep(0.5)
        self.click(self.Assertion_elm23)
        time.sleep(0.5)
    def assertion_test11(self):#重新发货
        self.click(self.Assertion_elm7)
        time.sleep(0.5)
        self.click(self.Assertion_elm12)
        time.sleep(0.5)
        self.click(self.Assertion_elm23)
        time.sleep(0.5)
        self.click(self.Assertion_elm23)
        time.sleep(0.5)
    def assertion_test12(self,data):#发货离库
        self.click(self.Assertion_elm7)
        time.sleep(0.5)
        self.click(self.Assertion_elm13)
        try:
            ResuLt=self.is_selected(self.Assertion_elm30)
            print(ResuLt)
            self.click(self.Assertion_elm30)
            self.send_keys(self.Assertion_elm14, data)
            self.click(self.Assertion_elm15)
            self.click(self.Assertion_elm16)
            self.send_keys(self.Assertion_elm17, data)
        except:
            pass
        finally:
            time.sleep(0.5)
            self.click(self.Assertion_elm24)
            time.sleep(0.5)
            self.click(self.Assertion_elm23)
            time.sleep(0.5)
    def assertion_test13(self):#物流信息
        self.click(self.Assertion_elm7)
        time.sleep(0.5)
        self.click(self.Assertion_elm18)
        self.click(self.Assertion_elm19)
        time.sleep(0.5)
        self.click(self.Assertion_elm24)
        time.sleep(0.5)
        self.click(self.Assertion_elm23)
        time.sleep(0.5)
    def assertion_test14(self):#进入清单管理
        time.sleep(0.5)
        self.click(self.Assertion_elm25)
        time.sleep(0.5)
    def assertion_test15(self,data):#添加货品
        self.click(self.Assertion_elm26)
        self.send_keys(self.Assertion_elm27,data)
        time.sleep(0.5)
        self.click(self.Assertion_elm21)
        time.sleep(0.5)
        self.click(self.Assertion_elm23)
        time.sleep(0.5)
    def assertion_test16(self):#清单记录文本
        return self.driver.find_element(*self.Assertion_elm28).text
    def assertion_test18(self):#待出库筛选
        self.click(self.Assertion_elm31)
        self.click(self.Assertion_elm32)
        self.click(self.Assertion_elm6)
        time.sleep(0.5)
    def assertion_test19(self):#缺货筛选
        self.click(self.Assertion_elm31)
        self.click(self.Assertion_elm33)
        self.click(self.Assertion_elm6)
        time.sleep(0.5)
    def assertion_test20(self):#待发货筛选
        self.click(self.Assertion_elm31)
        self.click(self.Assertion_elm34)
        self.click(self.Assertion_elm6)
        time.sleep(0.5)
    def assertion_test21(self):#已发货筛选
        self.click(self.Assertion_elm31)
        self.click(self.Assertion_elm35)
        self.click(self.Assertion_elm6)
        time.sleep(0.5)
    def assertion_test22(self):#取消出库筛选
        self.click(self.Assertion_elm31)
        self.click(self.Assertion_elm36)
        self.click(self.Assertion_elm6)
        time.sleep(0.5)
    def assertion_test23(self):#筛选还原
        self.click(self.Assertion_elm31)
        self.click(self.Assertion_elm37)
        time.sleep(0.5)



