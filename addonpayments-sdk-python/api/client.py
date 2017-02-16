# -*- encoding: utf-8 -*-

import requests
import attr
from decouple import config

from exceptions import SdkError
from logger import Logger
from api.utils import XmlUtils

logger = Logger().get_logger(__name__)


class ApiClient(object):
    """
    Client class for sending requests to Addonpayments.

    Set URL endpoint from settings.ini (python-decouple) file,
    but if it is not defined the default is the test endpoint
    """

    endpoint = config('ADDONPAYMENTS_API_URL', default='https://remote.sandbox.addonpayments.com/remote')
    encoding_charset = 'utf-8'

    def __init__(self, secret):
        self.secret = secret
        self.headers = {
            'Content-Type': 'application/xml'
        }

    def send(self, request):
        """
        Sends the request to Addonpayments.
        Carries out the following actions:
            * Generate security hash
            * Parse request object to XML
            * Send POST request
            * Unparse XML response to dict
        :return: dict
        """
        # generate hash
        logger.debug("Generating hash.")
        request.hash(self.secret)

        # validate request
        logger.debug("Validating request.")
        attr.validate(request)

        logger.info("Sending XML request to Addonpayments URL: {}".format(self.endpoint))
        try:
            xml = XmlUtils.to_xml(request)
            result = requests.post(self.endpoint, data=xml.encode(self.encoding_charset), headers=self.headers)
        except requests.exceptions.RequestException as e:
            error_msg = "POST requests error"
            logger.error("{}: {}".format(error_msg))
            raise SdkError(error_msg, e)
        return XmlUtils.from_xml_response(result.text)
