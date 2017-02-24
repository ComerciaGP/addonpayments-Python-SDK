# -*- encoding: utf-8 -*-

import attr

from addonpayments.hpp.common.requests import HppRequest


@attr.s
class PaymentRequest(HppRequest):
    """
    Class representing a payment request to be sent to HPP.
    """

    flag_fields = ['auto_settle_flag']
    hash_values = ['timestamp', 'merchant_id', 'order_id', 'amount', 'currency']
