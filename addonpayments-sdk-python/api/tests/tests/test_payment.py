# -*- encoding: utf-8 -*-

import pytest

from sdk.api.client import ApiClient
from sdk.api.payment.requests import AuthRequest
from sdk.api.tests.conftest import BaseTest


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
        assert response['result'] == '00'

    @pytest.mark.skip(reason="Recurring not activated")
    def test_auth_recurring(self, valid_card_with_cvn, recurring):
        request = AuthRequest(
            merchantid=self.merchant_id,
            card=valid_card_with_cvn,
            amount=100,
            currency='EUR',
            autosettle='1',
            comments=['comment one', 'comment two'],
            recurring=recurring
        )
        client = ApiClient(self.secret)
        response = client.send(request)
        assert response['result'] == '00'

    def test_auth_with_three_ds(self, valid_card_with_cvn, mpi):
        request = AuthRequest(
            merchantid=self.merchant_id,
            card=valid_card_with_cvn,
            amount=100,
            currency='EUR',
            autosettle='1',
            comments=['comment one', 'comment two'],
            mpi=mpi
        )
        client = ApiClient(self.secret)
        response = client.send(request)
        assert response['result'] == '00'

    def test_auth_with_dcc_info(self, valid_card_with_cvn, dcc_info_with_amount):
        request = AuthRequest(
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
        assert response['result'] == '00'
