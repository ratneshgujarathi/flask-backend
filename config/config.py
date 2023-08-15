# Importing config
import os
import pathlib
# from server.constants import CollectionNames


class BaseConfig(object):
    # DEBUGGING
    DEBUG = False

    # PATH
    BASE_PATH = '/'

    # use when linux server deployment
    # APP_PATH = '/mnt/ext/opt/{app_name}'
    # STORAGE_PATH = os.path.join(APP_PATH, 'storage')
    # LOGS_PATH = os.path.join(APP_PATH, 'logs')

    # CONFIG FILES
    # CONF_PATH_ULINUX = '/etc/config/uLinux.conf'
    # CONF_PATH_SMB = '/etc/config/smb.conf'
    # PYTHON_PATH = APP_PATH + '/packages/python/bin/python3'

    # SERVER INFO
    SERVER_PROTOCOL = 'http'
    SERVER_IP = '127.0.0.1'
    SERVER_PORT = '9046'


class DevelopmentConfig(BaseConfig):
    # DEBUGGING
    DEBUG = True

    # SERVER INFO
    SERVER_IP = '0.0.0.0'
    SERVER_PORT = '9046'

    BASE_PATH = str(pathlib.Path(__file__).parent.parent.absolute())
    STORAGE_PATH = os.path.join(BASE_PATH, 'storage')
    LOGS_PATH = os.path.join(BASE_PATH, 'logs')

    def __init__(self):
        super(DevelopmentConfig, self).__init__()


class ProductionConfig(BaseConfig):

    def __init__(self):
        super(ProductionConfig, self).__init__()


def load_config(env=None):
    try:
        env = os.environ.get('FLASK_ENV')
        if env:
            env = env.lower()

        if env == 'dev' or env == 'development':
            return DevelopmentConfig()
        elif env == 'prod' or env == 'production':
            return ProductionConfig()
        else:
            return ProductionConfig()
    except Exception as err:
        print(err)

    return DevelopmentConfig()
