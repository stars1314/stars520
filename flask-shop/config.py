# -*- coding = utf-8 -*-
# @time : 2022/5/18 21:52
# @author : 李志
# @file : config.py
# @software : PyCharm

import os


class Config:
    # 配置mysql的参数
    MYSQL_DIALECT = "mysql"
    MYSQL_DIRVER = "pymysql"
    MYSQL_NAME = "root"
    MYSQL_PWD = "123456"
    MYSQL_HOST = "localhost"
    MYSQL_PORT = "3306"
    MYSQL_DB = "flask_shop"
    MYSQL_CHARSET = "utf8"

    SQLALCHEMY_DATABASE_URI = F"{MYSQL_DIALECT}+{MYSQL_DIRVER}://{MYSQL_NAME}:{MYSQL_PWD}@{MYSQL_HOST}:" \
                              F"{MYSQL_PORT}/{MYSQL_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 盐的设置
    SECRET_KEY = os.urandom(16)
    
    ALLOWED_IMGS = set(['bmp','png','jpg','jpeg','gif'])

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    SERVER_IMG_UPLOADS = os.path.join(BASE_DIR,'flask_shop','static','img') 


class DevelopmentConfig(Config):
    # 启动debug调试模式
    DEBUG = True


class ProductionConfig(Config):
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}