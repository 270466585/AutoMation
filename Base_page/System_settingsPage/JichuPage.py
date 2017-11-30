# coding:utf-8

from Base_page.DriverPage import BasePage
from selenium.webdriver.common.by import By
import time


class Jichu(BasePage):

    '''
    基础信息维护页面定位元素
    '''

    Assertion_elm1=(By.XPATH, "//div[@id='ac']/div[1]/div[1]/div[1]")  # 系统设置
    Assertion_elm2 = (By.LINK_TEXT, u'基础信息维护')  # 基础信息维护
    Assertion_elm3=(By.XPATH, "//div[@id='layout_center_tabs']/div[2]/\
    div[2]/div/div[1]/div/div/span/span/a")#下拉按钮
    Assertion_elm4=(By.XPATH,'//div[4]/div/div[1]')#货品类别设置
    Assertion_elm5=(By.XPATH,'//div[4]/div/div[2]')#包装设置
    Assertion_elm6=(By.XPATH,'//div[4]/div/div[3]')#SKU设置
    Assertion_elm7=(By.XPATH,'//div[4]/div/div[4]')#库区类别管理
    Assertion_elm8=(By.XPATH,'//div[4]/div/div[5]')#库区管理
    Assertion_elm9=(By.XPATH,'//div[4]/div/div[6]')#供应商管理
    Assertion_elm10=(By.XPATH,'//div[4]/div/div[7]')#客户信息管理
    Assertion_elm11=(By.XPATH,'//div[4]/div/div[8]')#合同管理
    Assertion_elm14 = (By.LINK_TEXT, u'保存')  # 保存
    Assertion_elm15 = (By.LINK_TEXT, u'关闭')  # 关闭
    # Assertion_elm15 = (By.LINK_TEXT, u'取消')  # 取消
    Assertion_elm16 = (By.LINK_TEXT, u'确定')  # 确定
    Assertion_elm22 = (By.CLASS_NAME, 'pagination-info')  # 获取记录
    Assertion_elm131 = (By.CLASS_NAME, 'tooltip-content')  # 货品名称重复提示
    '''货品类别设置'''
    Assertion_elm12 = (By.XPATH, '//div[2]/div[3]/div/div/div[2]/div[2]/\
    div/div[2]/div[1]/div/div[1]/table/tbody/tr/td/a/span')  # 添加货品类别
    Assertion_elm13 = (By.XPATH, '//div[5]/div[2]/div[2]/div/form/div/span/input[1]')  # 货品类别名称
    Assertion_elm17 = (By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/\
    div[2]/div[1]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/div')#货品类别状态
    Assertion_elm18=(By.XPATH,"//tr[@id='datagrid-row-r3-2-0']/td[4]/div/dt/img")#操作按钮
    Assertion_elm19=(By.XPATH,"//div[@id='baseMenu']/div[1]/div[1]")#编辑按钮
    Assertion_elm20=(By.XPATH,'//div[6]/div[2]/div[2]/div/form/div/span/input[1]')#编辑货品类别
    Assertion_elm21=(By.XPATH,"//div[@id='baseMenu']/div[2]/div[1]")#货品列表禁用或启用
    Assertion_elm23=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/\
    div[1]/div/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/div')#货品类别名称文本
    '''包装设置'''
    Assertion_elm24=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/\
    table/tbody/tr/td/a/span/span[1]')#添加包装
    Assertion_elm25=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div/span/input[1]')#包装类型名称
    Assertion_elm26=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/\
    div[2]/div[2]/table/tbody/tr/td[1]/div')#包装类型名称文本
    Assertion_elm27=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/\
    div[2]/div[2]/table/tbody/tr/td[2]/div')#包装状态文本
    Assertion_elm28=(By.XPATH,"//tr[@id='datagrid-row-r6-2-0']/td[4]/div/dt/img")#包装操作按钮
    Assertion_elm29=(By.XPATH,"//div[@id='baseMenu']/div[1]/div[1]")#编辑包装
    Assertion_elm30=(By.XPATH,'//div[6]/div[2]/div[2]/div/form/div/span/input[1]')#编辑包装类型
    Assertion_elm31=(By.XPATH,"//div[@id='baseMenu']/div[2]/div[1]")#包装禁用或启用
    '''SKU设置'''
    Assertion_elm32=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/\
    div[2]/div[1]/div/div[1]/table/tbody/tr/td/a/span/span[1]')#新增SKU
    Assertion_elm33=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[1]/span/input[1]')#编码
    Assertion_elm34=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[2]/span/input[1]')#品名
    Assertion_elm35=(By.XPATH,"//form[@id='addSkuForm']/div[3]/span/span/a")#下拉按钮
    Assertion_elm36=(By.XPATH,'//div[8]/div/div[1]')#下拉选项
    Assertion_elm37=(By.XPATH,"//form[@id='addSkuForm']/div[4]/span/span/a")#下拉按钮
    Assertion_elm38=(By.XPATH,'//div[9]/div/div[1]')#下拉选项
    Assertion_elm39=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[5]/span/input[1]')#计量单位
    Assertion_elm40=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[6]/span/input[1]')#单价
    Assertion_elm41=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[7]/span/textarea')#规格
    Assertion_elm42=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/\
    div/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/div')#SKU名称文本
    Assertion_elm43=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/\
    div/div[2]/div[2]/div[2]/table/tbody/tr/td[8]/div')#SKU状态本文
    Assertion_elm44=(By.XPATH,"//tr[@id='datagrid-row-r6-2-0']/td[9]/div/dt/img")#SKU操作按钮
    Assertion_elm45=(By.XPATH,"//div[@id='baseMenu']/div[1]/div[1]")#编辑SKU
    Assertion_elm46=(By.XPATH,'//div[6]/div[2]/div[2]/div/form/div[1]/span/input[1]')#编辑SKU名称
    Assertion_elm47=(By.XPATH,"//div[@id='baseMenu']/div[2]/div[1]")#禁用或启用
    '''库区类别管理'''
    Assertion_elm48=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/\
    div/div[1]/table/tbody/tr/td/a/span/span[1]')#添加库区类别
    Assertion_elm49=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div/span/input[1]')#库区类型
    Assertion_elm50=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/\
    div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/div')#库区类型名称文本
    Assertion_elm51=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/\
    div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/div')#库区类型状态文本
    Assertion_elm52=(By.XPATH,"//tr[@id='datagrid-row-r6-2-0']/td[3]/div/dt/img")#库区类型操作按钮
    Assertion_elm53=(By.XPATH,"//div[@id='baseMenu']/div[1]/div[1]")#编辑库区按钮
    Assertion_elm54=(By.XPATH,'//div[6]/div[2]/div[2]/div/form/div/span/input[1]')#编辑库区类型
    Assertion_elm55=(By.XPATH,"//div[@id='baseMenu']/div[2]/div[1]")#禁用或启用库区类型
    '''库区管理'''
    Assertion_elm56=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/\
    div/div[1]/table/tbody/tr/td/a/span/span[1]')#添加库区
    Assertion_elm57=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[1]/span/input[1]')#库区名称
    Assertion_elm58=(By.XPATH,"//form[@id='addWarehouseForm']/div[2]/span/span/a")#下拉按钮
    Assertion_elm59=(By.XPATH,'//div[8]/div/div[1]')#下拉选项
    Assertion_elm60=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[3]/span/input[1]')#负责人
    Assertion_elm61=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[4]/span/input[1]')#联系方式
    Assertion_elm62=(By.XPATH,"//form[@id='addWarehouseForm']/div[5]/span/span/a")#选择省下拉按钮
    Assertion_elm63=(By.XPATH,'//div[9]/div/div[1]')#下拉选项
    Assertion_elm64=(By.XPATH,"//form[@id='addWarehouseForm']/div[6]/span/span/a")#选择市下拉按钮
    Assertion_elm65=(By.XPATH,'//div[10]/div/div')#下拉选项
    Assertion_elm66=(By.XPATH,"//form[@id='addWarehouseForm']/div[7]/span/span/a")#选择县下拉按钮
    Assertion_elm67=(By.XPATH,'//div[11]/div/div[3]')#下拉选项
    Assertion_elm68=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[8]/span/textarea')#街道地址
    Assertion_elm69=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/\
    div[1]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/div')#库区名称文本
    Assertion_elm70=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/\
    div[1]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[6]/div')#库区状态文本
    Assertion_elm71=(By.XPATH,"//tr[@id='datagrid-row-r6-2-0']/td[7]/div/dt/img")#库区操作按钮
    Assertion_elm72=(By.XPATH,"//div[@id='baseMenu']/div[1]/div[1]")#编辑库区
    Assertion_elm73=(By.XPATH,'//div[6]/div[2]/div[2]/div/form/div[1]/span/input[1]')#编辑库区名称
    Assertion_elm74=(By.XPATH,"//div[@id='baseMenu']/div[2]/div[1]")#禁用或启用库区
    '''供应商管理'''
    Assertion_elm75=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/\
    div[1]/div/div[1]/table/tbody/tr/td/a/span')#添加供应商
    Assertion_elm76=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[1]/span/input[1]')#供应商名称
    Assertion_elm77=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[2]/span/input[1]')#联系人
    Assertion_elm78=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[3]/span/input[1]')#联系方式
    Assertion_elm79=(By.XPATH,"//form[@id='addSupplierForm']/div[4]/span/span/a")#选择省下拉按钮
    Assertion_elm80=(By.XPATH,'//div[8]/div/div[1]')#下拉选项
    Assertion_elm81=(By.XPATH,"//form[@id='addSupplierForm']/div[5]/span/span/a")#选择市下拉按钮
    Assertion_elm82=(By.XPATH,'//div[9]/div/div')#下拉选项
    Assertion_elm83=(By.XPATH,"//form[@id='addSupplierForm']/div[6]/span/span/a")#选择县下拉按钮
    Assertion_elm84=(By.XPATH,'//div[10]/div/div[1]')#下拉选项
    Assertion_elm85=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[7]/span/textarea')#街道地址
    Assertion_elm86=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[8]/span/textarea')#备注
    Assertion_elm87=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/\
    div/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/div')#供应商名称文本
    Assertion_elm88=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/\
    div/div[2]/div[2]/div[2]/table/tbody/tr/td[5]/div')#供应商状态文本
    Assertion_elm89=(By.XPATH,"//tr[@id='datagrid-row-r6-2-0']/td[7]/div/dt/img")#供应商操作按钮
    Assertion_elm90=(By.XPATH,"//div[@id='baseMenu']/div[1]/div[1]")#编辑供应商
    Assertion_elm91=(By.XPATH,'//div[6]/div[2]/div[2]/div/form/div[1]/span/input[1]')#编辑供应商名称
    Assertion_elm92=(By.XPATH,"//div[@id='baseMenu']/div[2]/div[1]")#禁用或启用供应商
    '''客户信息管理'''
    Assertion_elm93=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/\
    div/div[1]/table/tbody/tr/td/a/span/span[1]')#添加客户
    Assertion_elm94=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[1]/span/input[1]')#客户名称
    Assertion_elm95=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[2]/span/input[1]')#联系人
    Assertion_elm96=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[3]/span/input[1]')#联系方式
    Assertion_elm97=(By.XPATH,"//form[@id='addCustomerForm']/div[4]/span/span/a")#选择省下拉按钮
    Assertion_elm98=(By.XPATH,'//div[8]/div/div[1]')#下拉选项
    Assertion_elm99=(By.XPATH,"//form[@id='addCustomerForm']/div[5]/span/span/a")#选择市下拉按钮
    Assertion_elm100=(By.XPATH,'//div[9]/div/div')#下拉选项
    Assertion_elm101=(By.XPATH,"//form[@id='addCustomerForm']/div[6]/span/span/a")#选择县下拉按钮
    Assertion_elm102=(By.XPATH,'//div[10]/div/div[4]')#下拉选项
    Assertion_elm103=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[7]/span/textarea')#街道地址
    Assertion_elm104=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[8]/span/textarea')#备注
    Assertion_elm105=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/\
    div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/div')#客户名称文本
    Assertion_elm106=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/\
    div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[5]/div')#客户状态文本
    Assertion_elm107=(By.XPATH,"//tr[@id='datagrid-row-r6-2-0']/td[7]/div/dt/img")#客户操作按钮
    Assertion_elm108=(By.XPATH,"//div[@id='baseMenu']/div[1]/div[1]")#编辑客户按钮
    Assertion_elm130=(By.XPATH,'//div[6]/div[2]/div[2]/div/form/div[1]/span/input[1]')#编辑客户名称 
    Assertion_elm109=(By.XPATH,"//div[@id='baseMenu']/div[2]/div[2]")#禁用或启用客户
    '''合同管理'''
    Assertion_elm110=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/\
    div/div[1]/table/tbody/tr/td/a/span/span[1]')#添加合同
    Assertion_elm111=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[1]/span/input[1]')#合同名称
    Assertion_elm112=(By.XPATH,'//div[5]/div[2]/div[2]/div/form/div[2]/span/input[1]')#合同编号
    Assertion_elm113=(By.XPATH,"//form[@id='addContractForm']/div[3]/span/span/a")#合同类型下拉按钮
    Assertion_elm114=(By.XPATH,'//div[9]/div/div[1]')#供应商选项
    Assertion_elm115=(By.XPATH,'//div[9]/div/div[2]')#客户选项
    Assertion_elm116=(By.XPATH,"//form[@id='addContractForm']/div[4]/span/span/a")#合同对象下拉按钮
    Assertion_elm117=(By.XPATH,'//div[10]/div/div[1]')#下拉选项
    Assertion_elm118=(By.XPATH,"//form[@id='addContractForm']/div[5]/span/span/a")#时间下拉按钮
    Assertion_elm119=(By.LINK_TEXT,u'今天')#下拉选项
    Assertion_elm120=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/\
    div[1]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/div')#合同名称文本
    Assertion_elm121=(By.XPATH,'//div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/\
    div[1]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[6]/div')#合同状态文本
    Assertion_elm122=(By.XPATH,"//tr[@id='datagrid-row-r6-2-0']/td[7]/div/dt/img")#合同操作按钮
    Assertion_elm123=(By.XPATH,"//div[@id='baseMenu']//div[.='编辑']")#编辑合同
    Assertion_elm124=(By.XPATH,'//div[6]/div[2]/div[2]/div/form/div[1]/span/input[1]')#编辑合同名称
    Assertion_elm125=(By.XPATH,"//div[@id='baseMenu']/div[2]/div[1]")#禁用或启用合同
    Assertion_elm126=(By.XPATH,"//div[@id='baseMenu']/div[3]/div[1]")#附件管理
    Assertion_elm127=(By.XPATH,'//div[6]/div[2]/div/div[1]/div[2]/div[1]/a/span/span[1]')#添加附件
    Assertion_elm128=(By.XPATH,'//div[10]/div[2]/div[2]/div/form/div[1]/span/input[1]')#附件名称
    Assertion_elm129=(By.XPATH,'//div[10]/div[2]/div[2]/div/form/div[2]/span/a/label')#选择文件





    def assertion_test1(self):
        self.click(self.Assertion_elm1)
    def assertion_test2(self):
        self.click(self.Assertion_elm2)
    def assertion_test8(self):  #获取记录文本
        return self.driver.find_element(*self.Assertion_elm22).text
    def assertion_test54(self):  #名称重复文本
        return self.driver.find_element(*self.Assertion_elm131).text

    '''货品类别设置'''
    def assertion_test3(self,data,data1):#添加货品类别
        self.click(self.Assertion_elm12)
        self.send_keys(self.Assertion_elm13,data)
        time.sleep(0.5)
        self.click(self.Assertion_elm14)
        try:
            Data = self.assertion_test54()
            if Data == u'货品类别已存在，请重新输入！':
                self.send_keys(self.Assertion_elm20, data1)
                time.sleep(0.5)
                self.click(self.Assertion_elm14)
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
        except:
            time.sleep(0.5)
            self.click(self.Assertion_elm16)
    def assertion_test4(self,data,data1):  #编辑货品类别
        try:
            self.driver.find_element(*self.Assertion_elm18).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm18)
            self.click(self.Assertion_elm19)
            self.send_keys(self.Assertion_elm20,data)
            time.sleep(0.5)
            self.click(self.Assertion_elm14)
            try:
                Data = self.assertion_test54()
                if Data==u'货品类别已存在，请重新输入！':
                    self.send_keys(self.Assertion_elm20, data1)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm14)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm16)
            except:
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
    def assertion_test5(self):  #禁用货品类别或启用
        try:
            self.driver.find_element(*self.Assertion_elm18).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm18)
            self.click(self.Assertion_elm21)
            self.click(self.Assertion_elm16)
            self.click(self.Assertion_elm16)
    def assertion_test7(self):  #货品类别状态文本
        return self.driver.find_element(*self.Assertion_elm17).text
    def assertion_test9(self):  #货品类别名称文本
         data=self.driver.find_elements(*self.Assertion_elm23)
         data1=[]
         for i in data:
            data1.append(i.text)
         return data1
    def assertion_test10(self):  # 进入货品类别
        time.sleep(0.5)
        self.click(self.Assertion_elm3)
        self.click(self.Assertion_elm4)
        time.sleep(0.5)

    '''包装设置'''
    def assertion_test11(self):#进入包装设置
        time.sleep(0.5)
        self.click(self.Assertion_elm3)
        self.click(self.Assertion_elm5)
        time.sleep(0.8)
    def assertion_test12(self,data,data1):#添加包装
        self.click(self.Assertion_elm24)
        self.send_keys(self.Assertion_elm25,data)
        time.sleep(0.5)
        self.click(self.Assertion_elm14)
        try:
            Data = self.assertion_test54()
            if Data == u'包装已存在，请重新输入！':
                self.send_keys(self.Assertion_elm25, data1)
                time.sleep(0.5)
                self.click(self.Assertion_elm14)
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
        except:
            time.sleep(0.5)
            self.click(self.Assertion_elm16)
    def assertion_test13(self):#包装类型名称文本
        return self.driver.find_element(*self.Assertion_elm26).text
    def assertion_test14(self):#包装类型状态文本
        return self.driver.find_element(*self.Assertion_elm27).text
    def assertion_test15(self,data,data1):#编辑包装类型
        try:
            self.driver.find_element(*self.Assertion_elm28).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm28)
            self.click(self.Assertion_elm29)
            self.send_keys(self.Assertion_elm30,data)
            time.sleep(0.5)
            self.click(self.Assertion_elm14)
            try:
                Data = self.assertion_test54()
                if Data == u'包装已存在，请重新输入！':
                    self.send_keys(self.Assertion_elm30, data1)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm14)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm16)
            except:
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
    def assertion_test16(self):#禁用或启用包装类型
        try:
            self.driver.find_element(*self.Assertion_elm28).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm28)
            self.click(self.Assertion_elm31)
            self.click(self.Assertion_elm16)
            self.click(self.Assertion_elm16)

    '''SKU设置'''
    def assertion_test17(self):#进入SKU设置
        time.sleep(0.5)
        self.click(self.Assertion_elm3)
        self.click(self.Assertion_elm6)
        time.sleep(0.5)
    def assertion_test18(self,data1,data2,data3,data4,data5,data6,data7):#新增SKU
        self.click(self.Assertion_elm32)
        self.send_keys(self.Assertion_elm33,data1)
        self.send_keys(self.Assertion_elm34,data2)
        self.click(self.Assertion_elm35)
        self.click(self.Assertion_elm36)
        self.click(self.Assertion_elm37)
        self.click(self.Assertion_elm38)
        self.send_keys(self.Assertion_elm39,data3)
        self.send_keys(self.Assertion_elm40,data4)
        self.send_keys(self.Assertion_elm41,data5)
        time.sleep(0.5)
        self.click(self.Assertion_elm14)
        try:
            Data = self.assertion_test54()
            if Data == u'货品编码已存在，请重新输入！':
                self.send_keys(self.Assertion_elm33,data6)
                time.sleep(0.5)
                self.click(self.Assertion_elm14)
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
            elif Data == u'品名已存在，请重新输入！':
                self.send_keys(self.Assertion_elm34, data7)
                time.sleep(0.5)
                self.click(self.Assertion_elm14)
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
        except:
            time.sleep(0.5)
            self.click(self.Assertion_elm16)
    def assertion_test19(self):#SKU名称文本
        return self.driver.find_element(*self.Assertion_elm42).text
    def assertion_test20(self):#SKU状态文本
        return self.driver.find_element(*self.Assertion_elm43).text
    def assertion_test21(self,data,data1):#编辑SKU
        try:
            self.driver.find_element(*self.Assertion_elm44).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm44)
            self.click(self.Assertion_elm45)
            self.send_keys(self.Assertion_elm46,data)
            time.sleep(0.5)
            self.click(self.Assertion_elm14)
            try:
                Data = self.assertion_test54()
                if Data == u'货品编码已存在，请重新输入！':
                    self.send_keys(self.Assertion_elm46, data1)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm14)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm16)
            except:
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
    def assertion_test22(self):#禁用或启用SKU
        try:
            self.driver.find_element(*self.Assertion_elm44).is_displayed()
        except:
            print ('No data！！！')
        else:
            time.sleep(0.5)
            self.click(self.Assertion_elm44)
            self.click(self.Assertion_elm47)
            self.click(self.Assertion_elm16)
            self.click(self.Assertion_elm16)


    '''库区类别管理'''
    def assertion_test23(self):#进入库区类别管理
        time.sleep(0.5)
        self.click(self.Assertion_elm3)
        self.click(self.Assertion_elm7)
        time.sleep(0.5)
    def assertion_test24(self,data,data1):#添加库区类别
        self.click(self.Assertion_elm48)
        self.send_keys(self.Assertion_elm49,data)
        time.sleep(0.5)
        self.click(self.Assertion_elm14)
        try:
            Data = self.assertion_test54()
            if Data == u'库区类型已存在，请重新输入！':
                self.send_keys(self.Assertion_elm49, data1)
                time.sleep(0.5)
                self.click(self.Assertion_elm14)
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
        except:
            self.click(self.Assertion_elm16)
    def assertion_test25(self):#库区类别名称文本
        return self.driver.find_element(*self.Assertion_elm50).text
    def assertion_test26(self):  # 库区类别状态文本
        return self.driver.find_element(*self.Assertion_elm51).text
    def assertion_test27(self,data,data1):  # 编辑库区类别
        try:
            self.driver.find_element(*self.Assertion_elm52).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm52)
            self.click(self.Assertion_elm53)
            self.send_keys(self.Assertion_elm54,data)
            time.sleep(0.5)
            self.click(self.Assertion_elm14)
            try:
                Data = self.assertion_test54()
                if Data == u'库区类型已存在，请重新输入！':
                    self.send_keys(self.Assertion_elm54, data1)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm14)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm16)
            except:
                self.click(self.Assertion_elm16)
    def assertion_test28(self):  # 禁用或启用库区类型
        try:
            self.driver.find_element(*self.Assertion_elm52).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm52)
            self.click(self.Assertion_elm55)
            time.sleep(0.5)
            self.click(self.Assertion_elm16)
            time.sleep(0.5)
            self.click(self.Assertion_elm16)


    '''库区管理'''
    def assertion_test29(self):#进入库区管理
        time.sleep(0.5)
        self.click(self.Assertion_elm3)
        self.click(self.Assertion_elm8)
        time.sleep(0.5)
    def assertion_test30(self,data,data1,data2,data3,data4):#添加库区
        self.click(self.Assertion_elm56)
        self.send_keys(self.Assertion_elm57,data)
        self.click(self.Assertion_elm58)
        self.click(self.Assertion_elm59)
        self.send_keys(self.Assertion_elm60,data1)
        self.send_keys(self.Assertion_elm61,data2)
        self.click(self.Assertion_elm62)
        self.click(self.Assertion_elm63)
        self.click(self.Assertion_elm64)
        self.click(self.Assertion_elm65)
        self.click(self.Assertion_elm66)
        self.click(self.Assertion_elm67)
        self.send_keys(self.Assertion_elm68,data3)
        time.sleep(0.5)
        self.click(self.Assertion_elm14)
        try:
            Data = self.assertion_test54()
            if Data == u'库区名称已存在，请重新输入！':
                self.send_keys(self.Assertion_elm57, data4)
                time.sleep(0.5)
                self.click(self.Assertion_elm14)
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
        except:
            self.click(self.Assertion_elm16)
    def assertion_test31(self):#库区名称文本
        return self.driver.find_element(*self.Assertion_elm69).text
    def assertion_test32(self):  # 库区状态文本
        return self.driver.find_element(*self.Assertion_elm70).text
    def assertion_test33(self,data,data1):  # 编辑库区名称
        try:
            self.driver.find_element(*self.Assertion_elm71).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm71)
            self.click(self.Assertion_elm72)
            self.send_keys(self.Assertion_elm73,data)
            time.sleep(0.5)
            self.click(self.Assertion_elm14)
            try:
                Data = self.assertion_test54()
                if Data == u'库区名称已存在，请重新输入！':
                    self.send_keys(self.Assertion_elm73, data1)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm14)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm16)
            except:
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
    def assertion_test34(self):  # 禁用或启用库区
        try:
            self.driver.find_element(*self.Assertion_elm71).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm71)
            self.click(self.Assertion_elm74)
            time.sleep(0.5)
            self.click(self.Assertion_elm16)
            time.sleep(0.5)
            self.click(self.Assertion_elm16)

    '''供应商管理'''
    def assertion_test35(self):#进入供应商管理
        time.sleep(0.5)
        self.click(self.Assertion_elm3)
        self.click(self.Assertion_elm9)
        time.sleep(0.5)
    def assertion_test36(self,data,data1,data2,data3,data4,data5):#添加供应商
        self.click(self.Assertion_elm75)
        self.send_keys(self.Assertion_elm76,data)
        self.send_keys(self.Assertion_elm77,data1)
        self.send_keys(self.Assertion_elm78,data2)
        self.click(self.Assertion_elm79)
        self.click(self.Assertion_elm80)
        self.click(self.Assertion_elm81)
        self.click(self.Assertion_elm82)
        self.click(self.Assertion_elm83)
        self.click(self.Assertion_elm84)
        self.send_keys(self.Assertion_elm85,data3)
        self.send_keys(self.Assertion_elm86,data4)
        time.sleep(0.5)
        self.click(self.Assertion_elm14)
        try:
            Data = self.assertion_test54()
            if Data == u'供应商名称已存在，请重新输入！':
                self.send_keys(self.Assertion_elm76, data5)
                time.sleep(0.5)
                self.click(self.Assertion_elm14)
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
        except:
            time.sleep(0.5)
            self.click(self.Assertion_elm16)
    def assertion_test37(self):#供应商名称文本
        return self.driver.find_element(*self.Assertion_elm87).text
    def assertion_test38(self):  # 供应商状态文本
        return self.driver.find_element(*self.Assertion_elm88).text
    def assertion_test39(self,data,data1):  # 编辑供应商名称
        try:
            self.driver.find_element(*self.Assertion_elm89).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm89)
            self.click(self.Assertion_elm90)
            self.send_keys(self.Assertion_elm91,data)
            time.sleep(0.5)
            self.click(self.Assertion_elm14)
            try:
                Data = self.assertion_test54()
                if Data == u'供应商名称已存在，请重新输入！':
                    self.send_keys(self.Assertion_elm91, data1)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm14)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm16)
            except:
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
    def assertion_test40(self):  # 禁用或启用供应商
        try:
            self.driver.find_element(*self.Assertion_elm89).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm89)
            self.click(self.Assertion_elm92)
            self.click(self.Assertion_elm16)
            self.click(self.Assertion_elm16)

    '''客户信息管理'''
    def assertion_test41(self):#进入客户信息管理
        time.sleep(0.5)
        self.click(self.Assertion_elm3)
        self.click(self.Assertion_elm10)
        time.sleep(0.5)
    def assertion_test42(self,data,data1,data2,data3,data4,data5):#添加客户信息
        self.click(self.Assertion_elm93)
        self.send_keys(self.Assertion_elm94,data)
        self.send_keys(self.Assertion_elm95,data1)
        self.send_keys(self.Assertion_elm96,data2)
        self.click(self.Assertion_elm97)
        self.click(self.Assertion_elm98)
        self.click(self.Assertion_elm99)
        self.click(self.Assertion_elm100)
        self.click(self.Assertion_elm101)
        self.click(self.Assertion_elm102)
        self.send_keys(self.Assertion_elm103,data3)
        self.send_keys(self.Assertion_elm104,data4)
        time.sleep(0.5)
        self.click(self.Assertion_elm14)
        try:
            Data = self.assertion_test54()
            if Data == u'客户名称已存在，请重新输入！':
                self.send_keys(self.Assertion_elm94, data5)
                time.sleep(0.5)
                self.click(self.Assertion_elm14)
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
        except:
            time.sleep(0.5)
            self.click(self.Assertion_elm16)
    def assertion_test43(self):#客户信息名称文本
        return self.driver.find_element(*self.Assertion_elm105).text
    def assertion_test44(self):  # 客户信息状态文本
        return self.driver.find_element(*self.Assertion_elm106).text
    def assertion_test45(self,data,data1):  # 编辑客户信息
        try:
            self.driver.find_element(*self.Assertion_elm107).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm107)
            self.click(self.Assertion_elm108)
            self.send_keys(self.Assertion_elm130,data)
            time.sleep(0.5)
            self.click(self.Assertion_elm14)
            try:
                Data = self.assertion_test54()
                if Data == u'客户名称已存在，请重新输入！':
                    self.send_keys(self.Assertion_elm130, data1)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm14)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm16)
            except:
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
    def assertion_test46(self):  # 禁用或启用客户信息
        try:
            self.driver.find_element(*self.Assertion_elm107).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm107)
            self.click(self.Assertion_elm109)
            self.click(self.Assertion_elm16)
            self.click(self.Assertion_elm16)

    '''合同管理'''
    def assertion_test47(self):#进入合同管理
        time.sleep(0.5)
        self.click(self.Assertion_elm3)
        self.click(self.Assertion_elm11)
        time.sleep(0.5)
    def assertion_test48(self,data,data1,data2,data3):#添加供应商合同
        self.click(self.Assertion_elm110)
        self.send_keys(self.Assertion_elm111,data)
        self.send_keys(self.Assertion_elm112,data1)
        self.click(self.Assertion_elm113)
        self.click(self.Assertion_elm114)
        self.click(self.Assertion_elm116)
        self.click(self.Assertion_elm117)
        self.click(self.Assertion_elm118)
        self.click(self.Assertion_elm119)
        self.click(self.Assertion_elm14)
        try:
            Data = self.assertion_test54()
            if Data == u'合同名称已存在，请重新输入！':
                self.send_keys(self.Assertion_elm111, data2)
                time.sleep(0.5)
                self.click(self.Assertion_elm14)
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
                if Data == u'合同编号已存在，请重新输入！':
                    self.send_keys(self.Assertion_elm112, data3)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm14)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm16)
                else:
                    pass
        except:
            time.sleep(0.5)
            self.click(self.Assertion_elm16)
    def assertion_test49(self,data,data1,data2,data3):#添加客户合同
        self.click(self.Assertion_elm110)
        self.send_keys(self.Assertion_elm111,data)
        self.send_keys(self.Assertion_elm112,data1)
        self.click(self.Assertion_elm113)
        self.click(self.Assertion_elm115)
        self.click(self.Assertion_elm116)
        self.click(self.Assertion_elm117)
        self.click(self.Assertion_elm118)
        self.click(self.Assertion_elm119)
        self.click(self.Assertion_elm14)
        try:
            Data = self.assertion_test54()
            if Data == u'合同名称已存在，请重新输入！':
                self.send_keys(self.Assertion_elm111, data2)
                time.sleep(0.5)
                self.click(self.Assertion_elm14)
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
                if Data == u'合同编号已存在，请重新输入！':
                    self.send_keys(self.Assertion_elm112, data3)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm14)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm16)
                else:
                    pass
        except:
            time.sleep(0.5)
            self.click(self.Assertion_elm16)
    def assertion_test50(self):#合同名称文本
        return self.driver.find_element(*self.Assertion_elm120).text
    def assertion_test51(self):  # 合同状态文本
        return self.driver.find_element(*self.Assertion_elm121).text
    def assertion_test52(self,data,data1):  # 编辑合同信息
        try:
            self.driver.find_element(*self.Assertion_elm122).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm122)
            self.click(self.Assertion_elm123)
            self.send_keys(self.Assertion_elm124,data)
            time.sleep(0.5)
            self.click(self.Assertion_elm14)
            try:
                Data = self.assertion_test54()
                if Data == u'合同名称已存在，请重新输入！':
                    self.send_keys(self.Assertion_elm124, data1)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm14)
                    time.sleep(0.5)
                    self.click(self.Assertion_elm16)
            except:
                time.sleep(0.5)
                self.click(self.Assertion_elm16)
    def assertion_test53(self):  # 禁用或启用合同
        try:
            self.driver.find_element(*self.Assertion_elm122).is_displayed()
        except:
            print ('No data！！！')
        else:
            self.click(self.Assertion_elm122)
            self.click(self.Assertion_elm125)
            self.click(self.Assertion_elm16)
            self.click(self.Assertion_elm16)

    # def assertion_test23(self):#合同管理操作
    #     pass
