# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import pytest

from addonpayments.api.tests.conftest import BaseTest
from addonpayments.api.client import ApiClient
from addonpayments.api.dcc.requests import DccRate, AuthRequestWithDccInfo


class TestDcc(BaseTest):
    @pytest.mark.skip(reason="Dcc rate not allowed")
    def test_dcc_rate(self, dcc_info_with_rate_type, valid_card):
        request = DccRate(
            merchantid=self.merchant_id,
            card=valid_card,
            amount=100,
            currency='EUR',
            dccinfo=dcc_info_with_rate_type,
            comments=['comment one', 'comment two']
        )
        client = ApiClient(self.secret)
        response = client.send(request)
        assert response.result == '00'

    def test_auth_with_dcc_info(self, valid_card_with_cvn, dcc_info_with_amount):
        request = AuthRequestWithDccInfo(
            merchantid=self.merchant_id,
            card=valid_card_with_cvn,
            amount=100,
            currency='EUR',
            autosettle='1',
            comments=['comment one', 'comment two'],
            dccinfo=dcc_info_with_amount
        )
        client = ApiClient(self.secret)
        response = client.send(request)
        assert response.result == '00'
