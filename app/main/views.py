from flask import (Flask, render_template, session, redirect,
 url_for, request, flash)
from flask.ext.login import login_required, current_user
from . import main
from . forms import AddTask, AddCategory
from .. import db
from ..models import Task, User, Category, Role, Permission
from ..decorators import admin_required, permission_required

@main.route('/')
def index():

	return render_template('index.html')


@main.route('/tasks', methods=['GET', 'POST'])
@login_required
def task():
	form = AddTask()

	cat = Category.query.all()
	# form.C_name.choices = [(category.id, category.name) for category in cat]
	
	inbox = Category.query.first()
	
	# category_id=Task.category_id
	username=current_user.username
	user = User.query.filter_by(username=username).first()
	
	
	# tasks_per_category = Task.query.filter_by(category_id=category_id).all() 
	
	if form.validate_on_submit():
		task = Task(name=form.name.data,
					due_date=form.due_date.data,
					user =current_user._get_current_object(),
					category = inbox
					)

		db.session.add(task)
		
		return redirect(url_for('main.task'))
	tasks = user.tasks.order_by(Task.due_date.asc()).all()


	return render_template('tasks.html', form=form, tasks=tasks, user=user, cat=cat)

@main.route('/category', methods=['GET', 'POST'])
@admin_required
def category():
	category = Category(name=request.form['category_name'])
	db.session.add(category)
	flash('Category added')

	return redirect(url_for('main.task'))

@main.route('/task/<int:id>', methods=['GET', 'POST'])
def tasks_per_category(id):
	cat = Category.query.order_by(Category.id.desc()).all()
	form = AddTask()
	# form.C_name.choices = [(category.id, category.name) for category in Category.query.all()]
	
	category_id=Task.category_id
	username=current_user.username
	user = User.query.filter_by(username=username).first()
	
	# tasks_per_category = Task.query.filter_by(category_id=category_id).all() 
	if form.validate_on_submit():
		task = Task(name=form.name.data,
					due_date=form.due_date.data,
					user =current_user._get_current_object(),
					category_id = id
					)

		db.session.add(task)
		
		return redirect(url_for('main.task'))
	
	tasks = user.tasks.filter_by(category_id=id).all()
	

	return render_template('tasks_per_category.html', form=form, tasks=tasks, user=user, cat=cat)

@main.route('/edit_task/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
	
	
	form = AddTask()
	task = Task(id=id)

	if form.validate_on_submit():
		
		task.name=form.name.data,
		task.due_date=form.due_date.data,
		user =current_user._get_current_object(),
		category_id = id
		db.session.add(task)
        flash('Your task has been updated.')
	return render_template("edit_task.html", form=form)

@main.route('/delete_task/<int:id>', methods=['GET', 'POST'])
def delete_task(id):
	t_id= Task.id
	task = Task.query.filter_by(id=t_id)
	db.session.delete(task)
	
	return render_template("tasks_per_category.html")
