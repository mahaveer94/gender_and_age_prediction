from gender_and_age_prediction.exception import GenderException
import os
import sys

from gender_and_age_prediction.logger import logging

def test_exception():
    try:
        logging.info("logger file run")
        a=1/0
    except Exception as e:
        raise  GenderException(e,sys)
    

if __name__ == '__main__':  
    try:
        test_exception()
    except Exception as e:
        print(e)
    