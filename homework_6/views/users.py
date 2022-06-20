import logging
from flask import (
    Blueprint,
    request,
    render_template,
    url_for,
    redirect
)
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import BadRequest, InternalServerError
from views.forms.user import UserForm
from models import db, User

log = logging.getLogger(__name__)

users_app = Blueprint("users_app", __name__)


@users_app.route("/register/", methods=["GET", "POST"], endpoint='register')
def register_user():
    form = UserForm()
    if request.method == "GET":
        return render_template("users/registration.html", form=form)

    if not form.validate_on_submit():
        return render_template("users/registration.html", form=form), 400

    user_username = form.data["username"]
    user_password = form.data["password"]
    user = User(
        username=user_username,
        password=user_password
    )
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        log.exception("Could not add user %s", user)
        db.session.rollback()
        raise BadRequest(f"Could not add user, probably the name '{user_username}' is not unique")
    except DatabaseError:
        log.exception("Could not add user %s", user)
        db.session.rollback()
        raise InternalServerError("Could not add user due to unexpected error!")

    url_blog = url_for("users_app.login")
    return redirect(url_blog)


@users_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login_user():
    form = UserForm()
    if request.method == "GET":
        return render_template("users/login.html", form=form)

    if not form.validate_on_submit():
        return render_template("users/login.html", form=form), 400

    user_username = form.data["username"]
    user_password = form.data["password"]
    user_logged_in = bool(form.data.get("logged_in"))

    user = User.query.filter_by(username=user_username, password=user_password).one_or_none()
    user_logged = User.query.filter_by(logged_in=True).one_or_none()
    if user:
        if user_logged:
            raise BadRequest("Could not login user, please logout first")
        elif not user_logged_in:
            raise BadRequest("Could not login user, please confirm your authorization by clicking 'I'm sure'")
        else:
            user.logged_in = user_logged_in
            db.session.commit()
    else:
        raise BadRequest("Could not login user, maybe wrong username or password")

    url_blog = url_for("blog_main_app.mainpage")
    return redirect(url_blog)


@users_app.route("/logout/", methods=["GET", "POST"], endpoint="logout")
def logout_user():
    form = UserForm()
    if request.method == "GET":
        return render_template("users/logout.html", form=form)

    user_logged_in = bool(form.data.get("logged_in"))

    user = User.query.filter_by(logged_in=True).one_or_none()
    if user and user_logged_in:
        user.logged_in = False
        db.session.commit()
    else:
        raise BadRequest("Please click I'm sure")

    url_blog = url_for("blog_main_app.mainpage")
    return redirect(url_blog)
