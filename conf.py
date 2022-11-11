import os.path


class Config(object):

    """项目的配置文件"""

    # 数据库连接URI
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:a123456@127.0.0.1:3306/flask_qa"
    # 这个配置将来会被禁用,设置为True或者False可以解除警告信息,建议设置False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'acvdfddfddfd23'

    # 文件上传的根路径

    MEDIA_ROOT = os.path.join(os.path.dirname(__file__),'medias')
