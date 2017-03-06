# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import pytest

from addonpayments.api.tests.conftest import BaseTest
from addonpayments.api.client import ApiClient
from addonpayments.api.three_ds.requests import ThreeDsVerifyEnrolled, ThreeDsVerifySig, AuthRequestWithThreeDS


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
        assert response.result == '00'

    @pytest.mark.skip(reason="MPI for client not configured")
    def test_three_ds_verify_sig(self):
        request = ThreeDsVerifySig(
            merchantid=self.merchant_id,
            amount=100,
            currency='EUR',
            pares="eJzNV1uTokoSft9fMdHn0ZiB4qIwQbtR3FFBQZDLGzcB5SagIL9+sZ3p6T3RJ87sPmzsE1UZWV9+WZUfWcX8cyjyL7"
                  "e4abOqfH0B39CXL3EZVlFWJq8vlil+pV7+ufwHY6ZNHPP7OLw28ZJR47b1k/hLFr2+xEc/9vEAhCGOE4uIprAopDGMWvg0PQ/x6"
                  "GXJ7KARt2/OACUoFCepyfgj5nIK+Q1jkJ/TCbsJU7/slowfXlhFWxIowFCUQX5MmSJuFH5JE/icxDHAIM85g/xauLs+Ru1EdMii"
                  "3H6Tyn0zOkuod3kv9kC3i2UPW2554lKAn9amWYH8qM/dCtjLaXfnarYXV/dqu0d52882wSnSKcAgz9rHu9S3DqXn8twfdOpfTqaf"
                  "qa4f1XpxJG1Xy3/R/J//fkQvLRcLTizc3aSLq0rzqvpqxD1u6dqYlk4nn6UbO1T2occZ/1a2m4GHONO/F2ZAbSHoZy1FrZBV8dBW"
                  "gOeIcrGV8eVfYULSiXvlxbkOlsFscbyZbBjptNbaom9pJbnYBjm/R6JAVxzRchr2H9fecfBpMkisAN0mwzD3ZpvhCrORlmLup07N"
                  "92G30IF5XBJrMDkqXWpUPv241XDolt8Lv4fOdtgasvJOF4ptw6sDih0bmRD5Q4b+prKiO4FZFjJjbH+8YwnUiGyjDjJQcZhjLFUe"
                  "Dqjl4ratXNR2eXlZrorTf62mx7AwQhmOdnAz2Tzv0SEFq9GB17JAh003JnbbrgXzUU08vzGRtTA+1uR/ipXJBfdz7k/R7464b49r"
                  "J7e24+XiMfn6H/AvBh19Q="
        )
        client = ApiClient(self.secret)
        response = client.send(request)
        assert response.result == '00'

    def test_auth_with_three_ds(self, valid_card_with_cvn, mpi):
        request = AuthRequestWithThreeDS(
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
        assert response.result == '00'
