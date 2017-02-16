# -*- encoding: utf-8 -*-

import attr
from attr import ib as Field

from api.common.requests import ApiRequest
from api.elements import Card, DccInfoWithRateType
from api.mixins import FieldsAmountMixin, FieldsCommentMixin


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
