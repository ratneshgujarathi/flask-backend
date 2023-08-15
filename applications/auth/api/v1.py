import logging

from flask import Blueprint, request

from applications.auth.utils.accounts import *
from helpers.response import ErrorResponse, SuccessResponse

auth = Blueprint('auth', __name__, url_prefix='/v1/auth')


@auth.route('/login', methods=['POST'])
# @swag_from('../swagger/auth/login.yml')
def login():
    try:
        return SuccessResponse(do_login_user(request))
    except Exception as err:
        logging.error(f"Failed to login: {err}")
        return ErrorResponse(err.args)


@auth.route('/logout', methods=['POST'])
# @swag_from('../swagger/auth/logout.yml')
def logout():
    try:
        return SuccessResponse(do_logout_user(request))
    except Exception as err:
        logging.error(f"Failed to logout: {err}")
        return ErrorResponse('BAD_REQUEST')


@auth.route('/register', methods=['POST'])
def register():
    try:
        return SuccessResponse(do_register_user(request))
    except Exception as err:
        logging.error(f"Failed to register: {err}")
        return ErrorResponse('BAD_REQUEST')


@auth.route('/users', methods=['GET'])
def list_users():
    try:
        return SuccessResponse(do_list_users(request))
    except Exception as err:
        logging.error(f"Failed to register: {err}")
        return ErrorResponse('BAD_REQUEST')


@auth.route('/user', methods=['GET'])
def get_user():
    try:
        return SuccessResponse(do_get_user(request))
    except Exception as err:
        logging.error(f"Failed to register: {err}")
        return ErrorResponse('BAD_REQUEST')


@auth.route('/user', methods=['PUT'])
def update_user():
    try:
        return SuccessResponse(do_update_user(request))
    except Exception as err:
        logging.error(f"Failed to register: {err}")
        return ErrorResponse('BAD_REQUEST')


@auth.route('/user', methods=['DELETE'])
def delete_user():
    try:
        return SuccessResponse(do_delete_user(request))
    except Exception as err:
        logging.error(f"Failed to register: {err}")
        return ErrorResponse('BAD_REQUEST')
