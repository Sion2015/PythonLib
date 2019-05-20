# -*- coding: UTF-8 -*-

from oslo_config.cfg import CONF
from oslo_log import log as logging
# from oslo_context import context
from src.utils.path import LOG_PATH, SRC_PATH
from logging import handlers, FileHandler


class MyFileHandler(FileHandler):
    def __init__(self, file_name, mode):
        log_file_dir = str(LOG_PATH.joinpath(file_name))
        super(MyFileHandler, self).__init__(log_file_dir, mode)


class MyTimeRotatingFileHandler(handlers.TimedRotatingFileHandler):
    def __init__(self, file_name, when, interval=1, backup_count=0):
        log_file_dir = str(LOG_PATH.joinpath(file_name))
        super(MyTimeRotatingFileHandler, self).__init__(log_file_dir, when, interval, backup_count)


handlers.MyFileHandler = MyFileHandler
handlers.MyTimeRotatingFileHandler = MyTimeRotatingFileHandler

CONF.log_config_append = str(SRC_PATH.joinpath("conf", "logging.conf"))
DOMAIN = 'test'
logging.setup(CONF, DOMAIN)
