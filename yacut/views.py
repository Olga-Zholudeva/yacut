import random
import string

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap


@app.route("/", methods=["GET", "POST"])
def yacut_view():
    """Обрабатываем запрос на создаение короткой ссылки."""

    form = URLMapForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if URLMap.query.filter_by(short=short).first():
            flash(f"Имя {short} уже занято!", "dublikat")
            return render_template("yacut.html", form=form)
        if not short:
            short = get_unique_short_id()
        urlmap = URLMap(original=form.original_link.data, short=short)
        db.session.add(urlmap)
        db.session.commit()
        flash(
            url_for(
                "redirect_view",
                short=short,
                _external=True,
            ),
            "link",
        )
    return render_template("yacut.html", form=form)


@app.route("/<string:short>")
def redirect_view(short):
    """Перенаправляем на страницу полной ссылки."""

    urlmap = URLMap.query.filter_by(short=short).first()
    if urlmap:
        return redirect(urlmap.original)
    abort(404)


def get_unique_short_id():
    """Формируем короткую ссылку, если она не пришла от пользователя."""

    short = "".join(random.choices(string.ascii_lowercase, k=6))
    if URLMap.query.filter_by(short=short).first():
        get_unique_short_id()
    return short
