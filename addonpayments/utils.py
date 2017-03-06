# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import re
import six
import uuid
import hashlib
from datetime import datetime

from addonpayments.exceptions import SdkError
from addonpayments.logger import Logger


logger = Logger().get_logger(__name__)


class GenerationUtils(object):
    """
    Utils for the auto-generation of fields, for example the SHA1 hash.
    """

    date_format = "%Y%m%d%H%M%S"

    @staticmethod
    def generate_hash(to_hash, secret):
        """
        This method takes the pre-built string of concatenated fields and the secret and returns the SHA-1 hash to be
        placed in the request sent to HPP or API.
        :param to_hash: string
        :param secret: string
        :return: string
        """
        # Step 1: With the SHA-1 algorithm, obtain the hash value of a string composed of the requested values.
        to_hash_first_pass = hashlib.sha1(six.binary_type(to_hash.encode('utf-8'))).hexdigest()
        # Step 2: Concatenate the hash value chain with the shared secret.
        return hashlib.sha1(six.binary_type("{}.{}".format(to_hash_first_pass, secret).encode('utf-8'))).hexdigest()

    def generate_order_id(self):
        """
        Order Id for a initial request should be unique per client ID. This method generates a unique order Id using
        the Python uuid class
        :return: string
        """
        return uuid.uuid4().hex

    def generate_timestamp(self):
        """
        Generate the current date timestamp in the string format (YYYYMMDDHHSS) required in a request.
        :return: string
        """
        return datetime.now().strftime(self.date_format)


class ValidationUtils(object):
    """
    Class validates HPP and API response objects.
    """

    @staticmethod
    def validate_response(sdk_response, secret):
        """
        Method validates HPP and API response hash.
        :param sdk_response: SdkResponse
        :param secret: string
        """
        if sdk_response.sha1hash and not sdk_response.is_hash_valid(secret):
            error_msg = "SdkResponse contains an invalid security hash"
            logger.error(error_msg)
            raise SdkError(error_msg)
        return sdk_response


class ValidateUtils(object):
    """
    Utils for the attrs validation fields.
    """

    @staticmethod
    def validate_mandatory(name, value):
        """
        This method raise exception if value is empty
        :param name: string
        :param value:
        """
        if not value:
            raise ValueError("Missing required argument: {}".format(name))

    @staticmethod
    def validate_str(name, value):
        """
        This method raise exception if value is not string
        :param name: string
        :param value:
        """
        if not isinstance(value, six.string_types):
            raise ValueError("{} must be string".format(name))

    @staticmethod
    def validate_int(name, value):
        """
        This method raise exception if value is not int
        :param name: string
        :param value:
        """
        if not isinstance(value, int):
            raise ValueError("{} must be integer".format(name))

    @staticmethod
    def validate_list(name, value):
        """
        This method raise exception if value is not list
        :param name: string
        :param value:
        """
        if not isinstance(value, list):
            raise ValueError("{} must be list".format(name))

    @staticmethod
    def validate_dict(name, value):
        """
        This method raise exception if value is not dict
        :param name: string
        :param value:
        """
        if not isinstance(value, dict):
            raise ValueError("{} must be dict".format(name))

    @staticmethod
    def validate_length_range(name, value, minimum, maximum):
        """
        This method raise exception if the length of the value is not within the range
        :param name: string
        :param value: string
        :param minimum: int
        :param maximum: int
        """
        if len(value) < minimum or len(value) > maximum:
            raise ValueError("{} must be between {} and {} characters".format(name, minimum, maximum))

    @staticmethod
    def validate_length(name, value, length):
        """
        This method raise exception if the length of the value is not the correct
        :param name: string
        :param value: string
        :param length: int
        """
        if len(value) != length:
            raise ValueError("{} must be {} characters in length".format(name, length))

    @staticmethod
    def validate_regex(name, value, regex, regex_msg):
        """
        This method raise exception if the value does not match the regular expression
        :param name: string
        :param value: string
        :param regex: string
        :param regex_msg: string
        """
        if not re.match(regex, value):
            raise ValueError("{} must only contain {} characters".format(name, regex_msg))
