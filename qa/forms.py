import os.path

from flask import current_app
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField,FileField
from wtforms.validators import DataRequired, Length
from flask_ckeditor import CKEditorField

from models import Question, db, QuestionTags, Answer


class WriteQuestionForm(FlaskForm):
    """写文章/问题"""

    img = FileField(label='上传图片',render_kw={
        'accept':'.jpeg,.jpg,.png'
    },validators=[FileAllowed(['png','jpg','jpeg'],'请选择合适的图片类型')])

    title = StringField(label='标题',render_kw={
        'class':"form-control",
        'placeholder': "请输入标题（最多50个字）"
    },validators=[DataRequired('请添加标题'),Length(min=5,max=50,message='标题长度为5——50个字')])

    tags = StringField(label='标签',render_kw={
        'class':"form-control",
        'placeholder': "输入标签，用,分隔"
    })

    desc = StringField(label='描述',render_kw={
        'class':"form-control",
        'placeholder': "描述"
    })
    content = CKEditorField(label='文章内容',render_kw={
        'class':"form-control",
        'placeholder': "请输入正文"
    })


    def save(self):

        # 1.保存图片
        img = self.img.data
        img_name=''
        if img:
            img_name = secure_filename(img.filename)
            img_path = os.path.join(current_app.config['MEDIA_ROOT'], img_name)
            print(img_path)
            img.save(img_path)


        title = self.title.data
        tags = self.tags.data
        desc = self.desc.data
        content = self.content.data

        obj = Question(title=title,desc=desc,content=content,user=current_user,img=img_name)
        db.session.add(obj)

        # 保存标签
        tags = tags.split('，')
        for tag_name in tags:
            if tag_name:
                tag_obj = QuestionTags(tag_name=tag_name,question=obj)
                db.session.add(tag_obj)
        db.session.commit()

class WriteAnswerForm(FlaskForm):
    content = CKEditorField(label="回答",validators=[DataRequired('请填写回答')])

    def save(self,question):
        content = self.content.data
        con_obj = Answer(content=content,user=current_user,question=question)
        db.session.add(con_obj)
        db.session.commit()
        return con_obj
