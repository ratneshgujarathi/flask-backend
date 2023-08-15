import importlib
from flask import Response
import json
import logging
import os
import uuid
import hashlib
import time
from datetime import datetime
from operator import attrgetter
# from server.helpers.file_handler import UnseekableStream
from zipfile import ZipFile, ZipInfo
from logging.handlers import RotatingFileHandler
from subprocess import PIPE, Popen
import io
# from server.config.config import load_config
from bson.objectid import ObjectId
from subprocess import Popen, PIPE

from flask import current_app as app
import gettext 

formatter = logging.Formatter(
    "%(asctime)s | %(funcName)s | %(levelname)s | %(message)s ")


class JSONEncoder(json.JSONEncoder):
    """
     extend json-encoder class
    """

    def default(self, o):
        try:
            if isinstance(o, ObjectId):
                return str(o)
            if isinstance(o, datetime):
                return str(o)
            if isinstance(o, uuid.UUID):
                return str(o)
            if isinstance(o, bytes):
                return o.decode("utf-8", "ignore")
            return json.JSONEncoder.default(self, o)
        except Exception as err:
            logging.error(err)


def setup_logger(name, log_file, level=logging.DEBUG):
    """
    Function to setup and initialize multiple loggers
    """
    handler = RotatingFileHandler(
        filename=log_file, maxBytes=5000000, backupCount=10)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    # Stop back propagation and removing all older handlers
    logger.handlers.clear()
    logger.addHandler(handler)

    return logger


# def zip_content_generator(zf, stream, base_path, dirpath, filename):
#     storage_path = os.path.join(dirpath, filename)
#     path_in_zip = os.path.join(base_path, filename)
#     _stat = os.stat(storage_path)
#     modified_time = datetime.fromtimestamp(_stat.st_mtime)
#     attrs = ('year', 'month', 'day', 'hour', 'minute', 'second')
#     mtime = attrgetter(*attrs)(modified_time)
#     force_zip64 = True if _stat.st_size > 4294967295 else False
#     z_info = ZipInfo(path_in_zip, mtime)
#     with open(storage_path, 'rb') as entry, zf.open(z_info, mode='w', force_zip64=force_zip64) as dest:
#         for chunk in iter(lambda: entry.read(16384), b''):
#             dest.write(chunk)
#             # Yield chunk of the zip file stream in bytes.
#             yield stream.get()


# def zipfile_generator():
#     src = load_config().LOGS_PATH
#     stream = UnseekableStream()
#     with ZipFile(stream, mode='w', allowZip64=True) as zf:
#         for dirpath, dirnames, filenames in os.walk(src):
#             files = [f for f in filenames if f.endswith(".log")]
#             base_path = ''
#             if str(os.path.basename(os.path.dirname(dirpath))) != 'boxafe':
#                 base_path = os.path.basename(dirpath)
#             for file in files:
#                 for data in zip_content_generator(zf, stream, base_path, dirpath, file):
#                     yield data
#     # ZipFile was closed.
#     yield stream.get()
#     stream.close()


# def zip_log():
#     file_name = 'logs.zip'
#     return Response(zipfile_generator(),
#                     mimetype='application/zip',
#                     headers={'Access-Control-Expose-Headers': 'Content-Disposition',
#                              'Content-Disposition': f'attachment;filename={file_name}',
#                              'Cache-Control': 'no-store, no-cache, must-revalidate, '
#                                               'post-check=0, pre-check=0, max-age=0'})