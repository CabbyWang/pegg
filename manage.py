# coding:utf-8
from flask import Flask
from flask_script import Manager
# from flask 


app = Flask(__name__)
manage = Manager(app)


@app.route('/')
def index():
    return '<h2>Welcome to my pegg system !</h2>'


if __name__ == '__main__':
    manage.run()
