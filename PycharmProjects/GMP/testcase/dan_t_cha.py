from selenium import webdriver
import HTMLTestRunner
from pages.searchPage import SearchPage
from selenium.webdriver.common.by import By
import unittest
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
class testDanGmp(unittest.TestCase):
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


    #查询条件需求:必须输入手机号才可以返回结果
    def test_a_DTCX001(self):
        '''不输入手机号查询  查询条件需求:必须输入手机号才可以返回结果'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',0.5)
        #查询按钮
        self.dan_cha = (By.XPATH,'/html/body/div[1]/div/section[2]/div/div/div/div[1]/div/div[2]/a[1]')
        dr.click_time(self.dan_cha,0.5)
        self.assertEqual(dr.base_get_text(dr.spnMessage_id),'请输入十一位手机号进行查询！')

    def test_a_DTCX002(self):
        '''输入手机号精确查询'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',0.5)
        #2018.02.01--2018.04.29
        self.time_2_4 = (By.XPATH,'//*[@id="reporttype"]/option[2]')
        dr.click_time(self.time_2_4,0.5)
        dr.clear_send(dr.ip_input,'13552321553')
        dr.click_time(dr.dan_cha,0.5)
        #判断手机号
        self.ip_number = (By.XPATH,'//*[@id="ctbId"]/tr/td[2]')
        self.assertEqual(dr.is_element_exist('//*[@id="ctbId"]/tr/td[2]'),True)
        self.assertEqual(dr.base_get_text(self.ip_number),'13552321553')

    def test_a_DTCX003(self):
        '''输入错误号码查询 预期结果:提示无记录，请修改查询条件 实际结果:请输入十一位手机号进行查询！'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',0.5)
        dr.clear_send(dr.ip_input,'1313w')
        dr.click_time(dr.dan_cha,0.5)
        self.assertEqual(dr.base_get_text(dr.spnMessage_id),'请输入十一位手机号进行查询！')

    def test_a_DTCX004(self):
        '''手机号码输入非法字符查询   预期结果:提示无记录, 实际结果:已做校验,智能输入手机号'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',0.5)
        dr.clear_send(dr.ip_input,'%&*（*&）')
        dr.click_time(dr.dan_cha,0.5)
        self.assertEqual(dr.base_get_text(dr.spnMessage_id),'请输入十一位手机号进行查询！')

    def test_a_DTCX005(self):
        '''手机号码输入非法字符查询   预期结果:提示无记录, 实际结果:已做校验,智能输入手机号'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',0.5)
        dr.clear_send(dr.ip_input,'--')
        dr.click_time(dr.dan_cha,0.5)
        self.assertEqual(dr.base_get_text(dr.spnMessage_id),'请输入十一位手机号进行查询！')

    def test_a_DTCX006(self):
        '''时间区间的下拉框选项是否正确'''
        pass
    def test_a_DTCX007(self):
        '''选择时间区间查询'''
        pass
    def test_a_DTCX008(self):
        '''时间区间和手机号码联合查询  符合条件'''
        pass
    def test_a_DTCX009(self):
        '''时间区间和手机号码联合查询  无符合条件的数据'''
        pass
    def test_a_DTCX010(self):
        '''输入存在子账号查询'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',0.5)
        #2018.02.01--2018.04.29
        self.time_2_4 = (By.XPATH,'//*[@id="reporttype"]/option[2]')
        dr.click_time(self.time_2_4,0.5)
        dr.clear_send(dr.ip_input,'13552321553')
        dr.clear_send(dr.sonID,'admin')
        dr.click_time(dr.dan_cha,0.5)
        #判断手机号
        self.ip_number = (By.XPATH,'//*[@id="ctbId"]/tr/td[2]')
        self.assertEqual(dr.is_element_exist('//*[@id="ctbId"]/tr/td[2]'),True)
        self.assertEqual(dr.base_get_text(self.ip_number),'13552321553')

    def test_a_DTCX011(self):
        '''输入不存在子账号查询  没有记录，请修改查询条件'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',0.5)
        dr.clear_send(dr.ip_input,'13552321553')
        dr.clear_send(dr.sonID,'adminassa')
        dr.click_time(dr.dan_cha,0.5)
        #查询无内容
        self.no_list = (By.XPATH,'//*[@id="ctbId"]/tr/td')
        self.assertEqual(dr.base_get_text(self.no_list),'没有记录，请修改查询条件')

    def test_a_DTCX012(self):
        '''子账号输入非法字符查询 提示没有记录,请修改查询条件'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',0.5)
        dr.clear_send(dr.ip_input,'13552321553')
        dr.clear_send(dr.sonID,'@#$%……&*')
        dr.click_time(dr.dan_cha,0.5)
        #查询无内容
        self.no_list = (By.XPATH,'//*[@id="ctbId"]/tr/td')
        self.assertEqual(dr.base_get_text(self.no_list),'没有记录，请修改查询条件')

    def test_a_DTCX013(self):
        '''子账号输入非法字符查询 提示没有记录,请修改查询条件'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',0.5)
        dr.clear_send(dr.ip_input,'13552321553')
        dr.clear_send(dr.sonID,'//')
        dr.click_time(dr.dan_cha,0.5)
        #查询无内容
        self.no_list = (By.XPATH,'//*[@id="ctbId"]/tr/td')
        self.assertEqual(dr.base_get_text(self.no_list),'没有记录，请修改查询条件')

    def test_a_DTCX014(self):
        '''时间区间+手机号码+子账号ID联合查询  实际前面用例已实现'''
        pass

    def test_a_DTCX0015(self):
        '''选择每页显示条数是否正确   延后 不好写'''
        # dr = self.searpage
        # dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',0.5)
        # dr.clear_send(dr.ip_input,'18701296509')
        # dr.click_time(dr.dan_cha,0.5)
        # self.js = "window.scrollTo(0,200)"
        # self.driver.execute_script(self.js)
        # time.sleep(1)
        pass

    def test_a_DTCX016(self):
        '''上一页按钮可点击'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',1)
        #时间区间
        self.time_bew = (By.ID,'reporttype"')
        #2018.02.01--2018.04.29
        self.time_2_4 = (By.XPATH,'//*[@id="reporttype"]/option[2]')
        dr.click_time(self.time_2_4,0.5)
        dr.clear_send(dr.ip_input,'18701296509')
        dr.click_time(dr.dan_cha,0.5)
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(1)
        #下一页
        self.next_page = (By.XPATH,'//*[@id="example1_next"]/a')
        dr.click_time(self.next_page,0.5)
        #上一页
        self.top_page = (By.XPATH,'//*[@id="example1_previous"]/a')
        dr.click_time(self.top_page,0.5)
        #序号10
        self.nember_10 = (By.XPATH,'//*[@id="ctbId"]/tr[10]/td[1]')
        self.assertEqual(dr.base_get_text(self.nember_10),'10')

    def test_a_DTCX017(self):
        '''已经是第一页点击上一页按钮给出提示  实际结果:上一页按钮禁用  用例不正确'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',1)
        #时间区间
        self.time_bew = (By.ID,'reporttype"')
        #2018.02.01--2018.04.29
        self.time_2_4 = (By.XPATH,'//*[@id="reporttype"]/option[2]')
        dr.click_time(self.time_2_4,0.5)
        dr.clear_send(dr.ip_input,'18701296509')
        dr.click_time(dr.dan_cha,0.5)
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(1)
        self.aa = self.driver.find_element_by_xpath('//*[@id="example1_previous"]/a').get_attribute('onclick')
        self.assertEqual(self.aa,None)

    def test_a_DTCX018(self):
        '''下一页按钮可点击'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',1)
        #时间区间
        self.time_bew = (By.ID,'reporttype"')
        #2018.02.01--2018.04.29
        self.time_2_4 = (By.XPATH,'//*[@id="reporttype"]/option[2]')
        dr.click_time(self.time_2_4,0.5)
        dr.clear_send(dr.ip_input,'18701296509')
        dr.click_time(dr.dan_cha,0.5)
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(1)
        #下一页
        self.next_page = (By.XPATH,'//*[@id="example1_next"]/a')
        dr.click_time(self.next_page,0.5)
        #序号20
        self.nember_20 = (By.XPATH,'//*[@id="ctbId"]/tr[10]/td[1]')
        self.assertEqual(dr.base_get_text(self.nember_20),'20')

    def test_a_DTCX019(self):
        '''已经是最后一页点击下一页按钮给出提示  实际结果:按钮禁用 用例不正确'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',1)
        #时间区间
        self.time_bew = (By.ID,'reporttype"')
        #2018.02.01--2018.04.29
        self.time_2_4 = (By.XPATH,'//*[@id="reporttype"]/option[2]')
        dr.click_time(self.time_2_4,0.5)
        dr.clear_send(dr.ip_input,'18701296509')
        dr.click_time(dr.dan_cha,0.5)
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

    def test_a_DTCX020(self):
        '''当前列表在第一页，点击第三页'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',1)
        #时间区间
        self.time_bew = (By.ID,'reporttype"')
        #2018.02.01--2018.04.29
        self.time_2_4 = (By.XPATH,'//*[@id="reporttype"]/option[2]')
        dr.click_time(self.time_2_4,0.5)
        dr.clear_send(dr.ip_input,'18701296509')
        dr.click_time(dr.dan_cha,0.5)
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(1)
        #第三页
        self.page_3 = (By.XPATH,'//*[@id="pageListId"]/li[4]/a')
        dr.click_time(self.page_3,1)
        #number30
        self.nember_30 = (By.XPATH,'//*[@id="ctbId"]/tr[10]/td[1]')
        self.assertEqual(dr.base_get_text(self.nember_30),'30')

    def test_a_DTCX021(self):
        '''分页总页数显示是否正确  '''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',1)
        #时间区间
        #self.time_bew = (By.ID,'reporttype"')
        #2018.02.01--2018.04.29
        self.time_2_4 = (By.XPATH,'//*[@id="reporttype"]/option[2]')
        dr.click_time(self.time_2_4,0.5)
        dr.clear_send(dr.ip_input,'18701296509')
        dr.click_time(dr.dan_cha,0.5)
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



    def test_a_DTCX022(self):
        '''当前列表在第一页，点击最后一页  数据不稳定,不建议做'''
        pass

    def test_a_DTCX023(self):
        '''分页总条数显示是否正确 分页显示总条数与实际显示列表总条数一致'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',1)
        #时间区间
        #2018.02.01--2018.04.29
        self.time_2_4 = (By.XPATH,'//*[@id="reporttype"]/option[2]')
        dr.click_time(self.time_2_4,0.5)
        dr.clear_send(dr.ip_input,'18701296509')
        dr.click_time(dr.dan_cha,0.5)
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
                self.v = self.driver.find_elements_by_xpath('//*[@id="ctbId"]/tr')
                cc = []
                for i in self.v:
                    cc.append(i.text)
                s = cc[-1].split(' ')
                print(s[0])
                self.assertEqual(dr.base_get_text(self.totalId),s[0])
                break

    def test_a_DTCX024(self):
        '''根据条件查询之后分页显示是否正确'''
        pass

    def test_a_DTCX025(self):
        '''不输入查询条件直接导出   实际结果:不可导出,对手机号进行了校验  用例不正确'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',0.5)
        #导出按钮
        self.onereferExcel = (By.ID,'onereferExcel')
        dr.click_time(self.onereferExcel,0.5)
        self.assertEqual(dr.base_get_text(dr.spnMessage_id),'请输入十一位手机号进行查询！')

    def test_a_DTCX026(self):
        '''根据手机号码导出  延后'''
        pass

    def test_a_DTCX027(self):
        '''手机号码输入非法字符导出 实际结果:不可导出,提示请输入十一位手机号进行查询   用例不正确'''
        dr = self.searpage
        dr.get_url_time('http://10.1.63.125:8080/gmp/send#/asingle',0.5)
        dr.clear_send(dr.ip_input,'1313w')
        #导出按钮
        self.onereferExcel = (By.ID,'onereferExcel')
        dr.click_time(self.onereferExcel,0.5)
        self.assertEqual(dr.base_get_text(dr.spnMessage_id),'请输入十一位手机号进行查询！')

    def test_a_DTCX028(self):
        '''导出用例27 28 29 30 没必要写,因为需要先通过点击查询来校验'''
        pass



    def tearDown(self):
        self.driver.refresh()



if __name__ == '__main__':
    suit = unittest.main()