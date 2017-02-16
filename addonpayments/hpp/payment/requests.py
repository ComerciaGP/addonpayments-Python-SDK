# -*- encoding: utf-8 -*-

import attr

from addonpayments.utils import GenerationUtils
from addonpayments.hpp.common.requests import HppRequest


@attr.s
class PaymentRequest(HppRequest):
    """
    Class representing a payment request to be sent to HPP.
    """

    flag_fields = ['auto_settle_flag']

    def hash(self, secret):
        """
        Creates the security hash from a number of fields and the shared secret.
        :param secret: string
        """
        # Get required values to generate HASH
        str_hash = '{}.{}.{}.{}.{}'.format(
            self.timestamp, self.merchant_id, self.order_id, self.amount, self.currency
        )
        # Generate HASH
        gen_utl = GenerationUtils()
        self.sha1hash = gen_utl.generate_hash(str_hash, secret)
        return self.sha1hash
