from flask import Flask
from flask import redirect  # 导入重定向
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')  # 默认路由
def index():
    return '<h1>Hello World</h1>'


@app.route('/re')  # 重定向
def re():
    return redirect('https://www.hao123.com/')


@app.route('/user/<name>')  # 可变参数路由写法
def user(name):
    return '<h1>hello, %s!</h1>' % name


if __name__ == '__main__':
    manager.run()
