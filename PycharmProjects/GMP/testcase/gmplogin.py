from selenium import webdriver
import HTMLTestRunner
from pages.searchPage import SearchPage
from selenium.webdriver.common.by import By
import unittest
import time
import random
from selenium.webdriver.common.action_chains import ActionChains

class testSearchGmp(unittest.TestCase):
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



    def test_b_GLMB001(self):
        '''进入模板审核'''
        self.searpage = SearchPage(self.driver,self.url)
        self.searpage.base_click(self.searpage.gmp_guanli)
        self.searpage.base_click(self.searpage.shujuguanli)
        time.sleep(2)
        self.searpage.base_click(self.searpage.moban)
        time.sleep(3)
        self.assertEqual(self.searpage.base_get_text(self.searpage.moban_cha),"查询")

    def test_b_GLMB002(self):
        '''输入已存在的账号id查询'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage = SearchPage(self.driver,self.url)
        self.searpage.base_claer(self.searpage.pno_id)
        self.searpage.base_input_text(self.searpage.pno_id,'admin')
        self.searpage.base_click(self.searpage.moban_cha)
        time.sleep(2)
        self.xpah = (By.XPATH,'//*[@id="smsAdmincId"]/tr[1]/td[3]')
        print(self.searpage.base_get_text(self.xpah))
        self.assertEqual(self.searpage.base_get_text(self.xpah),'admin')

    def test_b_GLMB003(self):
        '''输入不存在的账号id查询'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage = SearchPage(self.driver,self.url)
        self.searpage.clear_send(self.searpage.pno_id,'tasafsdsdf')
        self.searpage.base_click(self.searpage.moban_cha)
        time.sleep(2)
        self.xpah = (By.XPATH,'//*[@id="smsAdmincId"]/tr/td')
        self.assertEqual(self.searpage.base_get_text(self.xpah),'没有记录，请修改查询条件')

    def test_b_GLMB004(self):
        '''输入已存在模板id查询'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage = SearchPage(self.driver,self.url)
        self.searpage.clear_send(self.searpage.pno_id,2)
        self.searpage.base_click(self.searpage.moban_cha)
        time.sleep(2)
        self.xpah = (By.XPATH,'//*[@id="smsAdmincId"]/tr/td[4]/span/span')
        self.assertEqual(self.searpage.base_get_text(self.xpah),'2')

    def test_b_GLMB005(self):
        '''输入不存在的模板id查询'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage = SearchPage(self.driver,self.url)
        self.searpage.clear_send(self.searpage.pno_id,232423423)
        self.searpage.base_click(self.searpage.moban_cha)
        time.sleep(2)
        self.xpah = (By.XPATH,'//*[@id="smsAdmincId"]/tr/td')
        self.assertEqual(self.searpage.base_get_text(self.xpah),'没有记录，请修改查询条件')

    def test_b_GLMB006(self):
        '''输入非法字符进行查询'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage = SearchPage(self.driver,self.url)
        self.searpage.clear_send(self.searpage.pno_id,'%^%%$#')
        self.searpage.base_click(self.searpage.moban_cha)
        time.sleep(2)
        self.xpah = (By.XPATH,'//*[@id="smsAdmincId"]/tr/td')
        self.assertEqual(self.searpage.base_get_text(self.xpah),'没有记录，请修改查询条件')

    def test_b_GLMB007(self):
    #     '''输入已存在的账号ID，选择该账号ID模板最后更新的时间范围内，查询,目前无法实现该功能'''
    #     self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
    #     self.searpage = SearchPage(self.driver,self.url)
    #     self.searpage.clear_send(self.searpage.pno_id,2)
    #     self.searpage.click_time(self.searpage.iptDateRange_Start_id,1)
    #     self.riqistart = (By.XPATH,'/html/body/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[3]')
    #     self.searpage.click_time(self.riqistart,1)
    #     self.searpage.click_time(self.searpage.iptDateRange_End_id,1)
    #     self.riqiend = (By.XPATH,'/html/body/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[2]')
    #     self.searpage.base_click(self.riqiend)
    #     self.searpage.click_time(self.searpage.moban_cha,2)
    #     self.mo_number_2 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[1]/td[4]/span/span')
    #     self.assertEqual(self.searpage.base_get_text(self.mo_number_2),'2')
        pass

    def test_b_GLMB008(self):
        '''输入已存在的账号ID，选择该账号ID模板最后更新的时间不在范围内，查询  日期控件存在不确定性'''
        # self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        # self.searpage = SearchPage(self.driver,self.url)
        # self.searpage.clear_send(self.searpage.pno_id,2)
        # self.searpage.click_time(self.searpage.iptDateRange_Start_id,1)
        # self.riqistart = (By.XPATH,'/html/body/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[7]')
        # self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/table/thead/tr[1]/th[1]').click()
        # self.searpage.click_time(self.riqistart,1)
        # self.searpage.click_time(self.searpage.iptDateRange_End_id,1)
        # self.riqiend = (By.XPATH,'/html/body/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[7]')
        # self.searpage.base_click(self.riqiend)
        # self.searpage.click_time(self.searpage.moban_cha,2)
        # self.xpah = (By.XPATH,'//*[@id="smsAdmincId"]/tr/td')
        # self.assertEqual(self.searpage.base_get_text(self.xpah),'没有记录，请修改查询条件')
        pass

    # def test_b_GLMB009(self):
    #     '''选择每页显示条数是否正确'''
    #     self.searpage = SearchPage(self.driver,self.url)
    #     self.searpage.click_time(self.searpage.pageOptId_id,1)
    #     self.shu_10 = (By.XPATH,'//*[@id="pageOptId"]/option[1]')
    #     self.searpage.click_time(self.shu_10,1)
    #     self.number_10 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[10]/td[1]')
    #     self.assertEqual(self.searpage.base_get_text(self.number_10),'10')

    def test_b_GLMB010(self):
        '''上一页按钮可点击'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        self.searpage.click_time(self.searpage.next_page,2)
        self.top_page = (By.XPATH,'//*[@id="example1_previous"]/a')
        self.searpage.click_time(self.top_page,2)
        self.number_10 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[10]/td[1]')
        self.assertEqual(self.searpage.base_get_text(self.number_10),'10')

    def test_b_GLMB011(self):
        '''已经是第一页点击上一页按钮给出提示'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(3)
        self.aa = self.driver.find_element_by_xpath('//*[@id="example1_previous"]/a').get_attribute('onclick')
        #self.element = WebDriverWait(self.driver,3,0.5).until(EC.element_to_be_clickable(self.top_page))
        #self.aa = self.driver.__getattribute__('aria-controls')
        print(self.aa)
        self.assertEqual(self.aa,None)

    def test_b_GLMB012(self):
        '''下一页可点击'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(3)
        self.searpage.click_time(self.searpage.next_page,1)
        self.number = (By.XPATH,'//*[@id="smsAdmincId"]/tr[1]/td[1]')
        self.assertEqual(self.searpage.base_get_text(self.number),'11')

    def test_b_GLMB013(self):
        '''已经是最后一页点击下一页按钮给出提示'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(3)
        # self.driver.find_element_by_xpath('//*[@id="pageListId"]/li[5]/a').click()
        # time.sleep(2)
        self.aa = self.driver.find_element_by_xpath('//*[@id="example1_next"]/a').get_attribute('onclick')
        # self.v = self.driver.find_elements_by_xpath('//*[@id="smsAdmincId"]/tr')
        # print(self.v)
        # cc = []
        # for i in self.v:
        #     cc.append(i.text)
        # print(cc)
        while self.aa == 'nextPage()':
            self.searpage.click_time(self.searpage.next_page,1)
            self.cc = self.driver.find_element_by_xpath('//*[@id="example1_next"]/a').get_attribute('onclick')
            print(self.cc)
            if self.cc == None:
                self.assertEqual(self.cc,None)
                break

    def test_b_GLMB014(self):
        '''当前列表在第一页，点击第三页'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(3)
        self.number_page = (By.XPATH,'//*[@id="pageListId"]/li[3]/a')
        self.searpage.click_time(self.number_page,1)
        self.number = (By.XPATH,'//*[@id="smsAdmincId"]/tr[1]/td[1]')
        self.assertEqual(self.searpage.base_get_text(self.number),'11')

    def test_b_GLMB015(self):
        '''当前列表在第一页，点击最后一页'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(3)
        self.number_page = (By.XPATH,'//*[@id="pageListId"]/li[3]/a')
        self.searpage.click_time(self.number_page,1)
        self.number = (By.XPATH,'//*[@id="smsAdmincId"]/tr[1]/td[1]')
        self.assertEqual(self.searpage.base_get_text(self.number),'11')

    def test_b_GLMB019(self):
        '''审核功能是否可用'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        #选择第一条
        self.xuanze = (By.XPATH,'//*[@id="smsAdmincId"]/tr[1]/td[2]/input')
        self.searpage.click_time(self.xuanze,0.2)
        self.searpage.click_time(self.searpage.shen_click,1)
        #实例化select 点击审核按钮 然后进入下拉框中
        # self.s1 = Select(self.driver.find_element_by_id('sts'))
        # print(self.s1.select_by_value('0'))
        # print(self.s1.select_by_visible_text('有效'))
        self.driver.find_element_by_id('sts').click()
        self.id_s0 = (By.ID,'s0')
        self.id_s1 = (By.ID,'s1')
        self.id_s2 = (By.ID,'s2')
        self.assertEqual(self.searpage.base_get_text(self.id_s0),'有效')
        self.assertEqual(self.searpage.base_get_text(self.id_s1),'无效')
        self.assertEqual(self.searpage.base_get_text(self.id_s2),'待审核')

    def test_b_GLMB020(self):
        '''模板状态改为无效时，无效理由是否必填'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.xuanze = (By.XPATH,'//*[@id="smsAdmincId"]/tr[1]/td[2]/input')
        self.searpage.click_time(self.xuanze,0.2)
        self.searpage.click_time(self.searpage.shen_click,1)
        self.driver.find_element_by_id('sts').click()
        self.id_s1 = (By.ID,'s1')
        self.searpage.click_time(self.id_s1,0.5)
        self.searpage.click_time(self.searpage.btn_success,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'无效原由不能为空')

    def test_b_GLMB021(self):
        '''无效理由输入不合法'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.xuanze = (By.XPATH,'//*[@id="smsAdmincId"]/tr[1]/td[2]/input')
        self.searpage.click_time(self.xuanze,0.2)
        self.searpage.click_time(self.searpage.shen_click,1)
        self.driver.find_element_by_id('sts').click()
        self.id_s1 = (By.ID,'s1')
        self.searpage.click_time(self.id_s1,0.5)
        #获取maxlength = 64的属性值,进行判断
        self.aa = self.driver.find_element_by_id('remarks').get_attribute('maxlength')
        print(self.aa)
        self.assertEqual(self.aa,'64')

    def test_b_GLMB022(self):
        '''无效理由输入不合法2'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.xuanze = (By.XPATH,'//*[@id="smsAdmincId"]/tr[1]/td[2]/input')
        self.searpage.click_time(self.xuanze,0.2)
        self.searpage.click_time(self.searpage.shen_click,1)
        self.driver.find_element_by_id('sts').click()
        self.id_s1 = (By.ID,'s1')
        self.searpage.click_time(self.id_s1,0.5)
        self.searpage.base_input_text(self.searpage.remarks_id,'<script>alert("111")</script>')
        self.searpage.click_time(self.searpage.btn_success,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'审核成功')

    def test_b_GLMB023(self):
        '''修改状态为无效，发送中心该模板状态是否相应变化'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.xuanze = (By.XPATH,'//*[@id="smsAdmincId"]/tr[1]/td[2]/input')
        self.searpage.click_time(self.xuanze,0.2)
        self.searpage.click_time(self.searpage.shen_click,1)
        self.driver.find_element_by_id('sts').click()
        self.id_s1 = (By.ID,'s1')
        self.searpage.click_time(self.id_s1,0.5)
        self.searpage.base_input_text(self.searpage.remarks_id,'<script>alert("111")</script>')
        self.searpage.click_time(self.searpage.btn_success,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'审核成功')
        self.assertEqual(self.searpage.base_get_text(self.searpage.stat2_id),'无效')
    def test_b_GLMB024(self):
        '''修改状态为有效，发送中心该模板状态是否相应变化'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.xuanze = (By.XPATH,'//*[@id="smsAdmincId"]/tr[4]/td[2]/input')
        #选择第四条
        self.searpage.click_time(self.xuanze,0.2)
        #点击审核按钮
        self.searpage.click_time(self.searpage.shen_click,1)
        self.driver.find_element_by_id('sts').click()
        self.id_s0 = (By.ID,'s0')
        self.searpage.click_time(self.id_s0,0.5)
        self.searpage.click_time(self.searpage.btn_success,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'审核成功')
        self.assertEqual(self.searpage.base_get_text(self.searpage.youxiao_5),'有效')

    def test_b_GLMB025(self):
        '''修改状态为待审核，发送中心该模板状态是否相应变化'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.xuanze = (By.XPATH,'//*[@id="smsAdmincId"]/tr[4]/td[2]/input')
        self.searpage.click_time(self.xuanze,0.2)
        self.searpage.click_time(self.searpage.shen_click,1)
        self.driver.find_element_by_id('sts').click()
        #self.id_s0 = (By.ID,'s0')
        self.id_s2 = (By.ID,'s2')
        self.searpage.click_time(self.id_s2,0.5)
        self.searpage.click_time(self.searpage.btn_success,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'审核成功')
        self.assertEqual(self.searpage.base_get_text(self.searpage.daishen_xpath),'待审核')

    def test_b_GLMB026(self):
        '''选择多个模板状态不一样的模板进行审核'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.xuanze_2 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[2]/td[2]/input')
        self.xuanze_5 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[5]/td[2]/input')
        self.searpage.clickAndClick(self.xuanze_2,self.xuanze_5)
        self.searpage.click_time(self.searpage.shen_click,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'请选择同一状态的模板')

    def test_b_GLMB027(self):
        '''选择多个账号状态一样的模板进行审核'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(3)
        self.xuanze_8 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[8]/td[2]/input')
        self.xuanze_9 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[9]/td[2]/input')
        self.searpage.clickAndClick(self.xuanze_8,self.xuanze_9)
        self.js = "window.scrollTo(0,0)"
        self.driver.execute_script(self.js)
        time.sleep(3)
        self.searpage.click_time(self.searpage.shen_click,1)
        self.driver.find_element_by_id('sts').click()
        self.id_s0 = (By.ID,'s0')
        self.searpage.click_time(self.id_s0,0.5)
        self.searpage.click_time(self.searpage.btn_success,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'审核成功')
        self.assertEqual(self.searpage.base_get_text(self.searpage.youxiao_8),'有效')
        self.assertEqual(self.searpage.base_get_text(self.searpage.youxiao_9),'有效')

    def test_b_GLMB028(self):
        '''编辑时账号ID，模板内容，状态信息是否回显'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage.click_time(self.searpage.bianji_3,1)
        self.driver.find_element_by_id('st')
        self.driver.find_element_by_id('st0').click()
        self.bianji_shen = (By.XPATH,'//*[@id="myModal-examine"]/div/div/div[3]/button[2]')
        self.searpage.click_time(self.bianji_shen,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.youxiao_4),'有效')

    def test_b_GLMB029(self):
        '''模板内容为空时，能否提交成功'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage.click_time(self.searpage.bianji_3,1)
        self.driver.find_element_by_id('ctpl').clear()
        self.bianji_shen = (By.XPATH,'//*[@id="myModal-examine"]/div/div/div[3]/button[2]')
        self.searpage.click_time(self.bianji_shen,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'模板内容不能为空')



    def test_b_GLMB031(self):
        '''模板内容输入不合法'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage.click_time(self.searpage.bianji_3,1)
        self.driver.find_element_by_id('ctpl').clear()
        self.a = random.randint(1000,2000)
        self.driver.find_element_by_id('ctpl').send_keys('<script>alert("111")</script>【是撒多%s】'%(self.a))
        self.bianji_shen = (By.XPATH,'//*[@id="myModal-examine"]/div/div/div[3]/button[2]')
        self.searpage.click_time(self.bianji_shen,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'编辑成功')

    def test_b_GLMB032(self):
        '''修改状态为无效时，不填写无效理由直接点击提交'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage.click_time(self.searpage.bianji_3,1)
        self.driver.find_element_by_id('st')
        self.driver.find_element_by_id('st1').click()
        self.bianji_shen = (By.XPATH,'//*[@id="myModal-examine"]/div/div/div[3]/button[2]')
        self.searpage.click_time(self.bianji_shen,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'无效原由不能为空')

    def test_b_GLMB033(self):
        '''模板内容输入不合法NULL'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage.click_time(self.searpage.bianji_3,1)
        self.driver.find_element_by_id('ctpl').clear()
        self.b = random.randint(1,1000)
        self.driver.find_element_by_id('ctpl').send_keys('NULL%s【是撒多】'%(self.b))
        self.bianji_shen = (By.XPATH,'//*[@id="myModal-examine"]/div/div/div[3]/button[2]')
        self.searpage.click_time(self.bianji_shen,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'编辑成功')

    def test_b_GLMB034(self):
        '''无效理由输入不合法null   输入null应判断为字符串,实际没有做判断,所以编辑成功了'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage.click_time(self.searpage.bianji_3,1)
        self.driver.find_element_by_id('st')
        self.driver.find_element_by_id('st1').click()
        self.bianji_shen = (By.XPATH,'//*[@id="myModal-examine"]/div/div/div[3]/button[2]')
        self.driver.find_element_by_id('cremark').send_keys('null')
        self.searpage.click_time(self.bianji_shen,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'编辑成功')

    def test_b_GLMB035(self):
        '''无效理由输入不合法字符显示64'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage.click_time(self.searpage.bianji_3,1)
        self.driver.find_element_by_id('st')
        self.driver.find_element_by_id('st1').click()
        self.bianji_shen = (By.XPATH,'//*[@id="myModal-examine"]/div/div/div[3]/button[2]')
        self.aa = self.driver.find_element_by_id('remarks').get_attribute('maxlength')
        print(self.aa)
        self.assertEqual(self.aa,'64')

    def test_b_GLMB036(self):
        '''无效理由输入不合法<script>alert("111")</script>'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage.click_time(self.searpage.bianji_5,1)
        self.driver.find_element_by_id('st')
        self.driver.find_element_by_id('st1').click()
        self.bianji_shen = (By.XPATH,'//*[@id="myModal-examine"]/div/div/div[3]/button[2]')
        self.driver.find_element_by_id('cremark').send_keys('<script>alert("111")</script>')
        self.searpage.click_time(self.bianji_shen,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'编辑成功')

    def test_b_GLMB039(self):
        '''取消按钮是否可用'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage.click_time(self.searpage.bianji_3,1)
        self.bianji_quxiao = (By.XPATH,'//*[@id="myModal-examine"]/div/div/div[3]/button[1]')
        self.searpage.click_time(self.bianji_quxiao,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.youxiao_4),'有效')

    def test_b_GLMB040(self):
        '''删除功能是否可用,点击右上角的删除按钮,给出请选择模板的提示'''
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.searpage.base_click(self.searpage.deleteSms_id)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'请至少选择一个模板')

    def test_b_GLMB041(self):
        '''删除一个模板'''
        self.driver.get('http://10.1.63.125:8080/gmp/send#/smstpl')
        self.searpage.click_time(self.searpage.add_class,0.5)
        self.a = random.randint(1000,2000)
        self.searpage.base_input_text(self.searpage.smstpl_id,'啊飒飒【萨达%s】'%(self.a))
        self.searpage.click_time(self.searpage.btn_tijiao,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'添加成功')
        self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(2)
        self.page_3 = (By.XPATH,'//*[@id="pageListId"]/li[4]/a')
        self.searpage.click_time(self.page_3,1)
        self.js = "window.scrollTo(0,0)"
        self.driver.execute_script(self.js)
        time.sleep(1)
        self.number24_dele = (By.XPATH,'//*[@id="smsAdmincId"]/tr[4]/td[8]/a[2]')
        self.searpage.click_time(self.number24_dele,0.5)
        self.dele_queren = (By.XPATH,'//*[@id="myModal-dele"]/div/div/div[3]/button[2]')
        self.searpage.click_time(self.dele_queren,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'删除成功')

    def test_b_GLMB042(self):
        '''包含43 44 用例选择多个模板删除 仅选择标题的复选框，进行删除 删除之后分页数据，总条数是否变化'''
        # self.driver.get('http://10.1.63.125:8080/gmp/send#/smstpl')
        # self.cc = random.randint(1,1000)
        # self.searpage.click_time(self.searpage.add_class,0.5)
        # self.searpage.base_input_text(self.searpage.smstpl_id,'我快捷键%s【萨达】'%(self.cc))
        # self.searpage.click_time(self.searpage.btn_tijiao,1)
        # self.searpage.click_time(self.searpage.add_class,0.5)
        # self.searpage.base_input_text(self.searpage.smstpl_id,'我快中心%s【萨达】'%(self.cc))
        # self.searpage.click_time(self.searpage.btn_tijiao,1)
        # self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
        # self.js = "window.scrollTo(0,200)"
        # self.driver.execute_script(self.js)
        # time.sleep(2)
        # self.page_3 = (By.XPATH,'//*[@id="pageListId"]/li[4]/a')
        # self.searpage.click_time(self.page_3,1)
        # self.js = "window.scrollTo(0,0)"
        # self.driver.execute_script(self.js)
        # time.sleep(1)
        # self.number_24 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[4]/td[2]/input')
        # self.number_25 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[5]/td[2]/input')
        # self.searpage.clickAndClick(self.number_24,self.number_25)
        # self.driver.find_element_by_id('deleteSms').click()
        # time.sleep(1)
        # self.dele_queren = (By.XPATH,'//*[@id="myModal-dele"]/div/div/div[3]/button[2]')
        # self.searpage.click_time(self.dele_queren,1)
        # self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'删除成功')
        pass
    def test_b_GLMB045(self):
        '''进入短信'''
        self.driver.get('http://10.1.63.125:8080/gmp/send#/overview')
        self.searpage.click_time(self.searpage.zhanghu,2)
        self.searpage.click_time(self.searpage.duanxin,2)
        self.assertEqual(self.searpage.base_get_text(self.searpage.cha_xpath),"查询")

    def test_b_GLMB046(self):
        '''输入已存在的模板id为2 排名第一'''
        self.driver.get('http://10.1.63.125:8080/gmp/send#/smstpl')
        self.searpage.clear_send(self.searpage.smsid,'2')
        self.searpage.click_time(self.searpage.cha_xpath,1)
        self.neirong = (By.XPATH,'//*[@id="smsSendcId"]/tr/td[3]')
        self.number_1 = (By.XPATH,'//*[@id="smsSendcId"]/tr/td[1]')
        self.assertEqual(self.searpage.base_get_text(self.neirong,),'哈哈哈哈哈【天龙人】')
        self.assertEqual(self.searpage.base_get_text(self.number_1,),'1')

    def test_b_GLMB047(self):
        '''输入不存在的模板id查询'''
        self.driver.get('http://10.1.63.125:8080/gmp/send#/smstpl')
        self.searpage.clear_send(self.searpage.smsid,'21213124')
        self.searpage.click_time(self.searpage.cha_xpath,1)
        self.erro = (By.XPATH,'//*[@id="smsSendcId"]/tr/td')
        self.assertEqual(self.searpage.base_get_text(self.erro),'没有记录，请修改查询条件')

    def test_b_GLMB048(self):
        '''输入特殊字符查询 %#@@%'''
        self.driver.get('http://10.1.63.125:8080/gmp/send#/smstpl')
        self.searpage.clear_send(self.searpage.smsid,'%#@@%')
        self.searpage.click_time(self.searpage.cha_xpath,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'请输入正确的模板ID')

    def test_b_GLMB049(self):
        '''选择每页显示条数是否正确   数据不全'''
        pass

    def test_b_GLMB050(self):
        '''上一页按钮可点击 下一页按钮可点击'''
        self.driver.get('http://10.1.63.125:8080/gmp/send#/smstpl')
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        self.searpage.click_time(self.searpage.next_page,2)
        self.top_page = (By.XPATH,'//*[@id="example1_previous"]/a')
        self.searpage.click_time(self.top_page,2)
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        self.duan_number_10 = (By.XPATH,'//*[@id="smsSendcId"]/tr[10]/td[1]')
        self.assertEqual(self.searpage.base_get_text(self.duan_number_10),'10')

    def test_b_GLMB051(self):
        '''已经是第一页点击上一页按钮给出提示'''
        self.driver.get('http://10.1.63.125:8080/gmp/send#/smstpl')
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(1)
        self.aa = self.driver.find_element_by_xpath('//*[@id="example1_previous"]/a').get_attribute('onclick')
        self.assertEqual(self.aa,None)

    def test_b_GLMB052(self):
        '''第50条用例已覆盖'''
        pass

    def test_b_GLMB053(self):
        '''已经是最后一页点击下一页按钮给出提示  实际结果没有给出提示,变为了不可点击的状态'''
        self.driver.get('http://10.1.63.125:8080/gmp/send#/smstpl')
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        self.aa = self.driver.find_element_by_xpath('//*[@id="example1_next"]/a').get_attribute('onclick')
        for i in self.aa:
            if i == None:
                self.assertEqual(self.aa,None)
            else:
                self.searpage.click_time(self.searpage.next_page,1)

    def test_b_GLMB054(self):
        '''当前列表在第一页，点击第三页 点击最后一页'''
        self.driver.get('http://10.1.63.125:8080/gmp/send#/smstpl')
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        time.sleep(1)
        self.number_page_2 = (By.XPATH,'//*[@id="pageListId"]/li[3]/a')
        self.searpage.click_time(self.number_page_2,1)

    def test_b_GLMB055(self):
        '''第54用例已覆盖'''
        pass

    def test_b_GLMB056(self):
        '''56 57 58 数据局限性,数据冲突,无法覆盖'''
        pass
    def test_b_GLMB059(self):
        '''模板状态背景色显示是否正确   后续处理'''
        pass
    def test_b_GLMB060(self):
        '''模板内容为空'''
        self.driver.get('http://10.1.63.125:8080/gmp/send#/smstpl')
        self.searpage.click_time(self.searpage.add_class,0.5)
        self.searpage.base_input_text(self.searpage.smstpl_id,'')
        self.searpage.click_time(self.searpage.btn_tijiao,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'短信模板内容不能为空')

    def test_b_GLMB061(self):
        '''模板内容输入非法字符 null  用例62模板内容输入非法字符串  <script>alert("111")</script>'''
        self.driver.get('http://10.1.63.125:8080/gmp/send#/smstpl')
        self.searpage.click_time(self.searpage.add_class,0.5)
        self.a = random.randint(1000,2000)
        self.searpage.base_input_text(self.searpage.smstpl_id,'null【宝宝贝贝%s】'%(self.a))
        self.searpage.click_time(self.searpage.btn_tijiao,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'添加成功')
        self.js = "window.scrollTo(0,200)"
        self.driver.execute_script(self.js)
        # time.sleep(1)
        # self.searpage.click_time(self.searpage.next_page,1)
        # self.searpage.click_time(self.searpage.next_page,1)
        # self.driver.find_element_by_xpath('//*[@id="smsSendcId"]/tr[9]/td[6]/a[1]').click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="myModal-dele"]/div/div/div[3]/button[2]').click()
        # self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'删除成功')

    def test_b_GLMB062(self):
        '''模板内容输入非法字符串  <script>alert("111")</script>'''
        self.driver.get('http://10.1.63.125:8080/gmp/send#/smstpl')
        self.searpage.click_time(self.searpage.add_class,0.5)
        self.a = random.randint(1000,2000)
        self.searpage.base_input_text(self.searpage.smstpl_id,'<script>alert("111")</script>【啥深层次%s】'%(self.a))
        self.searpage.click_time(self.searpage.btn_tijiao,1)
        self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'添加成功')
    def test_b_GLMB063(self):
        '''模板内容长度输入过长   没有做校验'''
        self.assertEqual(1,2)

    def test_b_GLMB064(self):
        '''删除一个模板  用例64 65 不可做,影响数据'''
        pass

    def test_b_GLMB065(self):
        pass

    def test_b_GLMB066(self):
        '''用例67 68 69 模板状态接口都没有做校验,可以发送成功'''
        pass

    def test_b_GLMB069(self):
        '''未生效状态的模板，鼠标划过状态，会显示未生效原因'''
        self.driver.get('http://10.1.63.125:8080/gmp/send#/smstpl')
        time.sleep(1)
        self.move = self.driver.find_element_by_xpath('//*[@id="smsSendcId"]/tr[1]/td[5]/span')
        ActionChains(self.driver).move_to_element(self.move).perform()
        time.sleep(1)

    # def test_zzz(self):
    #     '''退出浏览器'''
    #     self.driver.quit()
    def tearDown(self):

        self.driver.refresh()



if __name__ == '__main__':
    suit = unittest.main()
    # suit = unittest.TestSuite()
    # suit.addTest(unittest.makeSuite(testSearchGmp))
    #
    # timestr=time.strftime('%Y%m%d%H%m%S', time.localtime(time.time()))
    #
    # # 报告路径fp = open('./ka.html', 'wb')
    # fp = open('/Users/sy/PycharmProjects/GMP/config/result'+timestr+'.html',"wb")
    # # 定义测试报告
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="自动化测试报告",description="审核模板,短信模板")
    #
    # # runner = unittest.TextTestRunner()
    # runner.run(suit)
    #
    # #mailbody = fp.read()
    #
    # fp.close()

    # fp = open('./lug.html',"wb")
    # # mailbody = fp.read()
    # fp.close()

    # msg = MIMEText(mailbody,"html","utf-8")
    # #设计邮件主题
    # msg["subject"] = Header("hahhahah","utf-8")
    #
    # smtp = smtplib.SMTP()
    #
    # #连接服务器
    # smtp.connect("mail.qq.com")
    # #登录
    # smtp.login("84551813@qq.com","airuchaoshui111")
    # #接收
    # smtp.sendmail("84551813@qq.com","2656020596@qq.com",msg.as_string())
    # smtp.quit()
