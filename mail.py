#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hello import *
from flask_mail import  Message, Mail

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
# send a mail

if __name__ == '__main__':
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'],
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=["393231175@qq.com"])
    msg.body = "123"
    msg.html = "dsf"
    with app.app_context():
        mail.send(msg)