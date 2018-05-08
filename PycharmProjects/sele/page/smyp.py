import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.header import Header

fp = open('lifug.html',"rb")
mailbody = fp.read()
#print(mailbody)
fp.close()

use ="84551813@qq.com"
psw = "mwdhjfnxzmkocafd"
msg = MIMEText(mailbody,"html","utf-8")
    #设计邮件主题
msg["subject"] = Header("hahhahah","utf-8")

smtpp = smtplib.SMTP_SSL("smtp.qq.com",465)

    #连接服务器
#smtp.connect("mail.qq.com")
    #登录
smtpp.login(use,psw)
    #接收
smtpp.sendmail("84551813@qq.com","2656020596@qq.com",msg.as_string())
smtpp.quit()