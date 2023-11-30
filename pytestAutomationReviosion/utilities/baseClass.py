import pytest
import inspect
import logging


@pytest.mark.usefixtures('setup')
class BaseClass():
    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logfile.log')
        formatterType = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatterType)

        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger