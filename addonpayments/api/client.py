# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import requests
import attr
from decouple import config

from addonpayments.exceptions import SdkError
from addonpayments.logger import Logger
from addonpayments.api.utils import XmlUtils
from addonpayments.utils import ValidationUtils
from addonpayments.api.common.responses import ApiResponse

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

    def send(self, request, response_validation=True):
        """
        Sends the request to AddonPayments.
        Carries out the following actions:
            * Generate security hash
            * Parse request object to XML
            * Send POST request
            * Receive AddonPayments response
            * Unparse XML response to ApiResponse
            * Validate hash
        :param request: ApiRequest
        :param response_validation: bool
        :return: ApiResponse
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
            logger.error(error_msg)
            raise SdkError(error_msg, e)

        normalized_dict = XmlUtils.from_xml_api_response(result.text)
        api_response = ApiResponse(**normalized_dict)
        if response_validation:
            return ValidationUtils.validate_response(api_response, self.secret)
        return api_response
