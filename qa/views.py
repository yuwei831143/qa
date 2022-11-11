<<<<<<< HEAD
from flask import render_template, request, abort, flash, redirect, url_for, jsonify
from flask import Blueprint
=======
from flask import Blueprint, render_template, request, abort, flash, redirect, url_for, jsonify
>>>>>>> 0f0671da8c1f08f7141d72655d2b426353749f87
from flask_login import login_required, current_user

from models import Question, Answer, AnswerComment, db
from qa.forms import WriteQuestionForm, WriteAnswerForm

<<<<<<< HEAD
qa = Blueprint('qa', __name__, template_folder='templates', static_folder='../assets')


@qa.route('/')
def index():
    """ 首页 回答列表"""
    per_page = 20
    page = int(request.args.get('page', 1))
    page_data = Answer.query.filter_by(is_valid=True).paginate(page=page, per_page=per_page)

    return render_template('index.html',page_data=page_data)


@qa.route('/follow')
def follow():
    """关注"""
    per_page = 20
    page = int(request.args.get('page',1))
    page_data = Question.query.filter_by(is_valid=True).paginate(page=page,per_page=per_page)

    return render_template('follow.html',page_data=page_data)

@qa.route('/qa/list')
def question_list():
    """查询问题数据列表"""
    try:
        per_page = 2
        page = int(request.args.get('page', 1))
        page_data = Question.query.filter_by(is_valid=True).paginate(page=page, per_page=per_page)
        data = render_template('qa_list.html',page_data=page_data)
        return {'code':0,'data':data}
    except Exception as e:
        print(e)
        data = ''
    return {'code':1,'data':data}


@qa.route('/detail/<int:q_id>',methods=['POST','GET'])
def detail(q_id):
    """详情"""
    question = Question.query.get(q_id)
    if not question.is_valid:
        abort(404)

    # 展示第一条回答
=======
qa = Blueprint('qa',__name__,template_folder='templates',static_folder='../assets')


@qa.route('/')
def index():  # put application's code here
    """首页"""
    per_page = 20
    # 获取当前页
    page = request.args.get('page',1)
    page_data = Answer.query.filter_by(is_valid=True).paginate(page=page,per_page=per_page)
    return render_template('index.html',page_data=page_data)


# @qa.route('/follow')
# def follow():
#     """关注"""
#     per_page = 20
#     page = int(request.args.get('page',1))
#     page_data = Question.query.filter_by(is_valid=True).paginate(page=page,per_page=per_page)
#     return render_template('follow.html',page_data=page_data)

@qa.route('/follow')
def follow():
    """ 关注 """
    per_page = 20  # 每页数据的大小
    page = int(request.args.get('page', 1))
    page_data = Question.query.filter_by(is_valid=True).paginate(
        page=page, per_page=per_page)
    return render_template('follow.html', page_data=page_data)



# @qa.route('/detail/<int:q_id>')
# def detail(q_id):
#     """详情"""
#     question = Question.query.get(q_id)
#     if question.is_valid is False:
#         abort(404)
#
#     answer = question.answer_list.query.filter_by(is_valid=True).first()
#
#     return render_template('detail.html',question=question,answer=answer)

@qa.route('/detail/<int:q_id>',methods=['POST','GET'])
def detail(q_id):
    """ 问题详情 """
    # 1. 查询问题信息
    question = Question.query.get(q_id)
    if not question.is_valid:
        abort(404)
    # 2. 展示第一条回答信息
>>>>>>> 0f0671da8c1f08f7141d72655d2b426353749f87
    answer = question.answer_list.filter_by(is_valid=True).first()

    # 添加回答
    form = WriteAnswerForm()
    if form.validate_on_submit():
        try:
            if not current_user.is_authenticated:
<<<<<<< HEAD
                return redirect(url_for('accounts.login'))
            form.save(question=question)
            flash('回答问题成功','success')
            return redirect(url_for('qa.detail',q_id=q_id))

        except Exception as e:
            print(e)
    return render_template('detail.html',question=question,answer=answer,form=form)
=======
                flash('请先登录','danger')
                return redirect(url_for('account.login'))
            form.save(question=question)
            flash('回答问题成功','success')
            return redirect(url_for('qa.detail',q_id=q_id))
        except Exception as e:
            print(e)
            print(form.errors)
    return render_template('detail.html', question=question, answer=answer,form=form)
>>>>>>> 0f0671da8c1f08f7141d72655d2b426353749f87


@qa.route('/write',methods=['POST','GET'])
@login_required
def write():
<<<<<<< HEAD
    """发布问题页"""
    form = WriteQuestionForm()
    if form.validate_on_submit():
        try:
            que_obj = form.save()
            if que_obj:

                flash('发布问题成功','success')
                return redirect(url_for('qa.index'))
        except Exception as e:
            print(e)
        else:
            flash('发布失败','danger')

    return render_template('write.html',form=form)


@qa.route('/comment/<int:answer_id>',methods=['POST','GET'])
def comments(answer_id):
    """评论"""
    answer = Answer.query.get(answer_id)
    question = answer.question


    if request.method == 'POST':
        try:
            # 获取数据，保存到数据库
            if not current_user.is_authenticated:
                result = {'code':1,'message':'请登录'}
                return jsonify(result),401

            content = request.form.get('content','')
            reply_id = request.form.get('reply_id', None)
            content_obj = AnswerComment(content=content,user=current_user,answer=answer,question=question,reply_id=reply_id)
            db.session.add(content_obj)
=======
    """写文章"""
    form = WriteQuestionForm()
    if form.validate_on_submit():
        try:
            form.save()
            flash('发布问题成功','success')
            return redirect(url_for('qa.index'))

        except Exception as e:
            print(e)
            flash('发布问题失败','danger')

    return render_template('write.html',form=form)

@qa.route('/question/list')
def q_list():
    try:
        per_page = 2
        page = int(request.args.get('page',1))
        page_data = Question.query.filter_by(is_valid=True).paginate(page=page,per_page=per_page)

    except Exception as e:
        print(e)


@qa.route('/comments/<int:answer_id>',methods=['POST','GET'])
def comments(answer_id):

    answer = Answer.query.get(answer_id)
    if request.method == 'POST':
        # 添加评论
        try:
            if not current_user.is_authenticated:
                result = {'code':1,'message':'请登录'}
                return jsonify(result),400

            content = request.form.get('content','11')
            reply_id = request.form.get('reply_id')
            question = answer.question
            comment_obj = AnswerComment(content=content,user=current_user,answer=answer,question=question,reply_id=reply_id)
            db.session.add(comment_obj)
            db.session.commit()
            return '', 201
        except Exception as e:
            result = {'code':1,'message':'服务器正忙，请稍后重试'}
            return jsonify(result),400

    else:
        try:
            page = int(request.args.get('page',1))
            page_data = answer.comment_list().paginate(page=page,per_page=3)
            data = render_template('comment.html',page_data=page_data,answer=answer)
            return jsonify({'code':0,'data':data,'meta':{'page':page}}),200
        except Exception as e:
            print(e)
            return jsonify({'code':0,'data':'','message':'服务器正忙'}),500


@qa.route('/comment/love/<int:comment_id>',methods=['POST','GET'])
def comment_love(comment_id):
    """评论点赞"""
    if not current_user.is_authenticated:
        abort(401)
    else:
        try:
            comment_obj = AnswerComment.query.get(comment_id)
            comment_obj.love_count += 1
            db.session.add(comment_obj)
>>>>>>> 0f0671da8c1f08f7141d72655d2b426353749f87
            db.session.commit()
            return '',201
        except Exception as e:
            print(e)
<<<<<<< HEAD
            result = {'code':1,'message':'评论失败'}
        return jsonify(result),400


    else:
        # 获取评论列表
        try:
            page = int(request.args.get('page',1))
            page_data = answer.comment_list().paginate(page=page,per_page=2)
            data = render_template('comments.html',page_data=page_data,answer=answer)
            return jsonify({'code':0,'data':data,'mata':{'page':page}}),200

        except Exception as e:
            print(e)
            return jsonify({'code':1,'data':'','message':'服务器正忙'}),500


@qa.route('/comment/love/<int:comment_id>',methods=['POST'])
@login_required
def comment_love(comment_id):
    """为评论点赞"""
    try:
        if not current_user.is_authenticated:
            return '',401
        comment_obj = AnswerComment.query.get(comment_id)
        comment_obj.love_count += 1
        db.session.add(comment_obj)
        db.session.commit()
        return '',201
    except Exception as e:
        print(e)
        abort(500)
    return '',201

=======
>>>>>>> 0f0671da8c1f08f7141d72655d2b426353749f87

