from sqlalchemy import Column, Integer, String
from flask_sqlalchemy_rls import SQLAlchemy, AnonymousUser
from flask import Flask, redirect, request
from flask_login import LoginManager, UserMixin, logout_user, login_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefg'
db = SQLAlchemy(app)


class TestModel(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)


class RegisteredUser(UserMixin):
    get_id = lambda self: 1
    get_sql_role = lambda self: 'alice'

registered_user = RegisteredUser()

login_manager = LoginManager(app)
login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return registered_user


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def get_all():
    return str(TestModel.query.all())


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route("/login")
def login():
    login_user(registered_user)
    return redirect('/')
