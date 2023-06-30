from re import match

import validators
from flask import jsonify, request

from . import app, db, views
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route("/api/id/<string:short_id>/", methods=["GET"])
def get_url(short_id):
    """Получаем длинную ссылку по короткой."""

    urlmap = URLMap.query.filter_by(short=short_id).first()
    if not urlmap:
        raise InvalidAPIUsage("Указанный id не найден", 404)
    return jsonify({"url": urlmap.original}), 200


@app.route("/api/id/", methods=["POST"])
def add_urlmap():
    """Обрабатываем запрос на создание короткой ссылки."""

    data = request.get_json(silent=True)
    if not data:
        raise InvalidAPIUsage("Отсутствует тело запроса", 400)
    if "custom_id" not in data.keys() or not data["custom_id"]:
        data["custom_id"] = views.get_unique_short_id()
    if "url" not in data.keys():
        raise InvalidAPIUsage('"url" является обязательным полем!', 400)
    if not validators.url(data["url"]):
        raise InvalidAPIUsage("Некорректный URL", 400)
    if URLMap.query.filter_by(short=data["custom_id"]).first():
        raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.', 400)
    if not match(r"^[A-Za-z0-9]{1,16}$", data["custom_id"]):
        raise InvalidAPIUsage("Указано недопустимое имя для короткой ссылки", 400)
    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    print(jsonify(urlmap.to_dict()))
    return jsonify(urlmap.to_dict()), 201
