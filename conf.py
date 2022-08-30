import os.path


class Config(object):
    """项目的配置文件"""


    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:a123456@127.0.0.1:3306/flask_qa"

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = 'asdfsdfsd'
    # 文件上传目录
    MEDIA_ROOT = os.path.join(os.path.dirname(__file__),'medias')
