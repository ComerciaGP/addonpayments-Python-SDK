# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import attr
from attr import ib as Field

from addonpayments.api.common.requests import ApiRequest
from addonpayments.api.elements import Card, Mpi
from addonpayments.api.mixins import FieldsAmountMixin, FieldsCommentMixin
from addonpayments.api.payment.requests import AuthRequest
from addonpayments.api.three_ds.validators import ThreeDSValidator


@attr.s
class ThreeDsVerifyEnrolled(FieldsAmountMixin, FieldsCommentMixin, ApiRequest):
    """
    Class representing a 3D Secure verifying card request to be sent to API.
    """
    card = Field(default=None, validator=attr.validators.instance_of(Card))

    object_fields = ['card']
    request_type = '3ds-verifyenrolled'

    def get_hash_values(self):
        return [self.timestamp, self.merchantid, self.orderid, self.amount, self.currency, self.card.number]


@attr.s
class ThreeDsVerifySig(FieldsAmountMixin, ApiRequest):
    """
    Class representing a 3D Secure signature verification request to be sent to API.
    """
    pares = Field(default=None, validator=ThreeDSValidator.pares)

    request_type = '3ds-verifysig'

    def get_hash_values(self):
        return [self.timestamp, self.merchantid, self.orderid, self.amount, self.currency, '']


@attr.s
class AuthRequestWithThreeDS(AuthRequest):
    """
    Class representing a authorisation with 3DS request to be sent to API.
    """
    mpi = Field(default=None, validator=attr.validators.instance_of(Mpi))

    object_fields = ['card', 'mpi']
