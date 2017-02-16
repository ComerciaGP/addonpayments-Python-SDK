# -*- encoding: utf-8 -*-

import attr
from attr import ib as Field

from sdk.api.common.requests import ApiRequest
from sdk.api.elements import Card, Recurring, Mpi, DccInfoWithAmount
from sdk.api.mixins import FieldsAmountMixin, FieldsMixin


@attr.s
class AuthRequest(FieldsMixin, FieldsAmountMixin, ApiRequest):
    """
    Class representing a authorisation request to be sent to API.
    """
    card = Field(default=None, validator=attr.validators.instance_of(Card))

    # Optional fields for a different requests
    recurring = Field(default=None, validator=attr.validators.optional(attr.validators.instance_of(Recurring)))
    mpi = Field(default=None, validator=attr.validators.optional(attr.validators.instance_of(Mpi)))
    dccinfo = Field(default=None, validator=attr.validators.optional(attr.validators.instance_of(DccInfoWithAmount)))

    object_fields = ['card', 'recurring', 'mpi', 'dccinfo']
    flag_fields = ['autosettle']
    request_type = 'auth'

    def get_hash_values(self):
        """
        Override function to get necessary hash values for this request
        :return: list
        """
        return [self.timestamp, self.merchantid, self.orderid, self.amount, self.currency, self.card.number]
