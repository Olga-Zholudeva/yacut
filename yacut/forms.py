from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

import settings as st


class URLMapForm(FlaskForm):
    original_link = URLField(
        "Длинная ссылка",
        validators=[
            DataRequired(message="Обязательное поле"),
            URL(require_tld=True, message=("Некорректный URL")),
        ],
    )
    custom_id = StringField(
        "Ваш вариант короткой ссылки",
        validators=[
            Length(1, 16),
            Optional(),
            Regexp(
                regex=st.short_name,
                message="Указано недопустимое имя для короткой ссылки",
            ),
        ],
    )
    submit = SubmitField("Создать")
