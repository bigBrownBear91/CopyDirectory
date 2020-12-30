import logging
import datetime


class Logger:
    def __init__(self, logging_file):
        logging.basicConfig(filename=logging_file, filemode='a', level=logging.DEBUG)
        logging.info(f'Start script at {datetime.datetime.now()}')

    def __del__(self):
        logging.info(f'End logging at {datetime.datetime.now()}')

    @staticmethod
    def log_info(message):
        logging.info(message)
