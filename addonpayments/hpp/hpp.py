# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import attr
import six

from addonpayments.exceptions import SdkError
from addonpayments.logger import Logger
from addonpayments.utils import ValidationUtils
from addonpayments.hpp.utils import JsonUtils
from addonpayments.hpp.common.responses import HppResponse

logger = Logger().get_logger(__name__)


class Hpp(object):
    """
    Class for converting HPP requests and responses to and from JSON.
    This class is also responsible for validating inputs, generating defaults and encoding parameter values.
    """

    encoding_charset = 'utf-8'

    def __init__(self, secret):
        self.secret = secret

    def get_request_hash(self, hpp_request):
        return hpp_request.hash(self.secret)

    def get_response_hash(self, hpp_response):
        return hpp_response.hash(self.secret)

    def request_to_json(self, hpp_request, encoded=True):
        """
        Method produces JSON from HppRequest object.
        Carries out the following actions:
            * Generate security hash
            * Validates inputs
            * Base64 encodes inputs
            * Serialises request object to JSON
        :param hpp_request: HppRequest
        :param encoded: bool
        :return: string
        """
        logger.info("Converting HppRequest to JSON.")

        # generate hash
        logger.debug("Generating hash.")

        # set request object and calculate hash from it
        self.get_request_hash(hpp_request)

        # validate request
        logger.debug("Validating request.")
        attr.validate(hpp_request)

        logger.debug("Encoding to base64 and converting HppRequest to JSON.")
        try:
            json_request = JsonUtils.to_json(hpp_request, self.encoding_charset, encoded)
        except Exception as e:
            error_msg = "Exception json encoding HPP request"
            logger.error("{}: {}".format(error_msg, e))
            raise SdkError(error_msg, e)
        return json_request

    def request_from_json(self, json_request, encoded=True):
        """
        Method produces HppRequest object from JSON.
        Carries out the following actions:
            * Deserialize JSON to request object
            * Decodes Base64 inputs
            * Validates inputs
        :param json_request: string
        :param encoded: bool
        :return: HppRequest
        """
        logger.info("Converting JSON to HppRequest.")

        logger.debug("Decoding object.")
        try:
            hpp_request = JsonUtils.from_json_hpp_request(json_request, self.encoding_charset, encoded)
        except Exception as e:
            error_msg = "Exception decoding json HPP request"
            logger.error("{}: {}".format(error_msg, e))
            raise SdkError(error_msg, e)

        # validate request
        attr.validate(hpp_request)

        return hpp_request

    def response_to_json(self, hpp_response, encoded=False):
        """
        Method produces JSON from HppResponse object.
        Carries out the following actions:
            * Generate security hash
            * Base64 encodes inputs
            * Serialises response object to JSON
        :param hpp_response: HppResponse
        :param encoded: bool
        :return: string
        """
        logger.info("Converting HppResponse to JSON.")

        # generate hash
        logger.debug("Generating hash.")
        self.get_response_hash(hpp_response)

        logger.debug("Encoding to base64 and converting HppResponse to JSON.")
        try:
            json_response = JsonUtils.to_json(hpp_response, self.encoding_charset, encoded)
        except Exception as e:
            error_msg = "Exception json encoding HPP response"
            logger.error("{}: {}".format(error_msg, e))
            raise SdkError(error_msg, e)
        return json_response

    def response_from_json(self, json_response, encoded=True):
        """
        Method produces HppResponse object from JSON.
        Carries out the following actions:
            * Deserialize JSON to response object
            * Decodes Base64 inputs
            * Validates hash
        :param json_response: string
        :param encoded: bool
        :return: HppResponse
        """
        logger.info("Converting JSON to HppResponse.")

        logger.debug("Decoding object.")
        try:
            hpp_response = JsonUtils().from_json_hpp_response(json_response, self.encoding_charset, encoded)
        except Exception as e:
            error_msg = "Exception decoding HPP response"
            logger.error("{}: {}".format(error_msg, e))
            raise SdkError(error_msg, e)
        return ValidationUtils.validate_response(hpp_response, self.secret)

    def response_from_dict(self, response_dict):
        """
        Return an HppResponse object from dict after hash validation

        :param response_dict:
        :return:
        """
        logger.info("Converting dict to HppResponse.")
        normalized_dict = {key.lower(): value for key, value in six.iteritems(response_dict)}
        hpp_response = HppResponse(**normalized_dict)

        return ValidationUtils.validate_response(hpp_response, self.secret)
