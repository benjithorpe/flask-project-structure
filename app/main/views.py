from datetime import datetime

from flask import render_template, session, redirect, url_for

from . import main_blueprint
from .forms import NameForm
from .. import db
from ..models import User


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # ...
        return redirect(url_for("main_blueprint.index"))
        # can also be written as:
        # return redirect(url_for(".index"))
    context = {
        "form": form,
        "name": session.get("name"),
        "known": session.get("known", False),
        "current_time": datetime.utcnow(),
    }
    return render_template("index.html", context=context)
