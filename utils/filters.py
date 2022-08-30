from datetime import datetime

import timeago


def number_split(num):


    return '{:,}'.format(int(num))

def dt_format_show(dt):

    """日期格式化显示"""

    now = datetime.now()
    return timeago.format(dt,now,'zh_CN')