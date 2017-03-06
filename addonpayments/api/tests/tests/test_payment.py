# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from addonpayments.api.tests.conftest import BaseTest
from addonpayments.api.client import ApiClient
from addonpayments.api.payment.requests import AuthRequest


class TestPayment(BaseTest):
    def test_auth_valid(self, valid_card_with_cvn):
        request = AuthRequest(
            merchantid=self.merchant_id,
            card=valid_card_with_cvn,
            amount=100,
            currency='EUR',
            autosettle='1',
            comments=['comment one', 'comment two']
        )
        client = ApiClient(self.secret)
        response = client.send(request)
        assert response.result == '00'

    def test_auth_declined(self, declined_card_with_cvn):
        request = AuthRequest(
            merchantid=self.merchant_id,
            card=declined_card_with_cvn,
            amount=100,
            currency='EUR',
            autosettle='1',
            comments=['comment one', 'comment two']
        )
        client = ApiClient(self.secret)
        response = client.send(request)
        assert response.result == '101'
