# -*- coding = utf-8 -*-
# @time : 2022/5/17 21:24
# @author : 李志
# @file : manager.py
# @software : PyCharm



from flask_shop import create_app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# 创建一个app对象
app = create_app("develop")

'''
python manager.py db init  执行一遍
python manager.py db migrate 生成表结构
python manager.py db upgrade 映射数据库

'''

# 管理数据库映射
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)



if __name__ == '__main__':
    app.run()
    # manager.run()