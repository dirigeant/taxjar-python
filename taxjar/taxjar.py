import re
import logging

from taxjar.client import Client
from taxjar.structures import *

logger = logging.getLogger(__name__)


class TaxJar:
    def __init__(self, token, *args, **kwargs):
        self.client = Client(token, *args, **kwargs)

    def is_valid_zipcode(self, zipcode):
        if re.findall('\w{5}-\w{4}', zipcode) or \
           re.findall('\w{5}', zipcode):
            return True

    def categories(self):
        r = self.client.GET_request('categories')

        categories = r.json().get('categories')

        try:
            categories_obj = [CategoryStruct(data=cat) for cat in categories]
            return categories_obj
        except Exception as e:
            logger.debug(e)
            raise

    def ratesForLocation(self, zipcode, address=None):
        if not self.is_valid_zipcode(zipcode):
            raise ValueError('Invalid zipcode')

        r = self.client.GET_request('rates', zipcode, address)
        rate = r.json().get('rate')

        try:
            rate_obj = RateStruct(data=rate)
            return rate_obj
        except Exception as e:
            logger.debug(e)
            raise
