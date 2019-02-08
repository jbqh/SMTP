#!/home/py36/bin/python3
#-*-coding:utf-8

import time
import smtplib
from email.mime.text import MIMEText

class MySMTP(smtplib.SMTP):
    def __init__(self,host,port,username,password,mimetype='plain'):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.mimetype = mimetype
        
    def sendmail(self,mail_from,mail_to,subject,body):
        msg = self.__msg__(mail_from,mail_to,subject,body)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.host,self.port)
            smtp.login(self.username,self.password)
            smtp.sendmail(mail_from,mail_to,msg)
            print('mail send successful')
         
        except Exception as e:
            print(e)
           
    def __msg__(self,*args):
        msg = MIMEText(args[3],self.mimetype,'utf-8')
        msg['From'] = args[0]
        msg['To'] = ','.join(args[1])
        msg['Subject'] = args[2]
        
        return msg.as_string()
        
#定义服务器服务器信息        
host = MAIL_SERVER
port = SMTP_PORT
username = LOGIN_NAME
password = LOGIN_PASSWORD

#mimetype:邮件正文格式
#   html:支持html格式
#   plain:纯文本格式
mimetype = 'html'

#邮件信息
mail_from = SENDER_USER_MAIL
mail_to = [RECEIVER_USER_MAIL] #list
subject = MAIL_SUBJECT
body = MAIL_BODY

smtp = MySMTP(host,port,username,password,mimetype)
smtp.sendmail(mail_from,mail_to,subject,body)
