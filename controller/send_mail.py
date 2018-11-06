#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 11:05
# @Author  : Fred Yang
# @File    : send_mail.py
# @Role    : API发送邮件

import json
import requests
import tornado.web





def get_main_settings():
    api = 'http://172.16.0.101:9000/app_settings'
    r = requests.get(api)
    r_data = json.loads(r.text)
    data = r_data['data']
    print(data)





get_main_settings()


def send_main():
    pass

#
# class SendMailHandler(tornado.web.RequestHandler):
#     def get(self, *args, **kwargs):
#         pass
#
#     def post(self, *args, **kwargs):
#         data = json.loads(self.request.body.decode('utf-8'))
#         name = data.get('name', None)
#         value = data.get('value', None)
#
#
#
# def send_mail(content, email):
#     '''定义发送邮件'''
#     # mail_to_list = ['xxx@xxxx.com', 'xxxx@qq.com']
#     mail_to_list = [email]
#     mail_host = EMAIL_INFO['host']
#     mail_user = EMAIL_INFO['user']
#     mail_password = EMAIL_INFO['password']
#     subject = "%s: OpenDevOps平台事件提醒" % (time.ctime())
#     msg = MIMEText(content, _subtype="html", _charset="gb2312")
#     msg['Subject'] = subject
#     msg['From'] = mail_user
#     msg["To"] = ','.join(mail_to_list)
#
#     try:
#         mail = smtplib.SMTP()
#         mail.connect(mail_host)
#         mail.login(mail_user, mail_password)
#         mail.sendmail(mail_user, mail_to_list, msg.as_string())
#         mail.close()
#         return True
#     except (Exception,) as e:
#         print(e)