from flask import Flask, render_template, session, redirect, url_for
from . import main
from . forms import AddTask
from .. import db
from ..models import Task, User

@main.route('/')
def index():

	return render_template('index.html')


@main.route('/task', methods=['GET', 'POST'])
def task():
	form = AddTask()
	if form.validate_on_submit():
		task = Task.query.filter_by(name=form.name.data).first()
		if task is None:
			name = Task(name=form.name.data)
			db.session.add(name)
			db.session.commit()
			session['known'] = False
		else:
			session['known'] = True
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('main.task'))
	return render_template('my_tasks.html', form=form, name=session.get('name'), known=session.get('known', False))


# @main.route('/user/<username>')
# def user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     return render_template('user.html', username=username)
    

