# -*- encoding: utf-8 -*-

import pytest

from api.client import ApiClient
from api.dcc.requests import DccRate
from api.tests.conftest import BaseTest


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
        assert response['result'] == '00'
