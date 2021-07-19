from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def read():
    users = User.get_all_users()
    return render_template('read.html', users = users)

@app.route('/process', methods=['POST'])
def process():
    User.create_user(request.form)
    return redirect('/')

@app.route('/users/create')
def create_user():
    return render_template('form.html', name=request.form)

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    data = {
        'id': user_id
    }
    User.delete_user(data)
    return redirect('/')

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    data = {
        'id': user_id
    }
    user = User.get_user_by_id(data)
    return render_template('update.html', user = user)

@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect(f'/users/{user_id}/user_card')

@app.route('/users/<int:user_id>/user_card')
def user_card(user_id):
    data = {
        'id':user_id
    }
    user = User.get_user_by_id(data)
    return render_template('user_card.html', user = user)