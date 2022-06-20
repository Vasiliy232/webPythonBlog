import logging
from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect
)
from sqlalchemy.exc import DatabaseError
from werkzeug.exceptions import InternalServerError
from views.forms.post import PostForm
from models import db, Post, User


log = logging.getLogger(__name__)

posts_app = Blueprint("posts_app", __name__)


@posts_app.get("/<int:post_id>/", endpoint="post")
def get_product(post_id):
    post = Post.query.get_or_404(post_id, description=f"Post #{post_id} not found")
    return render_template(
        "posts/post.html",
        post=post
    )


@posts_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_post():
    form = PostForm()
    if request.method == "GET":
        return render_template("posts/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("posts/add.html", form=form), 400

    user = User.query.filter_by(logged_in=True).one_or_none()

    post_title = form.data["title"]
    post_greetings = form.data["pre_post"]
    post_input_text = form.data["post"]
    post_username = user.username
    post = Post(
        title=post_title,
        pre_post=post_greetings,
        post_text=post_input_text,
        user_username=post_username
    )
    db.session.add(post)
    try:
        db.session.commit()
    except DatabaseError:
        log.exception("Could not add post %s", post)
        db.session.rollback()
        raise InternalServerError("Could not save product due to unexpected error!")

    url_post = url_for("posts_app.post", post_id=post.id)
    return redirect(url_post)
