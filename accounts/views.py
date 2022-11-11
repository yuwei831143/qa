<<<<<<< HEAD
import hashlib

from flask import render_template, flash, redirect, url_for, session, request
from flask import Blueprint
from flask_login import login_user, logout_user

from accounts.forms import RegisterForm, LoginForm
=======

from flask import Blueprint, render_template, flash, redirect, url_for, session, request
from flask_login import login_user, logout_user

import constants
from accounts.forms import RegisterForms, Login
>>>>>>> 0f0671da8c1f08f7141d72655d2b426353749f87
from models import User, db, UserProfile, UserLoginHistory

accounts = Blueprint('accounts',__name__,template_folder='templates',static_folder='../assets')

<<<<<<< HEAD
@accounts.route('/login',methods=['POST','GET'])
def login():
    """登录"""
    form = LoginForm()
    # 获取上一次的url没有跳转首页
    next_url = request.values.get('next', url_for('qa.index'))
    if form.validate_on_submit():
        user = form.do_login()
        if user:
            flash('{}欢迎回来'.format(user.nickname),'success')
            return redirect(next_url)
        else:
            flash('登录失败,请稍后再试','danger')
    else:
        print(form.errors)


    return render_template('login.html',form=form,next_url=next_url)

@accounts.route('/logout')
def logout():
    """退出登出"""
    logout_user()
    flash('欢迎下次再来','success')
    return redirect(url_for('accounts.login'))

@accounts.route('/register',methods=['POST','GET'])
def register():
    """注册"""
    form = RegisterForm()
    if form.validate_on_submit():
        user_obj = form.register()
        if user_obj:
            flash('注册成功请登录','success')
            return redirect(url_for('accounts.login'))
        else:
            flash('注册失败，请稍后再试','danger')
=======

@accounts.route('/login',methods=["POST","GET"])
def login():
    """登录"""
    form = Login()
    next_url = request.values.get('next', url_for('qa.index'))
    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username,password=password).first()
        if user is None:
            flash('用户名或者密码错误','danger')
        elif user.status == constants.UserStatus.USER_IN_ACTIVE.value:
            flash('用户已被禁用','danger')
        else:

            # session['user_id'] = user.id
            login_user(user)
            # 记录登录日志
            ip = request.remote_addr
            ua = request.headers.get('user-agent',None)
            obj = UserLoginHistory(username=username,ip=ip,ua=ua,user=user)
            db.session.add(obj)
            db.session.commit()

            flash('{},欢迎回来'.format(user.nickname), 'success')
            return redirect(next_url)
    else:
        print(form.errors)
    return render_template('login.html',form=form,next_url=next_url)

@accounts.route('/register',methods=['POST','GET'])
def register():
    """注册"""
    form = RegisterForms()
    if form.validate_on_submit():
        # 获取表单信息
        # 获取db.session
        # 跳转成功页面
        username = form.username.data
        password = form.password.data
        nickname = form.nickname.data

        try:
            user_obj = User(username=username,password=password,nickname=nickname)
            db.session.add(user_obj)
            profile = UserProfile(username=username,user=user_obj)
            db.session.add(profile)
            db.session.commit()

            flash('注册成功，请登录','success')
            return redirect(url_for('accounts.login'))
        except Exception as e:
            print(e)
            flash('注册失败','danger')
>>>>>>> 0f0671da8c1f08f7141d72655d2b426353749f87

    return render_template('register.html',form=form)


@accounts.route('/mine')

def mine():
    """个人中心"""
<<<<<<< HEAD
    return render_template('mine.html')
=======
    return render_template('mine.html')


@accounts.route('/logout')
def logout():
    """退出登录"""
    logout_user()
    flash('欢迎下次再来','success')
    return redirect(url_for('accounts.login'))
>>>>>>> 0f0671da8c1f08f7141d72655d2b426353749f87
