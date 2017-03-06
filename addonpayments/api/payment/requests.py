# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import attr
from attr import ib as Field

from addonpayments.api.common.requests import ApiRequest
from addonpayments.api.elements import Card
from addonpayments.api.mixins import FieldsAmountMixin, FieldsMixin


@attr.s
class AuthRequest(FieldsMixin, FieldsAmountMixin, ApiRequest):
    """
    Class representing a authorisation request to be sent to API.
    """
    card = Field(default=None, validator=attr.validators.instance_of(Card))

    object_fields = ['card']
    flag_fields = ['autosettle']
    request_type = 'auth'

    def get_hash_values(self):
        """
        Override function to get necessary hash values for this request
        :return: list
        """
        return [self.timestamp, self.merchantid, self.orderid, self.amount, self.currency, self.card.number]
