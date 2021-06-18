# flask 工厂函数


使用工厂函数不会直接创建 ``app`` 实例这个全局变量，而是通过 ``create_app()`` 函数创建,再返回 ``app`` 对象。

演示一个项目使用工厂函数的例子，用上 ``flask_sqlalchemy``，``flask_migrate``，``flask_bootstrap`` 等扩展库。

文档结构：
```
/app
    __init__.py
    models.py
    routes.py
config.py
run.py
```

```
# __init__.py

from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    # 加载配置文件
    app.config.from_object(Config)

    # 初始化各种扩展库
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)

    # 引入蓝图并注册
    from app.routes import main_routes
    app.register_blueprint(main_routes)

    return app

from app import models
```

调用工厂函数创建 ``app``。

```
# run.py

from app import create_app, db
app = create_app()
```

因为不存在全局变量 ``app`` 了，所以 ``routes`` 里面的路由函数也不能直接注册成 ``@app.route('/')`` 这种形式，应当使用蓝图（``Blueprint``）来管理路由。

```
# routers.py

main_routes = Blueprint('main', __name__)

@main_routes .route('/index')
def index():
    …………
```

本文源码：https://github.com/SingleDiego/Flask-Application-Factories
