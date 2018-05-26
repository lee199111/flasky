#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_mail import Message
from hello import *

# test to send a mail

if __name__ == '__main__':
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'],
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=["393231175@qq.com"])
    msg.body = "123"
    msg.html = "dsf"
    with app.app_context():
        mail.send(msg)
