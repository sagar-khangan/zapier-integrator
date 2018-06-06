import datetime
import logging
import os


def create_logger(jobid):
    try:
        if not os.path.exists("logs"):
            os.makedirs("logs")
        filename = "logs/{0}.log".format(str(jobid))
        logging.basicConfig(filename=filename, level=logging.DEBUG)
    except Exception as e:
        print e
        pass


def debug_log(m):
    try:
        logger = logging.getLogger(__name__)
        msg = " {0} :: {1}".format(datetime.datetime.now(), m)
        logger.debug(msg)
    except Exception as e:
        pass


def info_log(m):
    try:
        logger = logging.getLogger(__name__)
        msg = " {0} :: {1}".format(datetime.datetime.now(), m)
        logger.info(msg)
    except Exception as e:
        pass


def error_log(m):
    try:
        logger = logging.getLogger(__name__)
        msg = " {0} :: {1}".format(datetime.datetime.now(), m)
        logger.error(msg)
    except Exception as e:
        pass


def warning_log(m):
    try:
        logger = logging.getLogger(__name__)
        msg = " {0} :: {1}".format(datetime.datetime.now(), m)
        logger.warning(msg)
    except Exception as e:
        pass
