# -*- encoding: utf-8 -*-

import attr
from attr import ib as Field

from sdk.hpp.common.requests import HppRequest
from sdk.utils import GenerationUtils
from sdk.hpp.validators import HppValidator as Validator


@attr.s
class CardStorageRequest(HppRequest):
    """
    Class representing a request to be sent to HPP.
    """

    # Mandatory only for card storage fields (definition as optional)
    card_storage_enable = Field(default='0', validator=Validator.flag)
    offer_save_card = Field(default='0', validator=Validator.flag)
    payer_exist = Field(default='0', validator=Validator.flag)

    # Optional only for card storage fields
    payer_ref = Field(default='', validator=Validator.payer_ref)
    pmt_ref = Field(default='', validator=Validator.pmt_ref)

    hpp_select_stored_card = Field(default='', validator=Validator.hpp_select_stored_card)

    flag_fields = [
        'auto_settle_flag', 'card_storage_enable', 'offer_save_card', 'payer_exist'
    ]

    def hash(self, secret):
        """
        Creates the security hash from a number of fields and the shared secret.
        :param secret: string
        """
        # Get required values to generate HASH
        str_hash = '{}.{}.{}.{}.{}.{}.{}'.format(
            self.timestamp, self.merchant_id, self.order_id, self.amount,
            self.currency, self.payer_ref, self.pmt_ref
        )
        # Generate HASH
        gen_utl = GenerationUtils()
        self.sha1hash = gen_utl.generate_hash(str_hash, secret)
        return self.sha1hash
