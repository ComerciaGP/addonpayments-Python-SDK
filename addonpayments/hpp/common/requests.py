# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import attr
import six
from attr import ib as Field

from addonpayments.mixins import DictMixin, HashMixin
from addonpayments.utils import GenerationUtils
from addonpayments.validators import RequestValidator
from addonpayments.hpp.validators import HppValidator as Validator


@attr.s
class HppRequest(HashMixin, DictMixin):
    """
    Super class representing a request to be sent to HPP.
    This class contains all common attributes and functions for all other classes.

    You can consult the specific documentation of all HPP request fields on the website
    https://desarrolladores.addonpayments.com
    """

    # Mandatory fields
    merchant_id = Field(validator=RequestValidator.merchant_id)
    amount = Field(convert=str, validator=RequestValidator.amount)
    currency = Field(validator=RequestValidator.currency)
    auto_settle_flag = Field(validator=RequestValidator.flag)

    # Mandatory fields with auto-generation
    timestamp = Field(default=None, validator=RequestValidator.timestamp)
    order_id = Field(default=None, validator=RequestValidator.order_id)

    # Mandatory fields generated later
    sha1hash = Field(default=None, validator=RequestValidator.sha1hash)

    # Optional fields
    account = Field(default='', validator=RequestValidator.account)
    comment1 = Field(default='', validator=Validator.comment)
    comment2 = Field(default='', validator=Validator.comment)
    shipping_code = Field(default='', validator=Validator.shipping_code)
    shipping_co = Field(default='', validator=Validator.country)
    billing_code = Field(default='', validator=Validator.billing_code)
    billing_co = Field(default='', validator=Validator.country)
    cust_num = Field(default='', validator=Validator.additional_info)
    var_ref = Field(default='', validator=Validator.additional_info)
    prod_id = Field(default='', validator=Validator.additional_info)
    hpp_lang = Field(default='', validator=Validator.lang)
    hpp_version = Field(default='')
    merchant_response_url = Field(default='', validator=Validator.url)
    card_payment_button = Field(default='', validator=Validator.card_payment_button)
    supplementary_data = Field(default={}, validator=Validator.supplementary_data)

    def __attrs_post_init__(self):
        """
        This method will be called after the class is fully initialized.
        Uses method to set auto-generate values if they have not been initialized
        """
        if not self.timestamp:
            self.timestamp = GenerationUtils().generate_timestamp()
        if not self.order_id:
            self.order_id = GenerationUtils().generate_order_id()

    def to_dict(self):
        """
        Overrides to_dict method from DictMixin to set the supplementary data
        :return: dict
        """
        result = {}
        for key, value in six.iteritems(self.__dict__):
            # Add supplementary data into dict
            if key == 'supplementary_data':
                try:
                    for key_supp, value_supp in six.iteritems(self.supplementary_data):
                        if key_supp not in six.iterkeys(self.__dict__):
                            result[key_supp] = value_supp
                except AttributeError:
                    result[key.upper()] = value
            else:
                # Parse boolean fields to str '1' (True) or '0' (False)
                result_value = self.set_flags(key, value)
                if result_value:
                    result[key.upper()] = result_value
        return result

    def hash(self, secret):
        """
        Set and validate sha1hash
        :param secret: string
        """
        self.sha1hash = self.generate_hash(secret)
        # Validate hash
        attr.validate(self)
        return self.sha1hash
