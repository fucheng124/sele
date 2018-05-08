# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from twisted.python.compat import raw_input
import time
from pages.basePage import Page

class SearchPage(Page):

#搜索账号输入框
    username_id = (By.ID,'accountId')
#密码ID
    password_id = (By.ID,'pwdId')
#验证码
    imgCode_id = (By.ID,'iptloginImgCode')
#登录按钮
    login_button =(By.CLASS_NAME,'state')
#账户
    zhanghu = (By.XPATH,"/html/body/div/aside/div/section/ul/li[5]/a/span[1]")
#短信模板
    duanxin = (By.XPATH,"/html/body/div/aside/div/section/ul/li[5]/ul/li[3]/a")
#查询按钮
    cha_xpath = (By.XPATH,"/html/body/div/div/section[2]/div/div/div/div[1]/div[2]/a[1]")
#GMP 管理中心
    gmp_guanli = (By.CLASS_NAME,"hidden-xs")
#数据管理
    shujuguanli = (By.XPATH,"/html/body/div/aside/div/section/ul/li[7]/a/span[1]")
#模板审核
    moban = (By.XPATH,"/html/body/div/aside/div/section/ul/li[7]/ul/li[6]/a")

#模板审核下的查询按钮
    moban_cha = (By.XPATH,"/html/body/div[1]/div/section[2]/div/div/div/div[1]/div[2]/a[1]")
#模板下的搜索框
    pno_id = (By.ID,"pno")
#模板下的日期开始控件
    iptDateRange_Start_id = (By.ID,'iptDateRange_Start')
#模板下的日期结束控件
    iptDateRange_End_id = (By.ID,'iptDateRange_End')
#模板下分页选项
    pageOptId_id = (By.ID,'pageOptId')
#模板中下一页
    next_page = (By.XPATH,'//*[@id="example1_next"]/a')

#模板下的审核按钮
    shen_click = (By.ID,'examineSms')
#审核模板中确认按钮
    btn_success = (By.XPATH,'//*[@id="myModal-shenhe"]/div/div/div[3]/button[2]')
#无效缘由不能为空
    spnMessage_id = (By.ID,'spnMessage')
#审核模板下的输入框
    remarks_id = (By.ID,'remarks')
    value = 'sa1203174981749817983218749872394798237423652893479387428397492386498237492482379623958239'
#模板中的无效按钮
    stat2_id = (By.ID,'stat2')
#模板中模板ID为5的有效按钮
    youxiao_5 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[4]/td[6]/button')
#模板中模板ID为8的有效按钮
    youxiao_8 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[8]/td[6]/button')
#模板中模板ID为9的有效按钮
    youxiao_9 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[9]/td[6]/button')
#模板中ID为4的有效按钮
    youxiao_4 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[3]/td[6]/button')

#模板中模板ID为5的待审核按钮
    daishen_xpath = (By.XPATH,'//*[@id="smsAdmincId"]/tr[4]/td[6]/span')
#请选择同一状态的模板
    spnMessage_mo = (By.ID,'spnMessage')
#number为3的编辑按钮
    bianji_3 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[3]/td[8]/a[1]')
#number为5的编辑按钮
    bianji_5 = (By.XPATH,'//*[@id="smsAdmincId"]/tr[5]/td[8]/a[1]')
#右上角的删除按钮
    deleteSms_id = (By.ID,'deleteSms')
#短信模板中的新增按钮
    add_class = (By.XPATH,'/html/body/div/div/section[2]/div/div/div/div[1]/div[2]/a[2]')
#添加短信模板输入框
    smstpl_id = (By.ID,'smstpl')
#短信模板中提交审核按钮
    btn_tijiao = (By.XPATH,'//*[@id="myModal1"]/div/div/div[3]/button[2]')

#短信模板下的查询输入框
    smsid = (By.ID,'smsid')
#DTCX查询按钮
    dan_cha = (By.XPATH,'/html/body/div[1]/div/section[2]/div/div/div/div[1]/div/div[2]/a[1]')
#DTCX手机号输入框
    ip_input = (By.ID,'iptMobilePhone')
#DTCXsonID输入框
    sonID = (By.ID,'sonID')
#明细查询中的查询按钮
    aBtnSearch = (By.ID,'aBtnSearch')
    def __init__(self,driver,base_url):
        Page.__init__(self,driver,base_url)
    def goto_Gmppage(self):
        self.driver.get(self.base_url)
        print(self.base_url)

    def login(self):
        self.base_claer(self.username_id)
        self.base_input_text(self.username_id,'admin')
        self.base_claer(self.password_id)
        self.base_input_text(self.password_id,'miao666666')

    def clear_send(self,loc,text):
        self.base_claer(loc)
        self.base_input_text(loc,text)

    def click_time(self,loc,i= 0):
        self.base_click(loc)
        time.sleep(i)

    def clickAndClick(self,loc,loc1):
        self.base_click(loc)
        self.base_click(loc1)

    def get_url_time(self,url,i =0):
        self.base_get_url(url)
        time.sleep(i)

    def is_element_exist(self,xpath):
        s = self.driver.find_elements_by_xpath(xpath)
        if len(s) == 0:
            print( "元素未找到:%s"%xpath)
            return False
        elif len(s) == 1:
            return True
        else:
            print ("找到%s个元素：%s"%(len(s),xpath))
            return False
    def isElementExist(self,xpath):

        try:
            self.driver.find_elements_by_xpath(xpath)
            return True

        except:
            return False