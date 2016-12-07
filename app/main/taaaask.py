@main.route('/task', methods=['GET', 'POST'])
def task():
	form = AddTask()
	cat = Category.query.all()
	
	category_id=Task.category_id
	username=current_user.username
	user = User.query.filter_by(username=username).first()
	# tasks_per_category = Task.query.filter_by(category_id=category_id).all() 
	
	if form.validate_on_submit():
		task = Task(name=form.name.data,
					prerequisites =form.prerequisites.data,
					due_date=form.due_date.data,
					user =current_user._get_current_object(),
					category =category
					)

		db.session.add(task)
		
		return redirect(url_for('main.task'))
	tasks = user.tasks.order_by(Task.due_date.asc()).all()


	return render_template('my_tasks.html', form=form, tasks=tasks, user=user, cat=cat)

# html form
task = Task(name=request.form['name'],
					prerequisites =request.form['prerequisites'],
					due_date=request.form['due_date'],
					user =current_user._get_current_object(),
					category =category
					)

# html form date attrib erro

from flask import (Flask, render_template, session, redirect,
 url_for, request, flash)
from flask.ext.login import login_required, current_user
from . import main
from . forms import AddTask, AddCategory
from .. import db
from ..models import Task, User, Category, Role

@main.route('/')
def index():

	return render_template('index.html')


@main.route('/task', methods=['GET', 'POST'])
def task():
	# form = AddTask()
	cat = Category.query.all()
	# form.C_name.choices = [(category.id, category.name) for category in cat]
	# cat = Category.query.all()
	inbox = Category.query.first()
	
	# category_id=Task.category_id
	username=current_user.username
	user = User.query.filter_by(username=username).first()
	
	
	
	
	# if form.validate_on_submit():
	# task = Task(name=request.form['name'],
	# 			prerequisites =request.form['prerequisites'],
	# 			due_date=request.form['due_date'],
	# 			user =current_user._get_current_object(),
	# 			category = inbox
	# 			)

	# db.session.add(task)
		
		# return redirect(url_for('main.task'))
	tasks = user.tasks.order_by(Task.due_date.asc()).all()


	return render_template('my_tasks.html', tasks=tasks, user=user, cat=cat)

@main.route('/category', methods=['GET', 'POST'])
def category():
	category = Category(name=request.form['category_name'])
	db.session.add(category)
	flash('Category added')

	return redirect(url_for('main.task'))

@main.route('/tasks/<int:id>', methods=['GET', 'POST'])
def tasks(id):
	cat = Category.query.all()
	form = AddTask()
	# form.C_name.choices = [(category.id, category.name) for category in Category.query.all()]
	
	category_id=Task.category_id
	username=current_user.username
	user = User.query.filter_by(username=username).first()
	
	# tasks_per_category = Task.query.filter_by(category_id=category_id).all() 
	# if form.validate_on_submit():
	# task = Task(name=request.form['name'],
	# 			prerequisites =request.form['prerequisites'],
	# 			due_date=request.form['due_date'],
	# 			user =current_user._get_current_object(),
	# 			category_id = id
	# 			)

	# db.session.add(task)
		
		# return redirect(url_for('main.task'))
	tasks=Task.query.filter_by(category_id=id).all()

	return render_template('my_tasks.html', tasks=tasks, user=user, cat=cat)

@main.route('/addtask', methods=['GET', 'POST'])
def edit_task():
	inbox = Category.query.first()
	task = Task(name=request.form['name'],
				prerequisites =request.form['prerequisites'],
				due_date=request.form['due_date'],
				user=current_user._get_current_object(),
				category=inbox)

	db.session.add(task)
	
	return redirect(url_for('main.task'))





















	# username=current_user.username
	# user = User.query.filter_by(username=username).first()
	# cat = Category.query.all()

	# tasks=Task.query.filter_by(category_id=id).all()
	

	# return render_template('my_tasks.html', tasks=tasks, user=user, cat=cat)





















	
	

	
	
		
