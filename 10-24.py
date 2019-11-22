# import time
# from concurrent.futures import ThreadPoolExecutor,as_completed, ProcessPoolExecutor, Executor
# import math
# import threading
# def add(x,y):
#
#     print('{}+{}={}'.format(x,y,x+y))
#
#
# t1 = threading.Thread(target=add,name='1',args=(4,5))
# t1.start()
#
# time.sleep(2)
#
# t2 = threading.Thread(target=add,name = '2',args=(4,),kwargs={'y':6})
# t2.start()
# time.sleep(2)
#
# t3 = threading.Thread(target=add,name='3',kwargs={'x':4,'y':7})
# t3.start()

# import tornado.httpserver
# import tornado.ioloop
# import tornado.options
# import tornado.web
# from tornado.web import Application
# from tornado.options import define, options
# define("port", default=8000, help="run on the given port", type=int)
# class IndexHandler(tornado.web.RequestHandler):
#     def get(self):
#         greeting = self.get_argument('greeting', 'Hello')
#         self.write(greeting + ', tornado!')
# if __name__ == "__main__":
#     tornado.options.parse_command_line()
#     app = Application(handlers=[(r"/", IndexHandler)])
#     http_server = tornado.httpserver.HTTPServer(app)
#     http_server.listen(options.port)
#     tornado.ioloop.IOLoop.instance().start()
#http://localhost:8000/
#http://localhost:8000/?greeting=feng


# from flask import jsonify,Flask
# from flask import render_template
#
# app = Flask(__name__)
# @app.route("/")
# def index():
#     return render_template("index.html")
# @app.route("/hello", methods=['GET', ])
# def hello():
#     return jsonify(msg="hello world!")
# app.run()
from concurrent.futures import ThreadPoolExecutor

import time
def wait_on_b():
    time.sleep(1)
    print(b.result())  # b will never complete because it is waiting on a.
    return 5

def wait_on_a():
    time.sleep(1)
    print(a.result())  # a will never complete because it is waiting on b.
    return 6

executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)
# with ThreadPoolExecutor(max_workers=1) as executor:
#     future = executor.submit(pow, 323, 1235)
#     print(future.result())