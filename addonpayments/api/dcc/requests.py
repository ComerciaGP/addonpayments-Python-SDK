# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import attr
from attr import ib as Field

from addonpayments.api.common.requests import ApiRequest
from addonpayments.api.elements import Card, DccInfoWithRateType, DccInfoWithAmount
from addonpayments.api.mixins import FieldsAmountMixin, FieldsCommentMixin
from addonpayments.api.payment.requests import AuthRequest


@attr.s
class DccRate(FieldsAmountMixin, FieldsCommentMixin, ApiRequest):
    """
    Class representing a DCC rate request to be sent to API.
    """
    card = Field(default=None, validator=attr.validators.instance_of(Card))
    dccinfo = Field(default=None, validator=attr.validators.instance_of(DccInfoWithRateType))

    object_fields = ['card', 'dccinfo']
    request_type = 'dccrate'

    def get_hash_values(self):
        """
        Override function to get necessary hash values for this request
        :return: list
        """
        return [self.timestamp, self.merchantid, self.orderid, self.amount, self.currency, self.card.number]


@attr.s
class AuthRequestWithDccInfo(AuthRequest):
    """
    Class representing a authorisation with DCC info request to be sent to API.
    """
    dccinfo = Field(default=None, validator=attr.validators.instance_of(DccInfoWithAmount))

    object_fields = ['card', 'dccinfo']
