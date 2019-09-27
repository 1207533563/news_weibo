import requests,re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os,time


def mail(msg):
    mail_host="smtp.qq.com"  #设置服务器
    mail_user="1207533563@qq.com"    #用户名
    mail_pass="rburcnlxeskjggde"   #口令 
            
    sender = '1207533563@qq.com'
    receivers = ['736456849@qq.com','2441908854@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
            
    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header("11", 'utf-8')
    message['To'] =  Header("热搜", 'utf-8')

    subject = '实时热搜'
    message['Subject'] = Header(subject, 'utf-8')
            
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host) 
        smtpObj.connect(mail_host, 465)    # 465 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
            #smtplib.quit()
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print ("Error: 无法发送邮件")

    
if os.path.isfile('weibo.txt'):
    os.remove('weibo.txt')
else:
    pass
rsp = requests.get("http://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6")
rsp.encoding = "utf-8"
data = rsp.text
wb = re.findall(r'<a href="(/weibo.*?)" target="_blank">(.*?)</a>',data,flags=re.S)

with open("weibo.txt",'a') as f:
    for i in range(10):
        key = 's.weibo.com'+ wb[i][0]
        print(key)
        tmp = re.search('q=(.*?)&',key).group(1)
        nmp = "%23"+ wb[i][1] +"%23"
        key = re.sub(tmp,nmp,key)
        f.write(wb[i][1]+' '+'链接：'+key+'\n')
with open("weibo.txt",'r') as r:
    msg = r.read()
mail(msg)
 
