from services.database import db
from constants import CollectionNames


def do_register_user(request):
    data = request.json
    db[CollectionNames.USERS].insert_one({"name": data.get("name", None)})
    return data


def do_login_user(request):
    data = request.json
    return data


def do_logout_user(request):
    data = request.json
    return data


def do_update_user(request):
    data = request.json
    return data


def do_delete_user(request):
    data = request.json
    return data


def do_get_user(request):
    data = request.args
    return data


def do_list_users(request):
    data = request.args
    return data
