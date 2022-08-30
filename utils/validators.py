import re

from wtforms import ValidationError


def phone_required(form,filed):

    username = filed.data
    pattern = r'^1[0-9]{10}$'
    if not re.search(pattern,username):
        raise ValidationError('请输入手机号码')
    return filed