import logging

from applications.core.api.v1 import core_v1

SERVICES = [
    # {"blueprint": auth},
    {"blueprint": core_v1},
]


def register_apis(app):
    try:
        for service in SERVICES:
            # module = importlib.import_module(service['path'], package='server')
            app.register_blueprint(service['blueprint'])
        logging.info('Registered all the APIs')
    except Exception as err:
        logging.exception(f"Failed to register APIs: {err}")
