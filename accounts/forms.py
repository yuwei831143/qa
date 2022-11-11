import hashlib

from flask import request
from flask_login import login_user
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from models import User, db, UserProfile, UserLoginHistory
from utils import constants
from utils.validators import phone_required


class RegisterForm(FlaskForm):
    """用户注册"""
    username = StringField(label='用户名',render_kw={
        'class':'form-control input-lg',
        'placeholder':'请输入用户名'
    },validators=[DataRequired('请输入用户名'),phone_required])
    nickname = StringField(label='昵称',render_kw={
        'class':'form-control input-lg',
        'placeholder':'请输入昵称'
    },validators=[DataRequired('请输入昵称'),Length(min=2,max=20,message='昵称长度在2-20之间')])
    password = PasswordField(label='密码',render_kw={
        'class':'form-control input-lg',
        'placeholder':'请输入密码'
    },validators=[DataRequired('请输入密码')])
    confirm_password = PasswordField(label='确认密码',render_kw={
        'class':'form-control input-lg',
        'placeholder':'再次输入密码'
    },validators=[DataRequired('请再次输入密码'),
                  EqualTo('password',message='两次密码输入不一致')])


    def validate_username(self,field):
        """检测用户名是否已经存在"""
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError('该用户名已存在')

    def register(self):
        # 1.获取表单信息
        # 2.添加到db.session

        username = self.username.data
        password = self.password.data
        nickname = self.nickname.data

        try:
            # 将密码加密存储
            password = hashlib.sha256(password.encode()).hexdigest()
            user_obj = User(username=username, password=password, nickname=nickname)
            db.session.add(user_obj)
            profile = UserProfile(username=username, user=user_obj)
            db.session.add(profile)
            db.session.commit()
            return user_obj
        except Exception as e:
            print(e)
        return None


class LoginForm(FlaskForm):

    username = StringField(label='用户名',render_kw={
        'class': 'form-control input-lg',
        'placeholder':"请输入用户名"
    },validators=[DataRequired('请输入用户名'),phone_required])
    password = PasswordField(label='密码',render_kw={
        'class': 'form-control input-lg',
        'placeholder': "请输入密码"
    },validators=[DataRequired('请输入密码')])

    def validate(self):
        result = super().validate()
        username = self.username.data
        password = self.password.data

        if result:
            user = User.query.filter_by(username=username,password=password).first()
            if user is None:
                result = False
                self.username.errors = ['用户名或密码错误']
            elif user.status == constants.UserStatus.USER_IN_ACTIVE.value:
                result = False
                self.username.errors = ['用户已被禁用']
        return result

    def do_login(self):

        try:
            username = self.username.data
            password = self.password.data
            user = User.query.filter_by(username=username, password=password).first()
            # session['user_id'] = user.id
            login_user(user)
            # 记录日志
            ip = request.remote_addr
            ua = request.headers.get('user-agent', None)
            obj = UserLoginHistory(username=username, ip=ip, ua=ua, user=user)
            db.session.add(obj)
            db.session.commit()
            return user
        except Exception as e:
            print(e)

        return None





