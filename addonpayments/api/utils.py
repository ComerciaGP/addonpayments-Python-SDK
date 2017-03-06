# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import six
import xmltodict
import json

from addonpayments.exceptions import SdkError
from addonpayments.logger import Logger

logger = Logger().get_logger(__name__)


class XmlUtils(object):
    """
    Utils to serialize and deserialize objects to XML
    """

    @staticmethod
    def to_xml(request):
        """
        This method parse request to XML object
        :return: string
        """
        logger.debug("Parsing request object to XML")
        try:
            xml = xmltodict.unparse(request.normalize_xml())
        except Exception as e:
            error_msg = "Error parsing request to XML"
            logger.error("{}: {}".format(error_msg, e))
            raise SdkError(error_msg, e)
        return xml

    @staticmethod
    def from_xml_api_response(xml):
        """
        Method parse XML to dict.
        :param xml: string
        :return: dict
        """
        logger.debug("Parsing XML response to dict")
        try:
            resp = json.loads(json.dumps(xmltodict.parse(xml)))
            resp['response']
            response = {key.replace('@', ''): value for key, value in six.iteritems(resp['response'])}
        except Exception as e:
            error_msg = "Error parsing response XML"
            logger.error("{}: {}".format(error_msg, e))
            raise SdkError(error_msg, e)
        return response
