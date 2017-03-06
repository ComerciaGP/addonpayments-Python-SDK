# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import attr
from attr import ib as Field

from addonpayments.api.payment.requests import AuthRequest
from addonpayments.api.validators import FieldsValidator as Validator
from addonpayments.api.common.requests import ApiRequest
from addonpayments.api.elements import PaymentData, Payer, CardWithRef, CardRef, DccInfo, Recurring
from addonpayments.api.mixins import FieldsAmountMixin, FieldsMixin, FieldsCommentMixin


@attr.s
class ReceiptInRequest(FieldsMixin, FieldsAmountMixin, ApiRequest):
    """
    Class representing a receipt in request to be sent to API.
    """
    payerref = Field(default=None, validator=Validator.ref)
    paymentmethod = Field(default=None, validator=Validator.ref)
    paymentdata = Field(default=None, validator=attr.validators.instance_of(PaymentData))

    request_type = 'receipt-in'
    object_fields = ['paymentdata']
    flag_fields = ['autosettle']
    hash_fields = ['timestamp', 'merchantid', 'orderid', 'amount', 'currency', 'payerref']


@attr.s
class RealVaultThreeDsVerifyEnrolled(FieldsAmountMixin, ApiRequest):
    """
    Class representing a 3D Secure verify Stored card enrolled to be sent to API.
    """
    payerref = Field(default=None, validator=Validator.ref)
    paymentmethod = Field(default=None, validator=Validator.ref)

    request_type = 'realvault-3ds-verifyenrolled'
    hash_fields = ['timestamp', 'merchantid', 'orderid', 'amount', 'currency', 'payerref']


@attr.s
class PayerNewRequest(FieldsCommentMixin, ApiRequest):
    """
    Class representing a new payer to be sent to API.
    """
    payer = Field(default=None, validator=attr.validators.instance_of(Payer))

    request_type = 'payer-new'
    object_fields = ['payer']

    def get_hash_values(self):
        """
        Override function to get necessary hash values for this request
        :return: list
        """
        # Empty values represents amount and currency
        return [self.timestamp, self.merchantid, self.orderid, '', '', self.payer.ref]


@attr.s
class PayerEditRequest(FieldsCommentMixin, ApiRequest):
    """
    Class representing a edit payer to be sent to API.
    """
    payer = Field(default=None, validator=attr.validators.instance_of(Payer))

    request_type = 'payer-edit'
    object_fields = ['payer']

    def get_hash_values(self):
        """
        Override function to get necessary hash values for this request
        :return: list
        """
        # Empty values represents amount and currency
        return [self.timestamp, self.merchantid, self.orderid, '', '', self.payer.ref]


@attr.s
class CardNewRequest(FieldsCommentMixin, ApiRequest):
    """
    Class representing a new card to be sent to API.
    """
    card = Field(default=None, validator=attr.validators.instance_of(CardWithRef))

    request_type = 'card-new'
    object_fields = ['card']

    def get_hash_values(self):
        """
        Override function to get necessary hash values for this request
        :return: list
        """
        # Empty values represents amount and currency
        return [
            self.timestamp,
            self.merchantid,
            self.orderid,
            '',
            '',
            self.card.payerref,
            self.card.chname,
            self.card.number
        ]


@attr.s
class CardUpdateRequest(FieldsCommentMixin, ApiRequest):
    """
    Class representing a card update to be sent to API.
    """
    card = Field(default=None, validator=attr.validators.instance_of(CardWithRef))

    request_type = 'card-update-card'
    object_fields = ['card']

    def get_hash_values(self):
        """
        Override function to get necessary hash values for this request
        :return: list
        """
        return [self.timestamp, self.merchantid, self.card.payerref, self.card.ref, self.card.expdate, self.card.number]


@attr.s
class CardCancelRequest(FieldsCommentMixin, ApiRequest):
    """
    Class representing a card cancellation to be sent to API.
    """
    card = Field(default=None, validator=attr.validators.instance_of(CardRef))

    request_type = 'card-cancel-card'
    object_fields = ['card']

    def get_hash_values(self):
        """
        Override function to get necessary hash values for this request
        :return: list
        """
        return [self.timestamp, self.merchantid, self.card.payerref, self.card.ref]


@attr.s
class CardDccRateRequest(FieldsAmountMixin, FieldsCommentMixin, ApiRequest):
    """
    Class representing a card dcc rate to be sent to API.
    """
    payerref = Field(default=None, validator=Validator.ref)
    paymentmethod = Field(default=None, validator=Validator.ref)
    dccinfo = Field(default=None, validator=attr.validators.instance_of(DccInfo))

    request_type = 'realvault-dccrate'
    object_fields = ['dccinfo']
    hash_fields = ['timestamp', 'merchantid', 'orderid', 'amount', 'currency', 'payerref']


@attr.s
class AuthRequestWithRecurring(AuthRequest):
    """
    Class representing a authorisation with 3DS request to be sent to API.
    """
    recurring = Field(default=None, validator=attr.validators.instance_of(Recurring))

    object_fields = ['card', 'recurring']
