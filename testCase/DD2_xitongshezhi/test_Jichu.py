# # coding:utf-8
#
# import unittest,sys
# from GYL_project.Base_page.DriverPage import browser
# from GYL_project.Base_page.System_settingsPage.JichuPage import Jichu
# from GYL_project.common import read_Data
# from GYL_project.common.logger import Log
# from GYL_project.common.Screen import Screenshot
# from GYL_project.common import Global_function
# from GYL_project.common.Global_function import login_url
# from random import randint
# import time as t
# testData=randint(1,50)
# testData1=randint(1,50)
# testData2=str(180)+str(randint(10000000,99999999))
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
#
# class JiChu(unittest.TestCase):
#     log = Log()
#     @classmethod
#     def setUpClass(cls):
#         driver = browser()
#         cls.JC = Jichu(cls.driver)
#         cls.JC.open(login_url, u'登录')
#         cls.driver.implicitly_wait(5)
#         Global_function.login(cls)
#         cls.JC.assertion_test1()
#         cls.JC.assertion_test2()
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#
#     '''
#     货品类别设置
#     '''
#     @Screenshot(driver)
#     def test_JCXXWH1(self):
#         '''
#
#         :添加货品类别
#         :return:
#         '''
#         self.log.info('------添加货品类别：start!---------')
#         data = self.JC.assertion_test8()
#         try:
#             data1 = int(data[11]) + 1
#         except:
#             Data2 = data[12:14]
#             data2 = int(Data2) + 1
#         self.JC.assertion_test3(read_Data.getExcel2(testData,2))
#         data3 = self.JC.assertion_test8()
#         try:
#             data31 = int(data3[11])
#             self.assertEqual(data1, data31)
#         except:
#             Data3 = int(data3[12:14])
#             self.assertEqual(Data3, data2)
#         self.log.info('------添加货品类别：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH2(self):
#         '''
#
#         :编辑货品类别
#         :return:
#         '''
#         self.log.info('------编辑货品类别：start!---------')
#         self.JC.assertion_test4(read_Data.getExcel2(testData1,2))
#         self.assertEqual(self.JC.assertion_test9(),read_Data.getExcel2(testData1,2))
#         self.log.info('------编辑货品类别：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH3(self):
#         '''
#
#         :禁用货品类别
#         :return:
#         '''
#         self.log.info('------禁用货品类别：start!---------')
#         self.JC.assertion_test10()
#         data=self.JC.assertion_test7()
#         if data==read_Data.getExcel2(6,6):
#             self.JC.assertion_test5()
#         else:
#             self.JC.assertion_test5()
#             self.JC.assertion_test5()
#         self.assertEqual(self.JC.assertion_test7(), read_Data.getExcel2(11, 6))
#         self.log.info('------禁用货品类别：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH4(self):
#         '''
#
#         :启用货品类别
#         :return:
#         '''
#         self.log.info('------启用货品类别：start!---------')
#         self.JC.assertion_test10()
#         data = self.JC.assertion_test7()
#         if data == read_Data.getExcel2(11, 6):
#             self.JC.assertion_test5()
#         else:
#             self.JC.assertion_test5()
#             self.JC.assertion_test5()
#         self.assertEqual(self.JC.assertion_test7(), read_Data.getExcel2(6, 6))
#         self.log.info('------启用货品类别：stop!---------')
#
#     '''
#     包装设置
#     '''
#     @Screenshot(driver)
#     def test_JCXXWH5(self):
#         '''
#
#         :添加包装类型
#         :return:
#         '''
#         self.log.info('------添加包装类型：start!---------')
#         self.JC.assertion_test11()
#         data = self.JC.assertion_test8()
#         try:
#             data1 = int(data[11]) + 1
#         except:
#             Data2 = data[12:14]
#             data2 = int(Data2) + 1
#         self.JC.assertion_test12(read_Data.getExcel2(testData,2))
#         data3 = self.JC.assertion_test8()
#         try:
#             data31 = int(data3[11])
#             self.assertEqual(data1, data31)
#         except:
#             Data3 = int(data3[12:14])
#             self.assertEqual(Data3, data2)
#         self.log.info('------添加包装类型：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH6(self):
#         '''
#
#         :编辑包装类型
#         :return:
#         '''
#         self.log.info('------编辑包装类型：start!---------')
#         self.JC.assertion_test11()
#         self.JC.assertion_test15(read_Data.getExcel2(testData1, 2))
#         self.assertNotEqual(self.JC.assertion_test13(), read_Data.getExcel2(testData1, 2))
#         self.log.info('------编辑包装类型：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH7(self):
#         '''
#
#         :禁用包装类型
#         :return:
#         '''
#         self.log.info('------禁用包装类型：start!---------')
#         self.JC.assertion_test11()
#         data = self.JC.assertion_test14()
#         if data == read_Data.getExcel2(6, 6):
#             self.JC.assertion_test16()
#         else:
#             self.JC.assertion_test16()
#             self.JC.assertion_test16()
#         self.assertEqual(self.JC.assertion_test7(), read_Data.getExcel2(11, 6))
#         self.log.info('------禁用包装类型：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH8(self):
#         '''
#
#         :启用包装类型
#         :return:
#         '''
#         self.log.info('------启用包装类型：start!---------')
#         self.JC.assertion_test11()
#         data = self.JC.assertion_test14()
#         if data == read_Data.getExcel2(11, 6):
#             self.JC.assertion_test16()
#         else:
#             self.JC.assertion_test16()
#             self.JC.assertion_test16()
#         self.assertEqual(self.JC.assertion_test7(), read_Data.getExcel2(6, 6))
#         self.log.info('------启用包装类型：stop!---------')
#
#     '''
#     SKU设置
#     '''
#     @Screenshot(driver)
#     def test_JCXXWH9(self):
#         '''
#
#         :新增SKU
#         :return:
#         '''
#         self.log.info('------新增SKU：start!---------')
#         self.JC.assertion_test17()
#         data = self.JC.assertion_test8()
#         try:
#             data1 = int(data[11]) + 1
#         except:
#             Data2 = data[12:14]
#             data2 = int(Data2) + 1
#         self.JC.assertion_test18(read_Data.getExcel2(testData,7),
#                                  read_Data.getExcel2(testData1,7),
#                                  read_Data.getExcel2(testData,7),'12345',
#                                  read_Data.getExcel2(testData,7))
#         data3 = self.JC.assertion_test8()
#         try:
#             data31 = int(data3[11])
#             self.assertEqual(data1, data31)
#         except:
#             Data3 = int(data3[12:14])
#             self.assertEqual(Data3, data2)
#         self.log.info('------新增SKU：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH10(self):
#         '''
#
#         :编辑SKU
#         :return:
#         '''
#         self.log.info('------编辑SKU：start!---------')
#         self.JC.assertion_test17()
#         self.JC.assertion_test21(read_Data.getExcel2(testData1, 2))
#         self.assertNotEqual(self.JC.assertion_test19(), read_Data.getExcel2(testData1, 2))
#         self.log.info('------编辑SKU：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH11(self):
#         '''
#
#         :禁用SKU
#         :return:
#         '''
#         self.log.info('------禁用SKU：start!---------')
#         self.JC.assertion_test17()
#         data = self.JC.assertion_test20()
#         if data == read_Data.getExcel2(12, 6):
#             self.JC.assertion_test22()
#         else:
#             self.JC.assertion_test22()
#             self.JC.assertion_test22()
#         self.assertEqual(self.JC.assertion_test20(), read_Data.getExcel2(11, 6))
#         self.log.info('------禁用SKU：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH12(self):
#         '''
#
#         :启用SKU
#         :return:
#         '''
#         self.log.info('------启用SKU：start!---------')
#         self.JC.assertion_test17()
#         data = self.JC.assertion_test20()
#         if data == read_Data.getExcel2(11, 6):
#             self.JC.assertion_test22()
#         else:
#             self.JC.assertion_test22()
#             self.JC.assertion_test22()
#         self.assertEqual(self.JC.assertion_test20(), read_Data.getExcel2(12, 6))
#         self.log.info('------启用SKU：stop!---------')
#
#     '''
#     库区类别管理
#     '''
#     @Screenshot(driver)
#     def test_JCXXWH13(self):
#         '''
#
#         :新增库区类别
#         :return:
#         '''
#         self.log.info('------新增库区类别：start!---------')
#         self.JC.assertion_test23()
#         data = self.JC.assertion_test8()
#         try:
#             data1 = int(data[11]) + 1
#         except:
#             Data2 = data[12:14]
#             data2 = int(Data2) + 1
#         self.JC.assertion_test24(read_Data.getExcel2(testData,1))
#         data3 = self.JC.assertion_test8()
#         try:
#             data31 = int(data3[11])
#             self.assertEqual(data1, data31)
#         except:
#             Data3 = int(data3[12:14])
#             self.assertEqual(Data3, data2)
#         self.log.info('------新增库区类别：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH14(self):
#         '''
#
#         :编辑库区类别
#         :return:
#         '''
#         self.log.info('------编辑库区类别：start!---------')
#         self.JC.assertion_test23()
#         self.JC.assertion_test27(read_Data.getExcel2(testData1, 2))
#         self.assertEqual(self.JC.assertion_test25(), read_Data.getExcel2(testData1, 2))
#         self.log.info('------编辑库区类别：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH15(self):
#         '''
#
#         :禁用库区类别
#         :return:
#         '''
#         self.log.info('------禁用库区类别：start!---------')
#         self.JC.assertion_test23()
#         data = self.JC.assertion_test26()
#         if data == read_Data.getExcel2(12, 6):
#             self.JC.assertion_test28()
#         else:
#             self.JC.assertion_test28()
#             self.JC.assertion_test28()
#         self.assertEqual(self.JC.assertion_test26(), read_Data.getExcel2(11, 6))
#         self.log.info('------禁用库区类别：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH16(self):
#         '''
#
#         :启用库区类别
#         :return:
#         '''
#         self.log.info('------启用库区类别：start!---------')
#         self.JC.assertion_test23()
#         data = self.JC.assertion_test26()
#         if data == read_Data.getExcel2(11, 6):
#             self.JC.assertion_test28()
#         else:
#             self.JC.assertion_test28()
#             self.JC.assertion_test28()
#         self.assertEqual(self.JC.assertion_test26(), read_Data.getExcel2(12, 6))
#         self.log.info('------启用库区类别：stop!---------')
#
#     '''
#     库区管理
#     '''
#     @Screenshot(driver)
#     def test_JCXXWH17(self):
#         '''
#
#         :新增库区
#         :return:
#         '''
#         self.log.info('------新增库区：start!---------')
#         self.JC.assertion_test29()
#         data = self.JC.assertion_test8()
#         try:
#             data1 = int(data[11]) + 1
#         except:
#             Data2 = data[12:14]
#             data2 = int(Data2) + 1
#         self.JC.assertion_test30(read_Data.getExcel2(testData,0),
#                                  read_Data.getExcel2(testData,1),testData2,
#                                  read_Data.getExcel2(testData,2))
#         data3 = self.JC.assertion_test8()
#         try:
#             data31 = int(data3[11])
#             self.assertEqual(data1, data31)
#         except:
#             Data3 = int(data3[12:14])
#             self.assertEqual(Data3, data2)
#         self.log.info('------新增库区：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH18(self):
#         '''
#
#         :编辑库区
#         :return:
#         '''
#         self.log.info('------编辑库区：start!---------')
#         self.JC.assertion_test29()
#         self.JC.assertion_test33(read_Data.getExcel2(testData1, 2))
#         self.assertEqual(self.JC.assertion_test31(), read_Data.getExcel2(testData1, 2))
#         self.log.info('------编辑库区：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH19(self):
#         '''
#
#         :禁用库区
#         :return:
#         '''
#         self.log.info('------禁用库区：start!---------')
#         self.JC.assertion_test29()
#         data = self.JC.assertion_test32()
#         if data == read_Data.getExcel2(12, 6):
#             self.JC.assertion_test34()
#         else:
#             self.JC.assertion_test34()
#             self.JC.assertion_test34()
#         self.assertEqual(self.JC.assertion_test32(), read_Data.getExcel2(11, 6))
#         self.log.info('------禁用库区：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH20(self):
#         '''
#
#         :启用库区
#         :return:
#         '''
#         self.log.info('------启用库区：start!---------')
#         self.JC.assertion_test29()
#         data = self.JC.assertion_test32()
#         if data == read_Data.getExcel2(11, 6):
#             self.JC.assertion_test34()
#         else:
#             self.JC.assertion_test34()
#             self.JC.assertion_test34()
#         self.assertEqual(self.JC.assertion_test32(), read_Data.getExcel2(12, 6))
#         self.log.info('------启用库区：stop!---------')
#
#     '''
#     供应商管理
#     '''
#
#     @Screenshot(driver)
#     def test_JCXXWH21(self):
#         '''
#
#         :添加供应商
#         :return:
#         '''
#         self.log.info('------添加供应商：start!---------')
#         self.JC.assertion_test35()
#         data = self.JC.assertion_test8()
#         try:
#             data1 = int(data[11]) + 1
#         except:
#             Data2 = data[12:14]
#             data2 = int(Data2) + 1
#         self.JC.assertion_test36(read_Data.getExcel2(testData,0),
#                                  read_Data.getExcel2(testData,1),testData2,
#                                  read_Data.getExcel2(testData,2),
#                                  read_Data.getExcel2(testData,3))
#         data3 = self.JC.assertion_test8()
#         try:
#             data31 = int(data3[11])
#             self.assertEqual(data1, data31)
#         except:
#             Data3 = int(data3[12:14])
#             self.assertEqual(Data3, data2)
#         self.log.info('------添加供应商：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH22(self):
#         '''
#
#         :编辑供应商
#         :return:
#         '''
#         self.log.info('------编辑供应商：start!---------')
#         self.JC.assertion_test35()
#         self.JC.assertion_test39(read_Data.getExcel2(testData1, 2))
#         self.assertEqual(self.JC.assertion_test37(), read_Data.getExcel2(testData1, 2))
#         self.log.info('------编辑供应商：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH23(self):
#         '''
#
#         :禁用供应商
#         :return:
#         '''
#         self.log.info('------禁用供应商：start!---------')
#         self.JC.assertion_test35()
#         data = self.JC.assertion_test38()
#         if data == read_Data.getExcel2(12, 6):
#             self.JC.assertion_test40()
#         else:
#             self.JC.assertion_test40()
#             self.JC.assertion_test40()
#         self.assertEqual(self.JC.assertion_test38(), read_Data.getExcel2(11, 6))
#         self.log.info('------禁用供应商：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH24(self):
#         '''
#
#         :启用供应商
#         :return:
#         '''
#         self.log.info('------启用供应商：start!---------')
#         self.JC.assertion_test35()
#         data = self.JC.assertion_test38()
#         if data == read_Data.getExcel2(11, 6):
#             self.JC.assertion_test40()
#         else:
#             self.JC.assertion_test40()
#             self.JC.assertion_test40()
#         self.assertEqual(self.JC.assertion_test38(), read_Data.getExcel2(12, 6))
#         self.log.info('------启用供应商：stop!---------')
#
#     '''
#     客户信息管理
#     '''
#     @Screenshot(driver)
#     def test_JCXXWH25(self):
#         '''
#
#         :添加客户信息
#         :return:
#         '''
#         self.log.info('------添加客户信息：start!---------')
#         self.JC.assertion_test41()
#         data = self.JC.assertion_test8()
#         try:
#             data1 = int(data[11]) + 1
#         except:
#             Data2 = data[12:14]
#             data2 = int(Data2) + 1
#         self.JC.assertion_test42(read_Data.getExcel2(testData, 0),
#                                  read_Data.getExcel2(testData, 1), testData2,
#                                  read_Data.getExcel2(testData, 2),
#                                  read_Data.getExcel2(testData, 3))
#         data3 = self.JC.assertion_test8()
#         try:
#             data31 = int(data3[11])
#             self.assertEqual(data1, data31)
#         except:
#             Data3 = int(data3[12:14])
#             self.assertEqual(Data3, data2)
#         self.log.info('------添加客户信息：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH26(self):
#         '''
#
#         :编辑客户信息
#         :return:
#         '''
#         self.log.info('------编辑客户信息：start!---------')
#         self.JC.assertion_test41()
#         self.JC.assertion_test45(read_Data.getExcel2(testData1, 2))
#         self.assertEqual(self.JC.assertion_test43(), read_Data.getExcel2(testData1, 2))
#         self.log.info('------编辑客户信息：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH27(self):
#         '''
#
#         :禁用客户信息
#         :return:
#         '''
#         self.log.info('------禁用客户信息：start!---------')
#         self.JC.assertion_test41()
#         data = self.JC.assertion_test44()
#         if data == read_Data.getExcel2(12, 6):
#             self.JC.assertion_test46()
#         else:
#             self.JC.assertion_test46()
#             self.JC.assertion_test46()
#         self.assertEqual(self.JC.assertion_test44(), read_Data.getExcel2(11, 6))
#         self.log.info('------禁用客户信息：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH28(self):
#         '''
#
#         :启用客户信息
#         :return:
#         '''
#         self.log.info('------启用客户信息：start!---------')
#         self.JC.assertion_test41()
#         data = self.JC.assertion_test44()
#         if data == read_Data.getExcel2(11, 6):
#             self.JC.assertion_test46()
#         else:
#             self.JC.assertion_test46()
#             self.JC.assertion_test46()
#         self.assertEqual(self.JC.assertion_test44(), read_Data.getExcel2(12, 6))
#         self.log.info('------启用客户信息：stop!---------')
#
#     '''
#     合同管理
#     '''
#     @Screenshot(driver)
#     def test_JCXXWH29(self):
#         '''
#
#         :添加供应链合同
#         :return:
#         '''
#         self.log.info('------添加供应链合同：start!---------')
#         self.JC.assertion_test47()
#         data = self.JC.assertion_test8()
#         try:
#             data1 = int(data[11]) + 1
#         except:
#             Data2 = data[12:14]
#             data2 = int(Data2) + 1
#         self.JC.assertion_test48(read_Data.getExcel2(testData,0),
#                                  read_Data.getExcel2(testData,1))
#         data3 = self.JC.assertion_test8()
#         try:
#             data31 = int(data3[11])
#             self.assertEqual(data1, data31)
#         except:
#             Data3 = int(data3[12:14])
#             self.assertEqual(Data3, data2)
#         self.log.info('------添加供应链合同：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH30(self):
#         '''
#
#         :添加客户合同
#         :return:
#         '''
#         self.log.info('------添加客户合同：start!---------')
#         self.JC.assertion_test47()
#         data = self.JC.assertion_test8()
#         try:
#             data1 = int(data[11]) + 1
#         except:
#             Data2 = data[12:14]
#             data2 = int(Data2) + 1
#         self.JC.assertion_test49(read_Data.getExcel2(testData1,0),
#                                  read_Data.getExcel2(testData1,1))
#         data3 = self.JC.assertion_test8()
#         try:
#             data31 = int(data3[11])
#             self.assertEqual(data1, data31)
#         except:
#             Data3 = int(data3[12:14])
#             self.assertEqual(Data3, data2)
#         self.log.info('------添加客户合同：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH31(self):
#         '''
#
#         :编辑合同
#         :return:
#         '''
#         self.log.info('------编辑合同：start!---------')
#         self.JC.assertion_test47()
#         data = self.JC.assertion_test50()
#         self.JC.assertion_test52(read_Data.getExcel2(testData, 2))
#         if self.JC.assertion_test50()==data:
#             print u'合同编辑失败'
#         else:
#             self.assertNotEqual(self.JC.assertion_test50(), read_Data.getExcel2(testData, 2))
#         self.log.info('------编辑合同：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH32(self):
#         '''
#
#         :禁用合同
#         :return:
#         '''
#         self.log.info('------禁用合同：start!---------')
#         self.JC.assertion_test47()
#         data = self.JC.assertion_test51()
#         if data == read_Data.getExcel2(12, 6):
#             self.JC.assertion_test53()
#         else:
#             self.JC.assertion_test53()
#             self.JC.assertion_test53()
#         self.assertEqual(self.JC.assertion_test51(), read_Data.getExcel2(11, 6))
#         self.log.info('------禁用合同：stop!---------')
#
#     @Screenshot(driver)
#     def test_JCXXWH33(self):
#         '''
#
#         :启用合同
#         :return:
#         '''
#         self.log.info('------启用合同：start!---------')
#         self.JC.assertion_test47()
#         data = self.JC.assertion_test51()
#         if data == read_Data.getExcel2(11, 6):
#             self.JC.assertion_test53()
#         else:
#             self.JC.assertion_test53()
#             self.JC.assertion_test53()
#         self.assertEqual(self.JC.assertion_test51(), read_Data.getExcel2(12, 6))
#         self.log.info('------启用合同：stop!---------')
#
# if __name__=='__main__':
#     unittest.main()