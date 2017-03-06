# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import pytest

from addonpayments.api.tests.conftest import BaseTest
from addonpayments.api.client import ApiClient
from addonpayments.api.payment.requests import AuthRequest
from addonpayments.api.transaction_management.requests import Settle, Rebate, Void


class TestTransactionManagement(BaseTest):
    @pytest.mark.skip(reason="Settle not works")
    def test_settle(self, valid_card_with_cvn):
        client = ApiClient(self.secret)
        auth_request = AuthRequest(
            merchantid=self.merchant_id,
            card=valid_card_with_cvn,
            amount=100,
            currency='EUR',
            autosettle='1',
            comments=['comment one', 'comment two']
        )

        auth_response = client.send(auth_request)
        assert auth_response.result == '00'

        request = Settle(
            merchantid=self.merchant_id,
            pasref=auth_response.pasref,
            amount=100,
            comments=['comment one', 'comment two']
        )
        response = client.send(request)
        assert response.result == '00'

    @pytest.mark.skip(reason="Refund hash not defined into documentation")
    def test_rebate(self, valid_card_with_cvn):
        client = ApiClient(self.secret)
        auth_request = AuthRequest(
            merchantid=self.merchant_id,
            card=valid_card_with_cvn,
            amount=100,
            currency='EUR',
            autosettle='1',
            comments=['comment one', 'comment two']
        )

        auth_response = client.send(auth_request)
        assert auth_response.result == '00'

        request = Rebate(
            merchantid=self.merchant_id,
            amount=100,
            currency='EUR',
            pasref=auth_response.pasref,
            authcode=auth_response.authcode,
            refundhash=auth_request.sha1hash,
            comments=['comment one', 'comment two']
        )
        response = client.send(request)
        assert response.result == '00'

    @pytest.mark.skip(reason="Void not works")
    def test_void(self, valid_card_with_cvn):
        client = ApiClient(self.secret)
        auth_request = AuthRequest(
            merchantid=self.merchant_id,
            card=valid_card_with_cvn,
            amount=100,
            currency='EUR',
            autosettle='1',
            comments=['comment one', 'comment two']
        )

        auth_response = client.send(auth_request)
        assert auth_response.result == '00'

        request = Void(
            merchantid=self.merchant_id,
            pasref=auth_response.pasref,
        )
        response = client.send(request)
        assert response.result == '00'
