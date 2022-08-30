
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,EqualTo,ValidationError

from models import User
from utils.validators import phone_required


class RegisterForms(FlaskForm):
    """用户注册"""
    username = StringField(label='用户名',render_kw={
        'class':'form-control input-lg',
        'placeholder':'请输入用户名'
    },validators=[DataRequired('请输入用户名'),phone_required])
    nickname = StringField(label='用户昵称',render_kw={
        'class':'form-control input-lg',
        'placeholder':'请输入昵称'
    },validators=[DataRequired('密码')])
    password = PasswordField(label='密码',render_kw={
        'class':'form-control input-lg',
        'placeholder':'请输入用户密码'
    },validators=[DataRequired('昵称')])
    confirm_password = PasswordField('确认密码',render_kw={
        'class':'form-control input-lg',
        'placeholder':'请确认密码'
    },validators=[DataRequired('请重新输入密码'),EqualTo('password','两次密码输入不一致')])


    def validate_username(self,field):

        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError('该用户名已存在')
        return field


class Login(FlaskForm):

    username = StringField(label='用户名',render_kw={
        'class':'form-control input-lg',
        'placeholder':'请输入用户名'
    })
    password = PasswordField(label="密码",render_kw={
        'class':'form-control input-lg',
        'placeholder':'请输入密码'
    })




