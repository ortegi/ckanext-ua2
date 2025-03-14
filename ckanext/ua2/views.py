from flask import Blueprint


ua2 = Blueprint(
    "ua2", __name__)


def page():
    return "Hello, ua2!"


ua2.add_url_rule(
    "/ua2/page", view_func=page)


def get_blueprints():
    return [ua2]
