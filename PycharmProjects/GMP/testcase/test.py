from selenium import webdriver
import HTMLTestRunner
from pages.searchPage import SearchPage
from selenium.webdriver.common.by import By
import os
import xlrd
import xlwt
from datetime import date,datetime
import time
import datetime
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# cc = ['91 18701296509 201803281541440002 【自动化签名】发送短信 2018-03-28 15:41:44 2018-04-03 18:28:15 成功 2018-04-03 18:28:15 成功 DELIVRD', '92 18701296509 201803271631040262 【自动化签名】嘎嘎嘎 2018-03-27 16:31:04 2018-03-27 16:31:04 成功 2018-03-27 16:31:04 失败 UNDELIV', '93 18701296509 201803271631040261 【自动化签名】嘎嘎嘎 2018-03-27 16:31:04 2018-04-02 17:38:40 成功 2018-04-02 17:38:40 成功 DELIVRD', '94 18701296509 201803271631040260 【自动化签名】嘎嘎嘎 2018-03-27 16:31:04 2018-04-02 17:38:40 成功 2018-04-02 17:38:40 成功 DELIVRD', '95 18701296509 201803271631040259 【自动化签名】发送短信 2018-03-27 16:31:04 2018-04-02 17:38:40 成功 2018-04-02 17:38:40 成功 DELIVRD', '96 18701296509 201803271029550388 【自动化签名】您好，张三，您1990-02-01 00:00:00生日，特送你<<七十七天>>电影票一张 2018-03-27 10:29:55 2018-04-02 16:58:05 成功 2018-04-02 16:58:05 成功 DELIVRD', '97 18701296509 201803271029070381 【自动化签名】您好，张三，您1990-02-01 00:00:00生日，特送你<<七十七天>>电影票一张 2018-03-27 10:29:07 2018-04-02 16:58:05 成功 2018-04-02 16:58:05 成功 DELIVRD', '98 18701296509 201803270953430123 【自动化签名】嘎嘎嘎 2018-03-27 09:53:43 2018-04-02 16:58:05 成功 2018-04-02 16:58:05 成功 DELIVRD', '99 18701296509 201803270953060122 【自动化签名】嘎嘎嘎 2018-03-27 09:53:06 2018-04-02 16:35:20 成功 2018-04-02 16:35:20 成功 DELIVRD', '100 18701296509 201803270940210119 【自动化签名】嘎嘎嘎 2018-03-27 09:40:21 2018-04-02 15:03:20 成功 2018-04-02 15:03:20 成功 DELIVRD']
#
# print(cc[0])
# s = cc[-1].split(' ')
# print(s[0])
# s = xlrd.open_workbook('/Users/sy/Downloads/20180504155238.xls')
# print(s.sheet_names())
#
# sheet = s.sheet_by_name('明细列表1')
# print(sheet.nrows,sheet.ncols)
# #row = sheet.row_values(1)#获取第一行内容
# cols = sheet.col_values(1)#获取第二列内容
# print(cols)
timestr=time.strftime('%Y%m%d%H%m%S', time.localtime())
print(timestr)
t= time.time()
print(t)
print (time.strftime('%Y%m%d%H%M%S'))
os.system("cd /Users/sy/PycharmProjects/GMP/testcase & python 3.5")
#/Users/sy/PycharmProjects/GMP