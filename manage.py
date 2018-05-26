#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.model import Role
from app.view import *
from flask_script import Manager

manager = Manager(app)
"""用于启动程序、初始化db等任务"""


# manager.add_command("shell", Shell(make_context=make_shell_context))
@manager.shell
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@manager.command
def drop():
    db.drop_all()


@manager.command
def init():
    db.create_all()
    role = Role('admin')
    db.session.add(role)
    for i in range(5):
        db.session.add(User('user{}'.format(i), role))
    db.session.commit()


@manager.command
def rebuildb():
    db.drop_all()
    db.create_all()


@manager.command
def run():
    app.run(debug=True)


if __name__ == '__main__':
    manager.run()
