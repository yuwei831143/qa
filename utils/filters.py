from datetime import datetime

import timeago


def number_split(num):
<<<<<<< HEAD
    """数字格式化"""

    return '{:,}'.format(int(num))


def dt_format_show(dt):
    """日期和时间格式化显示"""
=======


    return '{:,}'.format(int(num))

def dt_format_show(dt):

    """日期格式化显示"""

>>>>>>> 0f0671da8c1f08f7141d72655d2b426353749f87
    now = datetime.now()
    return timeago.format(dt,now,'zh_CN')