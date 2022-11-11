<<<<<<< HEAD
from flask import Flask, session, g
from flask_login import LoginManager

from models import db, User
from accounts.views import accounts
from qa.views import qa
from utils.filters import number_split, dt_format_show
from  flask_ckeditor import CKEditor

app = Flask(__name__,static_folder='medias')

# 从配置文件加载配置
app.config.from_object('conf.Config')

# 数据库初始化
db.init_app(app)
# 富文本初始化
ckeditor = CKEditor(app)

# 注册蓝图
app.register_blueprint(accounts,url_prefix='/accounts')
app.register_blueprint(qa,url_prefix='/')

# 注册过滤器
app.jinja_env.filters['number_split'] = number_split
app.jinja_env.filters['dt_format_show'] = dt_format_show

=======


from flask import Flask, session, g
from accounts.views import accounts
from qa.views import qa
from flask_login import LoginManager
from flask_ckeditor import CKEditor


from models import db, User
from utils.filters import number_split, dt_format_show

app = Flask(__name__,static_folder='medias')

app.config.from_object('conf.Config')


# 数据库初始化
db.init_app(app)

# 富文本初始化
ckeditor = CKEditor(app)

>>>>>>> 0f0671da8c1f08f7141d72655d2b426353749f87
# 登录验证
login_manager = LoginManager()
login_manager.login_view = 'accounts.login'
login_manager.login_message = '请登录'
login_manager.login_message_category = 'danger'
login_manager.init_app(app)


<<<<<<< HEAD
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
=======

app.register_blueprint(accounts,url_prefix='/accounts')
app.register_blueprint(qa,url_prefix='/')


app.jinja_env.filters['number_split'] = number_split
app.jinja_env.filters['dt_format_show'] = dt_format_show
>>>>>>> 0f0671da8c1f08f7141d72655d2b426353749f87


# @app.before_request
# def before_request():
<<<<<<< HEAD
#     """如果有用户id,设置到全局对象"""
#     user_id = session.get('user_id',None)
#     if user_id:
#         user = User.query.get(user_id)
#
#         g.current_user = user


=======
#     user_id= session.get('user_id',None)
#     if user_id:
#         user = User.query.get(user_id)
#         g.current_user = user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
>>>>>>> 0f0671da8c1f08f7141d72655d2b426353749f87
