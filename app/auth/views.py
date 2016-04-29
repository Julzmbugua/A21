from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from . import auth
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('auth/login.html', form=form)
   