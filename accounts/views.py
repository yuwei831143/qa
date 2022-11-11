import hashlib

from flask import render_template, flash, redirect, url_for, session, request
from flask import Blueprint
from flask_login import login_user, logout_user

from accounts.forms import RegisterForm, LoginForm
from models import User, db, UserProfile, UserLoginHistory

accounts = Blueprint('accounts',__name__,template_folder='templates',static_folder='../assets')

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

    return render_template('register.html',form=form)


@accounts.route('/mine')

def mine():
    """个人中心"""
    return render_template('mine.html')