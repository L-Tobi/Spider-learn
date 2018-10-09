import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host='smtp.163.com'
mail_user=''
mail_password=''

sender = ''
receiver = ['1346763205@qq.com']
with open ('C:/Users/Tobi/Desktop/key.txt','r') as login_info:
    login_message = login_info.read()
    results = login_message.split(' ')
    mail_user = results[0]
    mail_password = results[1]
    sender = mail_user

message = MIMEText(' Exception ','plain','utf-8')
message['From'] = Header('Server ', 'utf-8')
message['To'] = Header('Tobi', 'utf-8')

subject = '邮件发送测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    print(type(mail_user), type(mail_password))
    smtpObj.login(mail_user, mail_password)
    smtpObj.sendmail(sender,receiver,message.as_string())
    print('邮件发送成功')
except Exception as e:
    print('邮件发送失败 ' , str(e))