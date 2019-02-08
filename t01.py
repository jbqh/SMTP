#!/home/py36/bin/python3

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
            #print('mail send failed')
        
    def __msg__(self,*args):
        msg = MIMEText(args[3],self.mimetype,'utf-8')
        msg['From'] = args[0]
        msg['To'] = args[1]
        msg['Subject'] = args[2]
        
        return msg.as_string()
        
host = 'mail.vdin.net'
port = 25
username ='jiangbin'
password = 'j123456'
mimetype = 'html'
mail_from ='bin.jiang@vdin.net'
mail_to = 'jbqh@qq.com'
subject = 'smtp plain test'
body = '<font size=5 color=red><b>send at: %s</b></font>' % time.strftime('%F %T')

smtp = MySMTP(host,port,username,password,mimetype)
smtp.sendmail(mail_from,mail_to,subject,body)
