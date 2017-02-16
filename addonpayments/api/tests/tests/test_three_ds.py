# -*- encoding: utf-8 -*-

import pytest

from addonpayments.api.client import ApiClient
from addonpayments.api.tests.conftest import BaseTest
from addonpayments.api.three_ds.requests import ThreeDsVerifyEnrolled, ThreeDsVerifySig


class TestThreeDs(BaseTest):
    @pytest.mark.skip(reason="MPI for client not configured")
    def test_three_ds_verify_enrolled(self, valid_card):
        request = ThreeDsVerifyEnrolled(
            merchantid=self.merchant_id,
            card=valid_card,
            amount=100,
            currency='EUR',
            comments=['comment one', 'comment two']
        )
        client = ApiClient(self.secret)
        response = client.send(request)
        assert response['result'] == '00'

    @pytest.mark.skip(reason="MPI for client not configured")
    def test_three_ds_verify_sig(self):
        request = ThreeDsVerifySig(
            merchantid=self.merchant_id,
            amount=100,
            currency='EUR',
        )
        client = ApiClient(self.secret)
        response = client.send(request)
        assert response['result'] == '00'
