# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import attr
from attr import ib as Field

from addonpayments.hpp.common.requests import HppRequest
from addonpayments.validators import RequestValidator
from addonpayments.hpp.validators import HppValidator as Validator
from addonpayments.hpp.card_storage.validators import CardStorageValidator


@attr.s
class CardStorageRequest(HppRequest):
    """
    Class representing a card storage request to be sent to HPP.
    """

    # Mandatory
    card_storage_enable = Field(default='1', validator=RequestValidator.flag)
    offer_save_card = Field(default='0', validator=RequestValidator.flag)
    payer_exist = Field(default='0', validator=RequestValidator.flag)

    # Optional
    payer_ref = Field(default='', validator=Validator.payer_ref)
    pmt_ref = Field(default='', validator=Validator.pmt_ref)

    flag_fields = ['auto_settle_flag', 'card_storage_enable', 'offer_save_card', 'payer_exist']
    hash_fields = ['timestamp', 'merchant_id', 'order_id', 'amount', 'currency', 'payer_ref', 'pmt_ref']


@attr.s
class DisplayCardsRequest(HppRequest):
    """
    Class representing a display stored cards request to be sent to HPP.
    """

    # Mandatory
    hpp_select_stored_card = Field(default='', validator=CardStorageValidator.hpp_select_stored_card)
    offer_save_card = Field(default='0', validator=RequestValidator.flag)
    payer_exist = Field(default='1', validator=CardStorageValidator.payer_exist)

    flag_fields = ['auto_settle_flag', 'card_storage_enable', 'offer_save_card', 'payer_exist']

    def get_hash_values(self):
        """
        Override function to get necessary hash values for this request
        :return: list
        """
        # Empty values represents pmt_ref
        return [
            self.timestamp, self.merchant_id, self.order_id, self.amount,
            self.currency, self.hpp_select_stored_card, ''
        ]


@attr.s
class RecurringPaymentRequest(HppRequest):
    """
    Class representing a recurring payment request to be sent to HPP.
    """

    # Mandatory
    card_storage_enable = Field(default='1', validator=RequestValidator.flag)
    offer_save_card = Field(default='0', validator=RequestValidator.flag)
    payer_exist = Field(default='0', validator=RequestValidator.flag)

    # Optional
    payer_ref = Field(default='', validator=Validator.payer_ref)
    pmt_ref = Field(default='', validator=Validator.pmt_ref)

    recurring_type = Field(default='', validator=CardStorageValidator.recurring_type)
    recurring_sequence = Field(default='', validator=CardStorageValidator.recurring_sequence)

    flag_fields = ['auto_settle_flag', 'card_storage_enable', 'offer_save_card', 'payer_exist']
    hash_fields = ['timestamp', 'merchant_id', 'order_id', 'amount', 'currency', 'payer_ref', 'pmt_ref']
