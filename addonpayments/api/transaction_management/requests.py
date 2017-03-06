# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import attr
from attr import ib as Field

from addonpayments.api.transaction_management.validators import TransactionManagementValidator
from addonpayments.api.common.requests import ApiRequest
from addonpayments.api.mixins import FieldsAmountMixin, FieldsCommentMixin
from addonpayments.validators import RequestValidator


@attr.s
class Settle(FieldsCommentMixin, ApiRequest):
    """
    Class representing a settle request to be sent to API.
    """
    pasref = Field(default='', validator=TransactionManagementValidator.pasref)
    amount = Field(default='', convert=str, validator=RequestValidator.amount)

    request_type = 'settle'

    def get_hash_values(self):
        """
        Override function to get necessary hash values for this request
        :return: list
        """
        # Empty values represents currency and card number
        return [self.timestamp, self.merchantid, self.orderid, self.amount, '', '']


@attr.s
class Rebate(FieldsAmountMixin, FieldsCommentMixin, ApiRequest):
    """
    Class representing a rebate request to be sent to API.
    """
    pasref = Field(default='', validator=TransactionManagementValidator.pasref)
    authcode = Field(default='', validator=TransactionManagementValidator.authcode)
    refundhash = Field(default=None, validator=RequestValidator.sha1hash)

    request_type = 'rebate'

    def get_hash_values(self):
        """
        Override function to get necessary hash values for this request
        :return: list
        """
        # Empty values represents amount and currency
        return [self.timestamp, self.merchantid, self.orderid, self.amount, self.currency, '']


@attr.s
class Void(FieldsCommentMixin, ApiRequest):
    """
    Class representing a void request to be sent to API.
    """
    pasref = Field(default='', validator=TransactionManagementValidator.pasref)

    request_type = 'void'

    def get_hash_values(self):
        """
        Override function to get necessary hash values for this request
        :return: list
        """
        # Empty values represents amount and currency
        return [self.timestamp, self.merchantid, self.orderid, '', '', '']
