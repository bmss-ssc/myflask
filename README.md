### 初学python之flask框架

#### 环境介绍

Python=3.6 flask=1.0.2

#### 请求钩子

before_first_request：注册一个函数，在处理第一个请求之前运行。
before_request：注册一个函数，在每次请求之前运行。
after_request：注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
teardown_request：注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。