import signal
import logging
import platform
from flask import Flask
from config import Config
from flask_pymongo import PyMongo

import tornado.options
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop, PeriodicCallback

is_closing = False

app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app)

# 注册蓝图
from views import view

app.register_blueprint(view)


def signal_handler(signum, frame):
    """
    捕获键盘信号，用来停止tornado循环
    :param signum:
    :param frame:
    :return:
    """
    global is_closing
    app.logger.info(f'Caught signal: {signum}')
    is_closing = True


def close_loop():
    """
    停止tornado的http_server和ioloop
    :return:
    """
    global is_closing
    if is_closing:
        app.logger.info('Stopping http server')
        http_server.stop()
        app.logger.info('Server Shutdown!')
        IOLoop.instance().stop()


def init_logger():
    """
    初始化logger
    :return:
    """
    log_formatter = logging.Formatter(Config.LOG_FORMAT)
    log_handler = logging.FileHandler(Config.LOG_FILE)
    log_handler.setLevel(logging.INFO)
    log_handler.setFormatter(log_formatter)
    app.logger.addHandler(log_handler)


if __name__ == '__main__':
    init_logger()

    tornado.options.parse_command_line()

    # 利用tornado拉起flask服务，linux系统可以支持多进程启动，windows只能单进程启动
    signal.signal(signal.SIGINT, signal_handler)
    http_server = HTTPServer(WSGIContainer(app))
    if platform.system() == 'Windows':
        http_server.listen(Config.APP_PORT)
    else:
        http_server.bind(Config.APP_PORT)
        http_server.start(Config.NUM_PROCESSES)
    PeriodicCallback(close_loop, 100).start()
    IOLoop.instance().start()
