from yacut import app, db
from flask import render_template, flash, url_for
from yacut.forms import URLMapForm
import string
import random
from yacut.models import URLMap

@app.route('/', methods=['GET', 'POST'])
def yacut_view():
    form = URLMapForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if not short:
            short = get_unique_short_id()
        yacut = URLMap(
            original=form.original_link.data,
            short=short
        )
        db.session.add(yacut)
        db.session.commit()
    return render_template('yacut.html', form=form)


def get_unique_short_id():
    short = ''.join(random.choices(string.ascii_lowercase, k=6))
    return short
