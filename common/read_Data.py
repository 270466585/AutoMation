# coding:utf-8

import csv, xlrd
import time as t


def getCsv():
    rows = []
    with open('testDate_csv.csv', 'rb') as f:
        readers = csv.reader(f, delimiter=',', quotechar='|')
        next(readers, None)
        for row in readers:
            rows.append(row)
        return rows


def getExcel1(Value1, Value2, file_name='/Users/Macx/PycharmProjects/GYL_project/testData/DataBase.xlsx'):
    '''

    :param Value1: 表格行
    :param Value2: 表格列
    :param file_name: 文件名
    :return: 
    '''
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    return sheet.cell_value(Value1, Value2)

def getExcel2(Value1, Value2, file_name='/Users/Macx/PycharmProjects/GYL_project/testData/DataBase.xlsx'):
    '''

    :param Value1: 表格行
    :param Value2: 表格列
    :param file_name: 文件名
    :return: 
    '''
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(1)
    return sheet.cell_value(Value1, Value2)


def getDdtEcxel(file_name='/Users/Macx/PycharmProjects/GYL_project/testData/DataBase.xlsx'):
    rows = []
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row, 0, sheet.ncols)))
    return rows

def getExcel3(Value1, Value2, Value3,file_name='/Users/Macx/PycharmProjects/GYL_project/testData/DataBase.xlsx'):
    '''

    :param Value1: 表格行
    :param Value2: 表格列
    :param file_name: 文件名
    :return:
    '''
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(Value1)
    return sheet.cell_value(Value2, Value3)



