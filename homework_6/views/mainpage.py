from flask import (
    Blueprint,
    render_template
)
from models import (
    Post
)


blog_main_app = Blueprint("blog_main_app", __name__)


@blog_main_app.get("/", endpoint="mainpage")
def blog_mainpage():
    posts: list[Post] = Post.query.all()
    return render_template("mainpage/blog.html", posts=posts)
