# -*- encoding: utf-8 -*-

import base64
import json

from exceptions import SdkError
from hpp.card_storage.requests import CardStorageRequest
from hpp.payment.requests import PaymentRequest
from hpp.common.responses import HppResponse
from logger import Logger

logger = Logger().get_logger(__name__)


class ValidationUtils(object):
    """
    Class validates HPP request and response objects.
    """

    @staticmethod
    def validate_response(hpp_response, secret):
        """
        Method validates HPP response hash.
        :param hpp_response:  HppResponse
        :param secret: string
        """
        if not hpp_response.is_hash_valid(secret):
            error_msg = "HppResponse contains an invalid security hash"
            logger.error(error_msg)
            raise SdkError(error_msg)
        return hpp_response


class JsonUtils(object):
    """
    Utils to serialize and deserialize HPP objects to JSON
    """

    @staticmethod
    def to_json(hpp_object, charset, encoded=False):
        """
        Method serialises HppRequest or HppResponse to JSON.
        :param hpp_object:
        :param charset: string
        :param encoded: bool
        :return: string
        """
        dict_object = hpp_object.to_dict()
        if encoded:
            return json.dumps(JsonUtils.encode(dict_object, charset))
        return json.dumps(dict_object, charset)

    @staticmethod
    def from_json_hpp_request(json_hpp_request, charset, encoded=False):
        """
        Method deserialize JSON to HppRequest.
        :param json_hpp_request: string
        :param charset: string
        :param encoded: bool
        :return: HppRequest
        """
        obj_request = json.load(json_hpp_request)
        if encoded:
            obj_request = JsonUtils.decode(obj_request, charset)

        is_card_storage = False
        if obj_request.get('CARD_STORAGE_ENABLE') or obj_request.get('card_storage_enable'):
            is_card_storage = True

        dict_request = {}
        supplementary_data = {}
        for key, value in obj_request.items():
            key_hpp = key.lower()
            is_supplementary_data = False
            if is_card_storage:
                if not hasattr(CardStorageRequest, key_hpp):
                    is_supplementary_data = True
            else:
                if not hasattr(PaymentRequest, key_hpp):
                    is_supplementary_data = True
            if is_supplementary_data:
                supplementary_data[key_hpp] = value
            else:
                dict_request[key_hpp] = value
        if supplementary_data:
            dict_request['supplementary_data'] = supplementary_data

        if is_card_storage:
            return CardStorageRequest(**dict_request)
        else:
            return PaymentRequest(**dict_request)

    def from_json_hpp_response(self, json_hpp_response, charset, encoded):
        """
        Method deserialize JSON to HppResponse.
        :param json_hpp_response: string
        :param charset: string
        :param encoded: bool
        :return: HppResponse
        """
        obj_response = json.loads(json_hpp_response)
        if encoded:
            obj_response = JsonUtils.decode(obj_response, charset)
        return self.normalize_response(obj_response)

    @staticmethod
    def encode(hpp_dict, charset='utf-8'):
        """
        Base64 encodes all Hpp Request values.
        :param hpp_dict: dict
        :param charset: string
        :return: dict
        """
        for key, value in hpp_dict.items():
            b64_value = base64.b64encode(bytes(str(value), charset))
            hpp_dict[key] = b64_value.decode(charset)
        return hpp_dict

    @staticmethod
    def decode(hpp_dict, charset='utf-8'):
        """
        Base64 decodes all Hpp Request values.
        :param hpp_dict: dict
        :param charset: string
        """
        for key, value in hpp_dict.items():
            hpp_dict[key] = str(base64.b64decode(value), charset)
        return hpp_dict

    @staticmethod
    def normalize_response(obj_response):
        """
        Method deserialize JSON to HppResponse.
        :type obj_response: dict
        :return: HppResponse
        """
        obj_response = {key.lower(): value for key, value in obj_response.items()}
        return HppResponse(**obj_response)
