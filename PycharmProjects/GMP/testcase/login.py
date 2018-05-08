
from selenium import webdriver
import  HTMLTestRunner
from pages.searchPage import SearchPage
from selenium.webdriver.common.by import By
import unittest
import time


class testSchGmp(unittest.TestCase):
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

    # def test_b_GLMB024(self):
    #     '''修改状态为有效，发送中心该模板状态是否相应变化'''
    #     self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
    #     self.xuanze = (By.XPATH,'//*[@id="smsAdmincId"]/tr[4]/td[2]/input')
    #     self.searpage.click_time(self.xuanze,0.2)
    #     self.searpage.click_time(self.searpage.shen_click,1)
    #     self.driver.find_element_by_id('sts').click()
    #     self.id_s0 = (By.ID,'s0')
    #     self.searpage.click_time(self.id_s0,0.5)
    #     self.searpage.click_time(self.searpage.btn_success,1)
    #     self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'审核成功')
    #     self.assertEqual(self.searpage.base_get_text(self.searpage.youxiao_5),'有效')
    #
    # def test_b_GLMB025(self):
    #     '''修改状态为待审核，发送中心该模板状态是否相应变化'''
    #     self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
    #     self.xuanze = (By.XPATH,'//*[@id="smsAdmincId"]/tr[4]/td[2]/input')
    #     self.searpage.click_time(self.xuanze,0.2)
    #     self.searpage.click_time(self.searpage.shen_click,1)
    #     self.driver.find_element_by_id('sts').click()
    #     #self.id_s0 = (By.ID,'s0')
    #     self.id_s2 = (By.ID,'s2')
    #     self.searpage.click_time(self.id_s2,0.5)
    #     self.searpage.click_time(self.searpage.btn_success,1)
    #     self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'审核成功')
    #     self.assertEqual(self.searpage.base_get_text(self.searpage.daishen_xpath),'待审核')
    #
    #
    # def test_b_GLMB027(self):
    #     '''选择多个账号状态一样的模板进行审核'''
    #     self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
    #     self.js = "window.scrollTo(0,200)"
    #     self.driver.execute_script(self.js)
    #     time.sleep(3)
    #     self.xuanze_8 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[8]/td[2]/input')
    #     self.xuanze_9 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[9]/td[2]/input')
    #     self.searpage.clickAndClick(self.xuanze_8,self.xuanze_9)
    #     self.js = "window.scrollTo(0,0)"
    #     self.driver.execute_script(self.js)
    #     time.sleep(3)
    #     self.searpage.click_time(self.searpage.shen_click,1)
    #     self.driver.find_element_by_id('sts').click()
    #     self.id_s0 = (By.ID,'s0')
    #     self.searpage.click_time(self.id_s0,0.5)
    #     self.searpage.click_time(self.searpage.btn_success,1)
    #     self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'审核成功')
    #     self.assertEqual(self.searpage.base_get_text(self.searpage.youxiao_8),'有效')
    #     self.assertEqual(self.searpage.base_get_text(self.searpage.youxiao_9),'有效')
    #
    # def test_b_GLMB028(self):
    #     '''编辑时账号ID，模板内容，状态信息是否回显'''
    #     self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
    #     self.searpage.click_time(self.searpage.bianji_3,1)
    #     self.driver.find_element_by_id('st')
    #     self.driver.find_element_by_id('st0').click()
    #     self.bianji_shen = (By.XPATH,'//*[@id="myModal-examine"]/div/div/div[3]/button[2]')
    #     self.searpage.click_time(self.bianji_shen,1)
    #     self.assertEqual(self.searpage.base_get_text(self.searpage.youxiao_4),'有效')
    #
    # def test_b_GLMB029(self):
    #     '''模板内容为空时，能否提交成功'''
    #     self.driver.get('http://10.1.63.125:8080/gmp/admin#/smstemplate')
    #     self.searpage.click_time(self.searpage.bianji_3,1)
    #     self.driver.find_element_by_id('ctpl').clear()
    #     self.bianji_shen = (By.XPATH,'//*[@id="myModal-examine"]/div/div/div[3]/button[2]')
    #     self.searpage.click_time(self.bianji_shen,1)
    #     self.assertEqual(self.searpage.base_get_text(self.searpage.spnMessage_id),'模板内容不能为空')

    # def test_b_GLMB030(self): 没有做校验
    #     '''模板内容输入65个字符'''
    #     self.searpage.click_time(self.searpage.bianji_3,1)
    #     self.aa = self.driver.find_element_by_id('remarks').get_attribute('maxlength'






    # def test_zzz(self):
    #     '''退出浏览器'''
    #     self.driver.quit()



    def tearDown(self):
        self.driver.refresh()
        time.sleep(0.5)
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(testSchGmp))

    timestr=time.strftime('%Y%m%d%H%m%S', time.localtime(time.time()))

    # 报告路径fp = open('./ka.html', 'wb')
    fp = open('/Users/sy/PycharmProjects/GMP/config/result'+timestr+'.html',"wb")
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="自动化测试报告",description="审核模板,短信模板")

    # runner = unittest.TextTestRunner()
    runner.run(suit)

    #mailbody = fp.read()

    fp.close()

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
