# -*- encoding: utf-8 -*-

import pytest

from sdk.api.card_storage.requests import (ReceiptInRequest, CardUpdateRequest, CardNewRequest, CardCancelRequest,
                                           CardDccRateRequest, RealVaultThreeDsVerifyEnrolled, PayerNewRequest,
                                           PayerEditRequest)
from sdk.api.client import ApiClient
from sdk.api.tests.conftest import BaseTest


class TestCardStorage(BaseTest):
    @pytest.mark.skip(reason="API request Payer delete not implemented")
    def test_payer_new(self, payer):
        client = ApiClient(self.secret)
        request = PayerNewRequest(
            merchantid=self.merchant_id,
            payer=payer
        )
        response = client.send(request)
        assert response['result'] == '00'
        # TODO delete payer (API not implemented)

    def test_payer_edit(self, payer):
        client = ApiClient(self.secret)

        request_new = PayerNewRequest(
            merchantid=self.merchant_id,
            payer=payer
        )
        response_new = client.send(request_new)
        # Because it can not be removed, the payer may exist (501)
        assert response_new['result'] == '00' or response_new['result'] == '501'

        payer.firstname = 'Updated {}'.format(payer.firstname)
        request = PayerEditRequest(
            merchantid=self.merchant_id,
            payer=payer,
            comments=['comment one', 'comment two'],
        )
        response = client.send(request)
        assert response['result'] == '00'
        # TODO delete payer (API not implemented)

    @pytest.mark.skip(reason="MPI for client not configured")
    def test_three_ds_verify_enrolled(self, payer, valid_card_with_ref):
        client = ApiClient(self.secret)
        # Create payer if not exists
        request_new_payer = PayerNewRequest(
            merchantid=self.merchant_id,
            payer=payer
        )
        response_new_payer = client.send(request_new_payer)
        # Because it can not be removed, the payer may exist (501)
        assert response_new_payer['result'] == '00' or response_new_payer['result'] == '501'
        # Ensure that the payer reference is the correct
        valid_card_with_ref.payerref = payer.ref

        request_new = CardNewRequest(
            merchantid=self.merchant_id,
            comments=['comment one', 'comment two'],
            card=valid_card_with_ref
        )
        response_new = client.send(request_new)
        assert response_new['result'] == '00'

        request = RealVaultThreeDsVerifyEnrolled(
            merchantid=self.merchant_id,
            amount=100,
            currency='EUR',
            payerref=valid_card_with_ref.payerref,
            paymentmethod=valid_card_with_ref.ref,
        )
        response = client.send(request)
        assert response['result'] == '00'

        request_cancel = CardCancelRequest(
            merchantid=self.merchant_id,
            comments=['comment one', 'comment two'],
            card=valid_card_with_ref
        )
        response_cancel = client.send(request_cancel)
        assert response_cancel['result'] == '00'
        # TODO delete payer (API not implemented)

    def test_card_new(self, payer, valid_card_with_ref):
        client = ApiClient(self.secret)
        # Create payer if not exists
        request_new_payer = PayerNewRequest(
            merchantid=self.merchant_id,
            payer=payer
        )
        response_new_payer = client.send(request_new_payer)
        # Because it can not be removed, the payer may exist (501)
        assert response_new_payer['result'] == '00' or response_new_payer['result'] == '501'
        # Ensure that the payer reference is the correct
        valid_card_with_ref.payerref = payer.ref

        request_new = CardNewRequest(
            merchantid=self.merchant_id,
            comments=['comment one', 'comment two'],
            card=valid_card_with_ref
        )
        response_new = client.send(request_new)
        assert response_new['result'] == '00'

        request_cancel = CardCancelRequest(
            merchantid=self.merchant_id,
            comments=['comment one', 'comment two'],
            card=valid_card_with_ref
        )
        response_cancel = client.send(request_cancel)
        assert response_cancel['result'] == '00'
        # TODO delete payer (API not implemented)

    def test_receipt_in(self, payment_data, payer, valid_card_with_ref):
        client = ApiClient(self.secret)
        # Create payer if not exists
        request_new_payer = PayerNewRequest(
            merchantid=self.merchant_id,
            payer=payer
        )
        response_new_payer = client.send(request_new_payer)
        # Because it can not be removed, the payer may exist (501)
        assert response_new_payer['result'] == '00' or response_new_payer['result'] == '501'
        # Ensure that the payer reference is the correct
        valid_card_with_ref.payerref = payer.ref

        request_new = CardNewRequest(
            merchantid=self.merchant_id,
            comments=['comment one', 'comment two'],
            card=valid_card_with_ref
        )
        response_new = client.send(request_new)
        assert response_new['result'] == '00'

        request = ReceiptInRequest(
            merchantid=self.merchant_id,
            amount=100,
            currency='EUR',
            autosettle='1',
            comments=['comment one', 'comment two'],
            payerref=valid_card_with_ref.payerref,
            paymentmethod=valid_card_with_ref.ref,
            paymentdata=payment_data
        )
        response = client.send(request)
        assert response['result'] == '00'

        request_cancel = CardCancelRequest(
            merchantid=self.merchant_id,
            comments=['comment one', 'comment two'],
            card=valid_card_with_ref
        )
        response_cancel = client.send(request_cancel)
        assert response_cancel['result'] == '00'
        # TODO delete payer (API not implemented)

    def test_card_update(self, payer, valid_card_with_ref):
        client = ApiClient(self.secret)
        # Create payer if not exists
        request_new_payer = PayerNewRequest(
            merchantid=self.merchant_id,
            payer=payer
        )
        response_new_payer = client.send(request_new_payer)
        # Because it can not be removed, the payer may exist (501)
        assert response_new_payer['result'] == '00' or response_new_payer['result'] == '501'
        # Ensure that the payer reference is the correct
        valid_card_with_ref.payerref = payer.ref

        request_new = CardNewRequest(
            merchantid=self.merchant_id,
            comments=['comment one', 'comment two'],
            card=valid_card_with_ref
        )
        response_new = client.send(request_new)
        assert response_new['result'] == '00'

        valid_card_with_ref.chname = 'update card owner'

        request = CardUpdateRequest(
            merchantid=self.merchant_id,
            comments=['comment one', 'comment two'],
            card=valid_card_with_ref
        )
        response = client.send(request)
        assert response['result'] == '00'

        request_cancel = CardCancelRequest(
            merchantid=self.merchant_id,
            comments=['comment one', 'comment two'],
            card=valid_card_with_ref
        )
        response_cancel = client.send(request_cancel)
        assert response_cancel['result'] == '00'
        # TODO delete payer (API not implemented)

    def test_card_cancel(self, payer, valid_card_with_ref):
        client = ApiClient(self.secret)
        # Create payer if not exists
        request_new_payer = PayerNewRequest(
            merchantid=self.merchant_id,
            payer=payer
        )
        response_new_payer = client.send(request_new_payer)
        # Because it can not be removed, the payer may exist (501)
        assert response_new_payer['result'] == '00' or response_new_payer['result'] == '501'
        # Ensure that the payer reference is the correct
        valid_card_with_ref.payerref = payer.ref

        request_new = CardNewRequest(
            merchantid=self.merchant_id,
            comments=['comment one', 'comment two'],
            card=valid_card_with_ref
        )
        response_new = client.send(request_new)
        assert response_new['result'] == '00'

        request = CardCancelRequest(
            merchantid=self.merchant_id,
            comments=['comment one', 'comment two'],
            card=valid_card_with_ref
        )
        response = client.send(request)
        assert response['result'] == '00'
        # TODO delete payer (API not implemented)

    @pytest.mark.skip(reason="Dcc rate not allowed")
    def test_real_vault_dcc_rate(self, payer, valid_card_with_ref, dcc_info):
        client = ApiClient(self.secret)
        # Create payer if not exists
        request_new_payer = PayerNewRequest(
            merchantid=self.merchant_id,
            payer=payer
        )
        response_new_payer = client.send(request_new_payer)
        # Because it can not be removed, the payer may exist (501)
        assert response_new_payer['result'] == '00' or response_new_payer['result'] == '501'
        # Ensure that the payer reference is the correct
        valid_card_with_ref.payerref = payer.ref

        request_new = CardNewRequest(
            merchantid=self.merchant_id,
            comments=['comment one', 'comment two'],
            card=valid_card_with_ref
        )
        response_new = client.send(request_new)
        assert response_new['result'] == '00'

        request = CardDccRateRequest(
            merchantid=self.merchant_id,
            amount=100,
            currency='EUR',
            payerref=valid_card_with_ref.payerref,
            paymentmethod=valid_card_with_ref.ref,
            comments=['comment one', 'comment two'],
            dccinfo=dcc_info
        )
        response = client.send(request)
        assert response['result'] == '00'

        request = CardCancelRequest(
            merchantid=self.merchant_id,
            comments=['comment one', 'comment two'],
            card=valid_card_with_ref
        )
        response = client.send(request)
        assert response['result'] == '00'
        # TODO delete payer (API not implemented)
