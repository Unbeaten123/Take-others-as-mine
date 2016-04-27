# -*- coding: utf-8 -*-
# QQ邮箱SMTP授权码（作邮箱密码使用）apmzehtpulhxbbjd
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

#输入发件人邮箱
from_addr = raw_input('From: ')
#输入QQ邮箱授权码
password = raw_input('Password: ')
#输入接受者的邮箱
to_addr = raw_input('To: ')
#输入SMTP服务器
smtp_server = raw_input('SMTP server: ')
#输入邮件内容
text_content = raw_input('Content:')

msg = MIMEText(text_content, 'plain', 'utf-8')
msg['From'] = _format_addr(u'余志州 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自狂拽帅气吊炸天的GodZhou！', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 587)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
