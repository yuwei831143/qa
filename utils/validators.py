import re

from wtforms import ValidationError


def phone_required(form,field):
    """自定义的手机号码的验证"""

    username = field.data
    pattern = r'^1[0-9]{10}$'
    if not re.search(pattern,username):
        raise ValidationError('请输入手机号码')
    return field