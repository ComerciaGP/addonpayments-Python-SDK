# -*- encoding: utf-8 -*-

import attr
from attr import ib as Field

from validators import RequestValidator
from utils import GenerationUtils
from api.mixins import XmlMixin


@attr.s
class ApiRequest(XmlMixin):
    """
    Super class representing a request to be sent to API.
    This class contains all common attributes and functions for all other classes.

    You can consult the specific documentation of all request fields on the website
    https://desarrolladores.addonpayments.com

    Subclasses values (fields to be defined in the subclasses):
        request_type            Type of the Addonpayments request (auth, receipt-in, payer-new, card-new, ...)
        hash_values             Hash a string made up of the request values
    Mixin XMLMixin attributes:
        xml_root_tag            If the object is a Request the root tag is <request attributes></ request>.
        xml_root_attributes     Normalized request objects always have timestamp and type attributes in the root tag
    """

    # Mandatory field
    merchantid = Field(validator=RequestValidator.merchant_id)
    type = Field(default=None)

    # Mandatory fields with auto-generation
    timestamp = Field(default=None, validator=RequestValidator.timestamp)
    orderid = Field(default=None, validator=RequestValidator.order_id)

    # Mandatory fields generated later
    sha1hash = Field(default=None, validator=RequestValidator.sha1hash)

    # Optional field
    account = Field(default='', validator=RequestValidator.account)

    # Static variables
    # Defined in subclasses
    request_type = ''
    hash_values = []
    # Default values for XmlMixin, all XML requests starts with <request type='' timestamp=''>
    xml_root_tag = 'request'
    xml_root_attributes = ['timestamp', 'type']

    def __attrs_post_init__(self):
        """
        This method will be called after the class is fully initialized.
        Uses method to set auto-generate values if they have not been initialized and request type
        """
        self.type = self.request_type
        gen_utl = GenerationUtils()
        if not self.timestamp:
            self.timestamp = gen_utl.generate_timestamp()
        if not self.orderid:
            self.orderid = gen_utl.generate_order_id()

    def get_hash_values(self):
        """
        This method return a list values to generate hash
        :return: list
        """
        return [getattr(self, f) for f in self.hash_values]

    def hash(self, secret):
        """
        Creates the security hash from a number of fields and the shared secret.
        :param secret: string
        """
        # Generate string to hash from fields values list
        str_hash = '.'.join(self.get_hash_values())
        # Generate HASH
        gen_utl = GenerationUtils()
        self.sha1hash = gen_utl.generate_hash(str_hash, secret)
        # Validate hash
        attr.validate(self)
        return self.sha1hash
