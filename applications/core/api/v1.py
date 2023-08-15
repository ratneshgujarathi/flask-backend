from flask import Blueprint, request

from helpers.response import SuccessResponse, ErrorResponse

# Create the Blueprint instance

core_v1 = Blueprint('core_v1', __name__, url_prefix="/v1/core/")


@core_v1.route('/calculate', methods=['GET'])
def calculate_values():
    try:
        args = request.args
        return SuccessResponse(args)
    except Exception as err:
        return ErrorResponse(err.args)
