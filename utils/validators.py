import re

from wtforms import ValidationError


<<<<<<< HEAD
def phone_required(form,field):
    """自定义的手机号码的验证"""

    username = field.data
    pattern = r'^1[0-9]{10}$'
    if not re.search(pattern,username):
        raise ValidationError('请输入手机号码')
    return field
=======
def phone_required(form,filed):

    username = filed.data
    pattern = r'^1[0-9]{10}$'
    if not re.search(pattern,username):
        raise ValidationError('请输入手机号码')
    return filed
>>>>>>> 0f0671da8c1f08f7141d72655d2b426353749f87
