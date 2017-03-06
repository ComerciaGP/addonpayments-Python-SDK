# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from addonpayments.responses import SdkResponse


class ApiResponse(SdkResponse):
    """
    Class representing the API response.

    You can consult the specific documentation of all API response fields on the website
    https://desarrolladores.addonpayments.com
    """

    hash_fields = ['timestamp', 'merchantid', 'orderid', 'result', 'message', 'pasref', 'authcode']
