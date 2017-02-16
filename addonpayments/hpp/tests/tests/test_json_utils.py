# -*- encoding: utf-8 -*-

from addonpayments.hpp.card_storage.requests import CardStorageRequest
from addonpayments.hpp.payment.requests import PaymentRequest


class TestJsonUtils:
    def test_from_json_hpp_payment_request(self, json_hpp_payment_request_valid):
        """
        Test PaymentRequest generated from JSON
        :param json_hpp_payment_request_valid: PaymentRequest
        """
        assert isinstance(json_hpp_payment_request_valid, PaymentRequest)
        assert json_hpp_payment_request_valid.merchant_id == "MerchantID"
        assert json_hpp_payment_request_valid.account == "myAccount"
        assert json_hpp_payment_request_valid.order_id == "OrderID"
        assert json_hpp_payment_request_valid.amount == "100"
        assert json_hpp_payment_request_valid.currency == "EUR"
        assert json_hpp_payment_request_valid.timestamp == "20990101120000"
        assert json_hpp_payment_request_valid.sha1hash == "5d8f05abd618e50db4861a61cc940112786474cf"
        assert json_hpp_payment_request_valid.auto_settle_flag == "1"
        comment1 = "a-z A-Z 0-9 ' \", + “” ._ - & \\ / @ ! ? % ( )* : £ $ & € # [ ] | = ;" \
                   "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷ø¤ùúûüýþÿŒŽšœžŸ¥"
        assert json_hpp_payment_request_valid.comment1 == comment1
        assert json_hpp_payment_request_valid.comment2 == "Comment Two"
        assert json_hpp_payment_request_valid.shipping_code == "56|987"
        assert json_hpp_payment_request_valid.shipping_co == "IRELAND"
        assert json_hpp_payment_request_valid.billing_code == "123|56"
        assert json_hpp_payment_request_valid.billing_co == "IRELAND"
        assert json_hpp_payment_request_valid.cust_num == "123456"
        assert json_hpp_payment_request_valid.var_ref == "VariableRef"
        assert json_hpp_payment_request_valid.prod_id == "ProductID"
        assert json_hpp_payment_request_valid.hpp_lang == "EN"
        assert json_hpp_payment_request_valid.card_payment_button == "Submit Payment"

    def test_from_json_hpp_payment_request_supplementary_data(self, json_hpp_payment_request_supplementary_data):
        """
        Test PaymentRequest with supplementary data () generated from JSON
        :param json_hpp_payment_request_supplementary_data: PaymentRequest
        """
        assert isinstance(json_hpp_payment_request_supplementary_data, PaymentRequest)
        assert json_hpp_payment_request_supplementary_data.merchant_id == "MerchantID"
        assert json_hpp_payment_request_supplementary_data.account == "myAccount"
        assert json_hpp_payment_request_supplementary_data.order_id == "OrderID"
        assert json_hpp_payment_request_supplementary_data.amount == "100"
        assert json_hpp_payment_request_supplementary_data.currency == "EUR"
        assert json_hpp_payment_request_supplementary_data.timestamp == "20990101120000"
        assert json_hpp_payment_request_supplementary_data.sha1hash == "5d8f05abd618e50db4861a61cc940112786474cf"
        assert json_hpp_payment_request_supplementary_data.auto_settle_flag == "1"
        comment1 = "a-z A-Z 0-9 ' \", + “” ._ - & \\ / @ ! ? % ( )* : £ $ & € # [ ] | ="
        assert json_hpp_payment_request_supplementary_data.comment1 == comment1
        assert json_hpp_payment_request_supplementary_data.comment2 == "Comment Two"
        assert json_hpp_payment_request_supplementary_data.shipping_code == "56|987"
        assert json_hpp_payment_request_supplementary_data.shipping_co == "IRELAND"
        assert json_hpp_payment_request_supplementary_data.billing_code == "123|56"
        assert json_hpp_payment_request_supplementary_data.billing_co == "IRELAND"
        assert json_hpp_payment_request_supplementary_data.cust_num == "123456"
        assert json_hpp_payment_request_supplementary_data.var_ref == "VariableRef"
        assert json_hpp_payment_request_supplementary_data.prod_id == "ProductID"
        assert json_hpp_payment_request_supplementary_data.hpp_lang == "EN"
        assert json_hpp_payment_request_supplementary_data.card_payment_button == "Submit Payment"
        assert isinstance(json_hpp_payment_request_supplementary_data.supplementary_data, dict)
        assert json_hpp_payment_request_supplementary_data.supplementary_data['supplementary_1'] == "Supp1"
        assert json_hpp_payment_request_supplementary_data.supplementary_data['supplementary_2'] == "Supp2"
        assert json_hpp_payment_request_supplementary_data.supplementary_data['supplementary_3'] == "Supp3"
        assert json_hpp_payment_request_supplementary_data.supplementary_data['supplementary_4'] == "Supp4"

    def test_from_json_hpp_payment_request_encoded(self, json_hpp_payment_request_encoded):
        """
        Test PaymentRequest with supplementary data () generated from JSON
        :param json_hpp_payment_request_encoded: PaymentRequest
        """
        assert isinstance(json_hpp_payment_request_encoded, PaymentRequest)
        assert json_hpp_payment_request_encoded.merchant_id == "MerchantID"
        assert json_hpp_payment_request_encoded.account == "myAccount"
        assert json_hpp_payment_request_encoded.order_id == "OrderID"
        assert json_hpp_payment_request_encoded.amount == "100"
        assert json_hpp_payment_request_encoded.currency == "EUR"
        assert json_hpp_payment_request_encoded.timestamp == "20990101120000"
        assert json_hpp_payment_request_encoded.sha1hash == "5d8f05abd618e50db4861a61cc940112786474cf"
        assert json_hpp_payment_request_encoded.comment1 == "Comment Two"
        assert json_hpp_payment_request_encoded.comment2 == "Comment Two"
        assert json_hpp_payment_request_encoded.auto_settle_flag == "1"
        assert json_hpp_payment_request_encoded.shipping_code == "56|987"
        assert json_hpp_payment_request_encoded.shipping_co == "IRELAND"
        assert json_hpp_payment_request_encoded.billing_code == "123|56"
        assert json_hpp_payment_request_encoded.billing_co == "IRELAND"
        assert json_hpp_payment_request_encoded.cust_num == "123456"
        assert json_hpp_payment_request_encoded.var_ref == "VariableRef"
        assert json_hpp_payment_request_encoded.prod_id == "ProductID"
        assert json_hpp_payment_request_encoded.hpp_lang == "EN"
        assert json_hpp_payment_request_encoded.card_payment_button == "Submit Payment"
        assert isinstance(json_hpp_payment_request_encoded.supplementary_data, dict)
        assert json_hpp_payment_request_encoded.supplementary_data['return_tss'] == "0"

    def test_from_json_hpp_card_storage_request(self, json_hpp_card_storage_request_valid):
        """
        Test CardStorageRequest generated from JSON
        :param json_hpp_card_storage_request_valid: CardStorageRequest
        """
        assert isinstance(json_hpp_card_storage_request_valid, CardStorageRequest)
        assert json_hpp_card_storage_request_valid.merchant_id == "MerchantID"
        assert json_hpp_card_storage_request_valid.account == "myAccount"
        assert json_hpp_card_storage_request_valid.order_id == "OrderID"
        assert json_hpp_card_storage_request_valid.amount == "100"
        assert json_hpp_card_storage_request_valid.currency == "EUR"
        assert json_hpp_card_storage_request_valid.timestamp == "20990101120000"
        assert json_hpp_card_storage_request_valid.sha1hash == "5d8f05abd618e50db4861a61cc940112786474cf"
        assert json_hpp_card_storage_request_valid.auto_settle_flag == "1"
        comment1 = "a-z A-Z 0-9 ' \", + “” ._ - & \\ / @ ! ? % ( )* : £ $ & € # [ ] | = ;" \
                   "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷ø¤ùúûüýþÿŒŽšœžŸ¥"
        assert json_hpp_card_storage_request_valid.comment1 == comment1
        assert json_hpp_card_storage_request_valid.comment2 == "Comment Two"
        assert json_hpp_card_storage_request_valid.shipping_code == "56|987"
        assert json_hpp_card_storage_request_valid.shipping_co == "IRELAND"
        assert json_hpp_card_storage_request_valid.billing_code == "123|56"
        assert json_hpp_card_storage_request_valid.billing_co == "IRELAND"
        assert json_hpp_card_storage_request_valid.cust_num == "123456"
        assert json_hpp_card_storage_request_valid.var_ref == "VariableRef"
        assert json_hpp_card_storage_request_valid.prod_id == "ProductID"
        assert json_hpp_card_storage_request_valid.hpp_lang == "EN"
        assert json_hpp_card_storage_request_valid.card_payment_button == "Submit Payment"
        assert json_hpp_card_storage_request_valid.card_storage_enable == "1"
        assert json_hpp_card_storage_request_valid.offer_save_card == "1"
        assert json_hpp_card_storage_request_valid.payer_ref == "PayerRef"
        assert json_hpp_card_storage_request_valid.pmt_ref == "PaymentRef"
        assert json_hpp_card_storage_request_valid.payer_exist == "1"

    def test_from_json_hpp_card_storage_request_supplementary_data(self,
                                                                   json_hpp_card_storage_request_supplementary_data):
        """
        Test CardStorageRequest with supplementary data () generated from JSON
        :param json_hpp_card_storage_request_supplementary_data: CardStorageRequest
        """
        assert isinstance(json_hpp_card_storage_request_supplementary_data, CardStorageRequest)
        assert json_hpp_card_storage_request_supplementary_data.merchant_id == "MerchantID"
        assert json_hpp_card_storage_request_supplementary_data.account == "myAccount"
        assert json_hpp_card_storage_request_supplementary_data.order_id == "OrderID"
        assert json_hpp_card_storage_request_supplementary_data.amount == "100"
        assert json_hpp_card_storage_request_supplementary_data.currency == "EUR"
        assert json_hpp_card_storage_request_supplementary_data.timestamp == "20990101120000"
        assert json_hpp_card_storage_request_supplementary_data.sha1hash == "5d8f05abd618e50db4861a61cc940112786474cf"
        assert json_hpp_card_storage_request_supplementary_data.auto_settle_flag == "1"
        comment1 = "a-z A-Z 0-9 ' \", + “” ._ - & \\ / @ ! ? % ( )* : £ $ & € # [ ] | ="
        assert json_hpp_card_storage_request_supplementary_data.comment1 == comment1
        assert json_hpp_card_storage_request_supplementary_data.comment2 == "Comment Two"
        assert json_hpp_card_storage_request_supplementary_data.shipping_code == "56|987"
        assert json_hpp_card_storage_request_supplementary_data.shipping_co == "IRELAND"
        assert json_hpp_card_storage_request_supplementary_data.billing_code == "123|56"
        assert json_hpp_card_storage_request_supplementary_data.billing_co == "IRELAND"
        assert json_hpp_card_storage_request_supplementary_data.cust_num == "123456"
        assert json_hpp_card_storage_request_supplementary_data.var_ref == "VariableRef"
        assert json_hpp_card_storage_request_supplementary_data.prod_id == "ProductID"
        assert json_hpp_card_storage_request_supplementary_data.hpp_lang == "EN"
        assert json_hpp_card_storage_request_supplementary_data.card_payment_button == "Submit Payment"
        assert json_hpp_card_storage_request_supplementary_data.card_storage_enable == "1"
        assert json_hpp_card_storage_request_supplementary_data.offer_save_card == "1"
        assert json_hpp_card_storage_request_supplementary_data.payer_ref == "PayerRef"
        assert json_hpp_card_storage_request_supplementary_data.pmt_ref == "PaymentRef"
        assert json_hpp_card_storage_request_supplementary_data.payer_exist == "1"
        assert isinstance(json_hpp_card_storage_request_supplementary_data.supplementary_data, dict)
        assert json_hpp_card_storage_request_supplementary_data.supplementary_data['supplementary_1'] == "Supp1"
        assert json_hpp_card_storage_request_supplementary_data.supplementary_data['supplementary_2'] == "Supp2"
        assert json_hpp_card_storage_request_supplementary_data.supplementary_data['supplementary_3'] == "Supp3"
        assert json_hpp_card_storage_request_supplementary_data.supplementary_data['supplementary_4'] == "Supp4"

    def test_from_json_hpp_card_storage_request_encoded(self, json_hpp_card_storage_request_encoded):
        """
        Test CardStorageRequest with supplementary data () generated from JSON
        :param json_hpp_card_storage_request_encoded: CardStorageRequest
        """
        assert isinstance(json_hpp_card_storage_request_encoded, CardStorageRequest)
        assert json_hpp_card_storage_request_encoded.merchant_id == "MerchantID"
        assert json_hpp_card_storage_request_encoded.account == "myAccount"
        assert json_hpp_card_storage_request_encoded.order_id == "OrderID"
        assert json_hpp_card_storage_request_encoded.amount == "100"
        assert json_hpp_card_storage_request_encoded.currency == "EUR"
        assert json_hpp_card_storage_request_encoded.timestamp == "20990101120000"
        assert json_hpp_card_storage_request_encoded.sha1hash == "5d8f05abd618e50db4861a61cc940112786474cf"
        assert json_hpp_card_storage_request_encoded.comment1 == "Comment Two"
        assert json_hpp_card_storage_request_encoded.comment2 == "Comment Two"
        assert json_hpp_card_storage_request_encoded.auto_settle_flag == "1"
        assert json_hpp_card_storage_request_encoded.shipping_code == "56|987"
        assert json_hpp_card_storage_request_encoded.shipping_co == "IRELAND"
        assert json_hpp_card_storage_request_encoded.billing_code == "123|56"
        assert json_hpp_card_storage_request_encoded.billing_co == "IRELAND"
        assert json_hpp_card_storage_request_encoded.cust_num == "123456"
        assert json_hpp_card_storage_request_encoded.var_ref == "VariableRef"
        assert json_hpp_card_storage_request_encoded.prod_id == "ProductID"
        assert json_hpp_card_storage_request_encoded.hpp_lang == "EN"
        assert json_hpp_card_storage_request_encoded.card_payment_button == "Submit Payment"
        assert json_hpp_card_storage_request_encoded.card_storage_enable == "1"
        assert json_hpp_card_storage_request_encoded.offer_save_card == "1"
        assert json_hpp_card_storage_request_encoded.payer_exist == "0"
        assert isinstance(json_hpp_card_storage_request_encoded.supplementary_data, dict)
        assert json_hpp_card_storage_request_encoded.supplementary_data['return_tss'] == "0"
