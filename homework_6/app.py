from flask import Flask
from os import getenv
from models import db
from flask_migrate import Migrate
from views.mainpage import blog_main_app
from views.posts import posts_app
from views.users import users_app

app = Flask(__name__)

CONFIG_NAME = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_NAME}")

app.register_blueprint(blog_main_app, url_prefix="/")
app.register_blueprint(posts_app, url_prefix="/post/")
app.register_blueprint(users_app, url_prefix="/user/")

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
