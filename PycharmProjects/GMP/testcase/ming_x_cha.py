from selenium import webdriver
import HTMLTestRunner
from pages.searchPage import SearchPage
from selenium.webdriver.common.by import By
import unittest
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
import xlrd
import xlwt
class testMxiGmp(unittest.TestCase):
    dr = webdriver.Chrome("/Users/sy/Downloads/chromedriver 2")
    url = "http://10.1.63.125:8080/gmp/login"
    searpage = SearchPage(dr,url)
    searpage.goto_Gmppage()
    searpage.login()
    time.sleep(15)
    dr.get("http://10.1.63.125:8080/gmp/send#/overview")


    def setUp(self,driver = dr):
        self.driver = driver
        #self.driver.implicitly_wait(30)
        self.url = "http://10.1.63.125:8080/gmp/login"
        self.searpage = SearchPage(self.driver,self.url)
        self.driver.maximize_window()

    def test_a_MXCX031(self):
        '''不输入手机号查询  查询条件需求:必须输入手机号才可以返回结果'''
        # dr = self.searpage
        # dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        # 查询按钮
        # self.dan_cha = (By.XPATH,'/html/body/div[1]/div/section[2]/div/div/div/div[1]/div/div[2]/a[1]')
        # dr.click_time(self.dan_cha,0.5)
        # self.assertEqual(dr.base_get_text(dr.spnMessage_id),'请输入十一位手机号进行查询！')
        pass
    def test_a_MXCX032(self):
        '''输入错误信息包编号查询'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        #信息包输入框
        self.iptMsgId = (By.ID,'iptMsgId')
        dr.clear_send(self.iptMsgId,'12312412445')
        dr.click_time(dr.aBtnSearch,1)
        #查询无内容
        self.no_list = (By.XPATH,'//*[@id="detailhtmlId"]/tr/td')
        self.assertEqual(dr.base_get_text(self.no_list),'没有记录，请修改查询条件')

    def test_a_MXCX033(self):
        '''输入错误号码查询'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        #手机号输入框输入框
        self.iptMsgContent = (By.ID,'iptMsgContent')
        dr.clear_send(self.iptMsgContent,'12313121232')
        dr.click_time(dr.aBtnSearch,1)
        #查询无内容
        self.no_list = (By.XPATH,'//*[@id="detailhtmlId"]/tr/td')
        self.assertEqual(dr.base_get_text(self.no_list),'没有记录，请修改查询条件')

    def test_a_MXCX034(self):
        '''总数，成功，失败，未知的数量正确 延后'''
        pass

    def test_a_MXCX035(self):
        '''数据不足十条不分页'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        #手机号输入框输入框
        self.iptMsgContent = (By.ID,'iptMsgContent')
        dr.clear_send(self.iptMsgContent,'12313121232')
        dr.click_time(dr.aBtnSearch,1)
        #下一页
        self.next_page = '//*[@id="example1_next"]/a'
        self.assertEqual(dr.is_element_exist(self.next_page),False)

    def test_a_MXCX036(self):
        '''数据超过十条分页'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        dr.click_time(dr.aBtnSearch,1)
        #通过断言下一页的元素是否存在才判断是否分页
        self.assertEqual(dr.is_element_exist('//*[@id="example1_next"]/a'),True)

    def test_a_MXCX037(self):
        '''输入手机号精确查询'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        #手机号输入框输入框
        self.iptMsgContent = (By.ID,'iptMsgContent')
        dr.clear_send(self.iptMsgContent,'1355232153')
        dr.click_time(dr.aBtnSearch,1)
        #number_1
        number_1 = (By.ID,'id')
        #手机号
        iPhone = (By.XPATH,'//*[@id="detailhtmlId"]/tr/td[3]')


        #self.assertEqual(dr.base_get_text(number_1),'1')
        self.assertEqual(dr.is_element_exist('//*[@id="detailhtmlId"]/tr/td[3]'),True)
        self.assertEqual(dr.base_get_text(iPhone),'13552321553')





    def test_a_MXCX038(self):
        '''输入错误号码查询'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        #手机号输入框输入框
        self.iptMsgContent = (By.ID,'iptMsgContent')
        dr.clear_send(self.iptMsgContent,'123131')
        dr.click_time(dr.aBtnSearch,1)
        #查询无内容
        self.no_list = (By.XPATH,'//*[@id="detailhtmlId"]/tr/td')
        self.assertEqual(dr.base_get_text(self.no_list),'没有记录，请修改查询条件')

    def test_a_MXCX039(self):
        '''手机号码输入非法字符查询  实际结果:只能输入数字'''
        pass
    def test_a_MXCX040(self):
        '''手机号码输入非法字符查询  实际结果:只能输入数字'''
        pass

    def test_a_MXCX041(self):
        '''开始时间早于结束时间'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        #点击开始日期
        dr.clear_send(id,'2018-05-01')
        dr.click_time(dr.aBtnSearch,1)
        #number_1
        self.number_1 = (By.XPATH,'//*[@id="id"]')
        self.assertEqual(dr.base_get_text(self.number_1),'1')

    def test_a_MXCX042(self):
        '''开始时间晚于结束时间 不可选择晚于结束时间,时间控件做了限制'''
        pass

    def test_a_MXCX043(self):
        '''时间区间和手机号码联合查询  有结果'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        #点击开始日期
        dr.clear_send(id,'2018-05-01')
        #手机号输入框输入框
        self.iptMsgContent = (By.ID,'iptMsgContent')
        dr.clear_send(self.iptMsgContent,'13552321553')
        dr.click_time(dr.aBtnSearch,1)
        #number_1
        number_1 = (By.ID,'id')
        #手机号
        iPhone = (By.XPATH,'//*[@id="detailhtmlId"]/tr/td[3]')
        self.assertEqual(dr.base_get_text(number_1),'1')
        self.assertEqual(dr.base_get_text(iPhone),'13552321553')


    def test_a_MXCX044(self):
        '''时间区间和手机号码联合查询  无结果'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        #点击开始日期
        dr.clear_send(id,'2018-05-01')
        #手机号输入框输入框
        self.iptMsgContent = (By.ID,'iptMsgContent')
        dr.clear_send(self.iptMsgContent,'112321312312')
        dr.click_time(dr.aBtnSearch,1)
        #查询无内容
        self.no_list = (By.XPATH,'//*[@id="detailhtmlId"]/tr/td')
        self.assertEqual(dr.base_get_text(self.no_list),'没有记录，请修改查询条件')

    def test_a_MXCX045(self):
        '''输入存在子账号查询'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        #子账号输入框输入框
        self.sonID = (By.ID,'sonID')
        dr.clear_send(self.sonID,'admin')
        dr.click_time(dr.aBtnSearch,1)
        #number_1
        number_1 = (By.ID,'id')
        self.assertEqual(dr.base_get_text(number_1),'1')

    def test_a_MXCX046(self):
        '''输入不存在子账号查询'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        #子账号输入框输入框
        self.sonID = (By.ID,'sonID')
        dr.clear_send(self.sonID,'sdada')
        dr.click_time(dr.aBtnSearch,1)
         #查询无内容
        self.no_list = (By.XPATH,'//*[@id="detailhtmlId"]/tr/td')
        self.assertEqual(dr.base_get_text(self.no_list),'没有记录，请修改查询条件')

    def test_a_MXCX047(self):
        '''子账号输入非法字符查询'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        #子账号输入框输入框
        self.sonID = (By.ID,'sonID')
        dr.clear_send(self.sonID,'*&^%$$')
        dr.click_time(dr.aBtnSearch,1)
         #查询无内容
        self.no_list = (By.XPATH,'//*[@id="detailhtmlId"]/tr/td')
        self.assertEqual(dr.base_get_text(self.no_list),'没有记录，请修改查询条件')

    def test_a_MXCX048(self):
        '''子账号输入非法字符查询'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        #子账号输入框输入框
        self.sonID = (By.ID,'sonID')
        dr.clear_send(self.sonID,'--')
        dr.click_time(dr.aBtnSearch,1)
         #查询无内容
        self.no_list = (By.XPATH,'//*[@id="detailhtmlId"]/tr/td')
        self.assertEqual(dr.base_get_text(self.no_list),'没有记录，请修改查询条件')

    def test_a_MXCX049(self):
        '''根据信息类型查询'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        #信息类型自动化001
        leixin = (By.XPATH,'//*[@id="selProduct"]/option[4]')
        dr.click_time(leixin,0.5)
        dr.click_time(dr.aBtnSearch,1)
        #number_1
        number_1 = (By.ID,'id')
        self.assertEqual(dr.base_get_text(number_1),'1')

    def test_a_MXCX050(self):
        '''时间区间+手机号码+子账号ID联合查询'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        #子账号输入框输入框
        self.sonID = (By.ID,'sonID')
        dr.clear_send(self.sonID,'--')
        #手机号输入框输入框
        self.iptMsgContent = (By.ID,'iptMsgContent')
        dr.clear_send(self.iptMsgContent,'12313121232')
        dr.click_time(dr.aBtnSearch,1)
          #查询无内容
        self.no_list = (By.XPATH,'//*[@id="detailhtmlId"]/tr/td')
        self.assertEqual(dr.base_get_text(self.no_list),'没有记录，请修改查询条件')

        #子账号输入框输入框
        self.sonID = (By.ID,'sonID')
        dr.clear_send(self.sonID,'admin')
        #手机号输入框输入框
        self.iptMsgContent = (By.ID,'iptMsgContent')
        dr.clear_send(self.iptMsgContent,'18701296509')
        dr.click_time(dr.aBtnSearch,1)
        #number_1
        number_1 = (By.ID,'id')
        self.assertEqual(dr.base_get_text(number_1),'1')

    def test_a_MXCX051(self):
        '''选择每页显示条数是否正确'''
        pass

    def test_a_MXCX052(self):
        '''上一页按钮可点击'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        dr.click_time(dr.aBtnSearch,1)
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(1)
        #下一页
        self.next_page = (By.XPATH,'//*[@id="example1_next"]/a')
        dr.click_time(self.next_page,0.5)
        #上一页
        self.top_page = (By.XPATH,'//*[@id="example1_previous"]/a')
        dr.click_time(self.top_page,0.5)
        #number_1
        self.number_1 = (By.XPATH,'//*[@id="id"]')

        self.assertEqual(dr.base_get_text(self.number_1),'1')

    def test_a_MXCX053(self):
        '''已经是第一页点击上一页按钮给出提示'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        dr.click_time(dr.aBtnSearch,1)
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(1)
        #上一页
        self.top_page = (By.XPATH,'//*[@id="example1_previous"]/a')
        self.aa = self.driver.find_element_by_xpath('//*[@id="example1_previous"]/a').get_attribute('onclick')
        self.assertEqual(self.aa,None)

    def test_a_MXCX054(self):
        '''下一页按钮可点击 用例52已执行'''
        pass

    def test_a_MXCX055(self):
        '''已经是最后一页点击下一页按钮给出提示'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        dr.click_time(dr.aBtnSearch,1)
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(1)
        #下一页
        self.aa = self.driver.find_element_by_xpath('//*[@id="example1_next"]/a').get_attribute('onclick')
        for i in self.aa:
            if self.aa == None:
                self.assertEqual(self.aa,None)
            else:
                self.searpage.click_time(self.searpage.next_page,1)

    def test_a_MXCX056(self):
        '''当前列表在第一页，点击第三页'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        dr.click_time(dr.aBtnSearch,1)
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(1)
        #page2
        page2 = (By.XPATH,'//*[@id="pageListId"]/li[3]/a')
        dr.click_time(page2,1)

    def test_a_MXCX057(self):
        '''分页总页数显示是否正确'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        dr.click_time(dr.aBtnSearch,1)
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(1)
        #总页数
        self.totalPageId = (By.ID,'totalPageId')
        #遍历页面总共有多少页
        aa = self.driver.find_elements_by_class_name('paginate_button ')
        cc = []
        for i in aa:
            cc.append(i.text)
        print(cc[-2])
        self.assertEqual(dr.base_get_text(self.totalPageId),cc[-2])

    def test_a_MXCX058(self):
        '''当前列表在第一页，点击最后一页'''
        pass

    def test_a_MXCX059(self):
        '''分页总条数显示是否正确'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        dr.clear_send(id,'2018-05-01')
        dr.click_time(dr.aBtnSearch,1)
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(1)
         #总条数
        self.totalId = (By.ID,'totalId')
        #获取下一页中是否有onclick属性值,如果有点击下一页,如果没有则为最后一页
        self.aa = self.driver.find_element_by_xpath('//*[@id="example1_next"]/a').get_attribute('onclick')
        while self.aa == 'nextPage()':
            self.searpage.click_time(self.searpage.next_page,1)
            self.cc = self.driver.find_element_by_xpath('//*[@id="example1_next"]/a').get_attribute('onclick')
            if self.cc == None:
                self.v = self.driver.find_elements_by_xpath('//*[@id="detailhtmlId"]/tr')
                cc = []
                for i in self.v:
                    cc.append(i.text)
                s = cc[-1].split(' ')
                print(s[0])
                self.assertEqual(dr.base_get_text(self.totalId),s[0])
                break
    def test_a_MXCX060(self):
        '''根据条件查询之后分页显示是否正确 用例57已做'''
        pass

    def test_a_MXCX061(self):
        '''选择时间区间，点击查询，导出'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        #点击开始日期
        dr.clear_send(id,'2018-05-01')
        dr.click_time(dr.aBtnSearch,1)
        #导出按钮
        outdetailsExcle = (By.ID,'outdetailsExcle')
        timestr=time.strftime('%Y%m%d%H%M%S')
        self.driver.find_element_by_id('outdetailsExcle').click()
        print(timestr)
        time.sleep(2)
        # a = self.driver.find_element_by_id('iptDateRange_Start').get_attribute('value')
        #打开导出的文件
        s = xlrd.open_workbook('/Users/sy/Downloads/'+timestr+'.xls')
        print(s.sheet_names())
        sheet = s.sheet_by_name('明细列表1')
        #print(sheet.nrows,sheet.ncols)
        #row = sheet.row_values(1)#获取第一行内容
        cols = sheet.col_values(1)#获取第二列内容
        print(cols)
        self.assertEqual(cols[1],'18727272727')
        self.assertEqual(cols[4],'18701296500')
        self.assertEqual(cols[7],'18701296509')

    def test_a_MXCX062(self):
        '''选择每种信息类型，点击查询，导出'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/receipt',0.5)
        id = (By.ID,'iptDateRange_Start')
        #点击开始日期
        dr.clear_send(id,'2018-05-01')
        #信息类型自动化001
        leixin = (By.XPATH,'//*[@id="selProduct"]/option[4]')
        dr.click_time(leixin,0.5)
        dr.click_time(dr.aBtnSearch,1)

        outdetailsExcle = (By.ID,'outdetailsExcle')
        timestr=time.strftime('%Y%m%d%H%M%S')
        self.driver.find_element_by_id('outdetailsExcle').click()
        print(timestr)
        time.sleep(2)
        # a = self.driver.find_element_by_id('iptDateRange_Start').get_attribute('value')
        #打开导出的文件
        s = xlrd.open_workbook('/Users/sy/Downloads/'+timestr+'.xls')
        print(s.sheet_names())
        sheet = s.sheet_by_name('明细列表1')
        #print(sheet.nrows,sheet.ncols)
        #row = sheet.row_values(1)#获取第一行内容
        cols = sheet.col_values(1)#获取第二列内容
        print(cols)
        self.assertEqual(cols[1],'18727272727')
        self.assertEqual(cols[4],'18701296500')
        self.assertEqual(cols[7],'18718181818')

    def test_a_MXCX063(self):
        '''输入信息包编号查询，导出   63 64 65 66 67 前面用例已覆盖'''
        pass
















    def tearDown(self):
        self.driver.refresh()



if __name__ == '__main__':
    suit = unittest.main()