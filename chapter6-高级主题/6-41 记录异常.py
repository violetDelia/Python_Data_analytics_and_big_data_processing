# -*- coding: UTF-8 -*-

import logging
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d]- %(levelname)s: %(message)s',level=logging.INFO)

class MyException(Exception):
    def __init__(self, longitude, latitude):
        self._longitude = longitude
        self._latitude = latitude

def get_position(longitude=None, latitude=None):
    if longitude is None or latitude is None:
        raise MyException(longitude, latitude)

try:
    get_position()
except MyException as e:
    logging.info("经度是：", e._latitude, "纬度是：", e._latitude)
finally:
    print("END")

	
	