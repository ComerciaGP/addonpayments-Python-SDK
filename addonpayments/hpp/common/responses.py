# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from addonpayments.responses import SdkResponse


class HppResponse(SdkResponse):
    """
    Class representing the HPP response.

    You can consult the specific documentation of all HPP response fields on the website
    https://desarrolladores.addonpayments.com
    """

    hash_fields = ['timestamp', 'merchant_id', 'order_id', 'result', 'message', 'pasref', 'authcode']
