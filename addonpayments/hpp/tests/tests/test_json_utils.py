# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json

from addonpayments.hpp.card_storage.requests import CardStorageRequest
from addonpayments.hpp.payment.requests import PaymentRequest
from addonpayments.hpp.utils import JsonUtils


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

    def test_to_json_hpp_payment_request(self, json_hpp_payment_request_valid):
        """
        Test PaymentRequest generated to JSON
        :param json_hpp_payment_request_valid: PaymentRequest
        """
        assert isinstance(json_hpp_payment_request_valid, PaymentRequest)

        json_base64_request = json.loads(JsonUtils.to_json(json_hpp_payment_request_valid, 'utf-8', True))
        assert isinstance(json_base64_request, dict)
        assert json_base64_request.get('TIMESTAMP') == 'MjA5OTAxMDExMjAwMDA='
        assert json_base64_request.get('ORDER_ID') == 'T3JkZXJJRA=='
        assert json_base64_request.get('VAR_REF') == 'VmFyaWFibGVSZWY='
        assert json_base64_request.get('MERCHANT_ID') == 'TWVyY2hhbnRJRA=='
        assert json_base64_request.get('AMOUNT') == 'MTAw'
        assert json_base64_request.get('ACCOUNT') == 'bXlBY2NvdW50'
        assert json_base64_request.get('PROD_ID') == 'UHJvZHVjdElE'
        assert json_base64_request.get('SHA1HASH') == 'NWQ4ZjA1YWJkNjE4ZTUwZGI0ODYxYTYxY2M5NDAxMTI3ODY0NzRjZg=='
        comment = 'YS16IEEtWiAwLTkgJyAiLCArIOKAnOKAnSAuXyAtICYgXCAvIEAgISA/ICUgKCApKiA6IMKjICQgJiDigqwgIyBbIF0gfC' \
                  'A9IDvDgMOBw4LDg8OEw4XDhsOHw4jDicOKw4vDjMONw47Dj8OQw5HDksOTw5TDlcOWw5fDmMOZw5rDm8Ocw53DnsOfw6DD' \
                  'ocOiw6PDpMOlw6bDp8Oow6nDqsOrw6zDrcOuw6/DsMOxw7LDs8O0w7XDtsO3w7jCpMO5w7rDu8O8w73DvsO/xZLFvcWhxZ' \
                  'PFvsW4wqU='
        assert json_base64_request.get('COMMENT1') == comment
        assert json_base64_request.get('CURRENCY') == 'RVVS'
        assert json_base64_request.get('SHIPPING_CODE') == 'NTZ8OTg3'
        assert json_base64_request.get('CARD_PAYMENT_BUTTON') == 'U3VibWl0IFBheW1lbnQ='
        assert json_base64_request.get('HPP_LANG') == 'RU4='
        assert json_base64_request.get('AUTO_SETTLE_FLAG') == 'MQ=='
        assert json_base64_request.get('SHIPPING_CO') == 'SVJFTEFORA=='
        assert json_base64_request.get('BILLING_CO') == 'SVJFTEFORA=='
        assert json_base64_request.get('COMMENT2') == 'Q29tbWVudCBUd28='
        assert json_base64_request.get('BILLING_CODE') == 'MTIzfDU2'
        assert json_base64_request.get('CUST_NUM') == 'MTIzNDU2'

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
        assert json_hpp_payment_request_supplementary_data.supplementary_data['SUPPLEMENTARY_1'] == "Supp1"
        assert json_hpp_payment_request_supplementary_data.supplementary_data['SUPPLEMENTARY_2'] == "Supp2"
        assert json_hpp_payment_request_supplementary_data.supplementary_data['SUPPLEMENTARY_3'] == "Supp3"
        assert json_hpp_payment_request_supplementary_data.supplementary_data['SUPPLEMENTARY_4'] == "Supp4"

    def test_to_json_hpp_payment_request_supplementary_data(self, json_hpp_payment_request_supplementary_data):
        """
        Test PaymentRequest with supplementary data () generated to JSON
        :param json_hpp_payment_request_supplementary_data: PaymentRequest
        """
        assert isinstance(json_hpp_payment_request_supplementary_data, PaymentRequest)

        json_base64_request = json.loads(JsonUtils.to_json(json_hpp_payment_request_supplementary_data, 'utf-8', True))
        assert isinstance(json_base64_request, dict)
        assert json_base64_request.get('SHIPPING_CO') == 'SVJFTEFORA=='
        assert json_base64_request.get('HPP_LANG') == 'RU4='
        assert json_base64_request.get('COMMENT2') == 'Q29tbWVudCBUd28='
        assert json_base64_request.get('ORDER_ID') == 'T3JkZXJJRA=='
        assert json_base64_request.get('SHA1HASH') == 'NWQ4ZjA1YWJkNjE4ZTUwZGI0ODYxYTYxY2M5NDAxMTI3ODY0NzRjZg=='
        assert json_base64_request.get('AUTO_SETTLE_FLAG') == 'MQ=='
        comment = 'YS16IEEtWiAwLTkgJyAiLCArIOKAnOKAnSAuXyAtICYgXCAvIEAgISA/ICUgKCApKiA6IMKjICQgJiDigqwgIyBbIF0gfCA9'
        assert json_base64_request.get('COMMENT1') == comment
        assert json_base64_request.get('VAR_REF') == 'VmFyaWFibGVSZWY='
        assert json_base64_request.get('TIMESTAMP') == 'MjA5OTAxMDExMjAwMDA='
        assert json_base64_request.get('ACCOUNT') == 'bXlBY2NvdW50'
        assert json_base64_request.get('AMOUNT') == 'MTAw'
        assert json_base64_request.get('SHIPPING_CODE') == 'NTZ8OTg3'
        assert json_base64_request.get('BILLING_CO') == 'SVJFTEFORA=='
        assert json_base64_request.get('CUST_NUM') == 'MTIzNDU2'
        assert json_base64_request.get('CURRENCY') == 'RVVS'
        assert json_base64_request.get('BILLING_CODE') == 'MTIzfDU2'
        assert json_base64_request.get('PROD_ID') == 'UHJvZHVjdElE'
        assert json_base64_request.get('CARD_PAYMENT_BUTTON') == 'U3VibWl0IFBheW1lbnQ='
        assert json_base64_request.get('MERCHANT_ID') == 'TWVyY2hhbnRJRA=='
        assert json_base64_request.get('SUPPLEMENTARY_1') == 'U3VwcDE='
        assert json_base64_request.get('SUPPLEMENTARY_2') == 'U3VwcDI='
        assert json_base64_request.get('SUPPLEMENTARY_3') == 'U3VwcDM='
        assert json_base64_request.get('SUPPLEMENTARY_4') == 'U3VwcDQ='

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

    def test_to_json_hpp_card_storage_request(self, json_hpp_card_storage_request_valid):
        """
        Test PaymentRequest generated to JSON
        :param json_hpp_card_storage_request_valid: PaymentRequest
        """
        assert isinstance(json_hpp_card_storage_request_valid, CardStorageRequest)

        json_base64_request = json.loads(JsonUtils.to_json(json_hpp_card_storage_request_valid, 'utf-8', True))
        assert isinstance(json_base64_request, dict)
        assert json_base64_request.get('BILLING_CO') == 'SVJFTEFORA=='
        assert json_base64_request.get('ACCOUNT') == 'bXlBY2NvdW50'
        assert json_base64_request.get('VAR_REF') == 'VmFyaWFibGVSZWY='
        assert json_base64_request.get('SHIPPING_CO') == 'SVJFTEFORA=='
        comment = 'YS16IEEtWiAwLTkgJyAiLCArIOKAnOKAnSAuXyAtICYgXCAvIEAgISA/ICUgKCApKiA6IMKjICQgJiDigqwgIyBbIF0gfCA9I' \
                  'DvDgMOBw4LDg8OEw4XDhsOHw4jDicOKw4vDjMONw47Dj8OQw5HDksOTw5TDlcOWw5fDmMOZw5rDm8Ocw53DnsOfw6DDocOiw6' \
                  'PDpMOlw6bDp8Oow6nDqsOrw6zDrcOuw6/DsMOxw7LDs8O0w7XDtsO3w7jCpMO5w7rDu8O8w73DvsO/xZLFvcWhxZPFvsW4wqU='
        assert json_base64_request.get('COMMENT1') == comment
        assert json_base64_request.get('COMMENT2') == 'Q29tbWVudCBUd28='
        assert json_base64_request.get('CURRENCY') == 'RVVS'
        assert json_base64_request.get('PAYER_EXIST') == 'MQ=='
        assert json_base64_request.get('MERCHANT_ID') == 'TWVyY2hhbnRJRA=='
        assert json_base64_request.get('CARD_PAYMENT_BUTTON') == 'U3VibWl0IFBheW1lbnQ='
        assert json_base64_request.get('ORDER_ID') == 'T3JkZXJJRA=='
        assert json_base64_request.get('SHIPPING_CODE') == 'NTZ8OTg3'
        assert json_base64_request.get('AMOUNT') == 'MTAw'
        assert json_base64_request.get('SHA1HASH') == 'NWQ4ZjA1YWJkNjE4ZTUwZGI0ODYxYTYxY2M5NDAxMTI3ODY0NzRjZg=='
        assert json_base64_request.get('AUTO_SETTLE_FLAG') == 'MQ=='
        assert json_base64_request.get('OFFER_SAVE_CARD') == 'MQ=='
        assert json_base64_request.get('BILLING_CODE') == 'MTIzfDU2'
        assert json_base64_request.get('PROD_ID') == 'UHJvZHVjdElE'
        assert json_base64_request.get('PAYER_REF') == 'UGF5ZXJSZWY='
        assert json_base64_request.get('CARD_STORAGE_ENABLE') == 'MQ=='
        assert json_base64_request.get('TIMESTAMP') == 'MjA5OTAxMDExMjAwMDA='
        assert json_base64_request.get('CUST_NUM') == 'MTIzNDU2'
        assert json_base64_request.get('PMT_REF') == 'UGF5bWVudFJlZg=='
        assert json_base64_request.get('HPP_LANG') == 'RU4='

    def test_from_json_hpp_card_storage_request_supp_data(self, json_hpp_card_storage_request_supp_data):
        """
        Test CardStorageRequest with supplementary data () generated from JSON
        :param json_hpp_card_storage_request_supp_data: CardStorageRequest
        """
        assert isinstance(json_hpp_card_storage_request_supp_data, CardStorageRequest)
        assert json_hpp_card_storage_request_supp_data.merchant_id == "MerchantID"
        assert json_hpp_card_storage_request_supp_data.account == "myAccount"
        assert json_hpp_card_storage_request_supp_data.order_id == "OrderID"
        assert json_hpp_card_storage_request_supp_data.amount == "100"
        assert json_hpp_card_storage_request_supp_data.currency == "EUR"
        assert json_hpp_card_storage_request_supp_data.timestamp == "20990101120000"
        assert json_hpp_card_storage_request_supp_data.sha1hash == "5d8f05abd618e50db4861a61cc940112786474cf"
        assert json_hpp_card_storage_request_supp_data.auto_settle_flag == "1"
        comment1 = "a-z A-Z 0-9 ' \", + “” ._ - & \\ / @ ! ? % ( )* : £ $ & € # [ ] | ="
        assert json_hpp_card_storage_request_supp_data.comment1 == comment1
        assert json_hpp_card_storage_request_supp_data.comment2 == "Comment Two"
        assert json_hpp_card_storage_request_supp_data.shipping_code == "56|987"
        assert json_hpp_card_storage_request_supp_data.shipping_co == "IRELAND"
        assert json_hpp_card_storage_request_supp_data.billing_code == "123|56"
        assert json_hpp_card_storage_request_supp_data.billing_co == "IRELAND"
        assert json_hpp_card_storage_request_supp_data.cust_num == "123456"
        assert json_hpp_card_storage_request_supp_data.var_ref == "VariableRef"
        assert json_hpp_card_storage_request_supp_data.prod_id == "ProductID"
        assert json_hpp_card_storage_request_supp_data.hpp_lang == "EN"
        assert json_hpp_card_storage_request_supp_data.card_payment_button == "Submit Payment"
        assert json_hpp_card_storage_request_supp_data.card_storage_enable == "1"
        assert json_hpp_card_storage_request_supp_data.offer_save_card == "1"
        assert json_hpp_card_storage_request_supp_data.payer_ref == "PayerRef"
        assert json_hpp_card_storage_request_supp_data.pmt_ref == "PaymentRef"
        assert json_hpp_card_storage_request_supp_data.payer_exist == "1"
        assert isinstance(json_hpp_card_storage_request_supp_data.supplementary_data, dict)
        assert json_hpp_card_storage_request_supp_data.supplementary_data['SUPPLEMENTARY_1'] == "Supp1"
        assert json_hpp_card_storage_request_supp_data.supplementary_data['SUPPLEMENTARY_2'] == "Supp2"
        assert json_hpp_card_storage_request_supp_data.supplementary_data['SUPPLEMENTARY_3'] == "Supp3"
        assert json_hpp_card_storage_request_supp_data.supplementary_data['SUPPLEMENTARY_4'] == "Supp4"

    def test_to_json_hpp_card_storage_request_supp_data(self, json_hpp_card_storage_request_supp_data):
        """
        Test CardStorageRequest with supplementary data () generated to JSON
        :param json_hpp_card_storage_request_supp_data: CardStorageRequest
        """
        assert isinstance(json_hpp_card_storage_request_supp_data, CardStorageRequest)
        json_base64_request = json.loads(JsonUtils.to_json(json_hpp_card_storage_request_supp_data, 'utf-8', True))
        assert isinstance(json_base64_request, dict)

        assert json_base64_request.get('AUTO_SETTLE_FLAG') == 'MQ=='
        assert json_base64_request.get('CURRENCY') == 'RVVS'
        assert json_base64_request.get('PROD_ID') == 'UHJvZHVjdElE'
        assert json_base64_request.get('SHIPPING_CO') == 'SVJFTEFORA=='
        assert json_base64_request.get('MERCHANT_ID') == 'TWVyY2hhbnRJRA=='
        assert json_base64_request.get('ORDER_ID') == 'T3JkZXJJRA=='
        assert json_base64_request.get('PAYER_EXIST') == 'MQ=='
        assert json_base64_request.get('PMT_REF') == 'UGF5bWVudFJlZg=='
        assert json_base64_request.get('AMOUNT') == 'MTAw'
        assert json_base64_request.get('CUST_NUM') == 'MTIzNDU2'
        assert json_base64_request.get('COMMENT2') == 'Q29tbWVudCBUd28='
        assert json_base64_request.get('OFFER_SAVE_CARD') == 'MQ=='
        assert json_base64_request.get('SHA1HASH') == 'NWQ4ZjA1YWJkNjE4ZTUwZGI0ODYxYTYxY2M5NDAxMTI3ODY0NzRjZg=='
        assert json_base64_request.get('SHIPPING_CODE') == 'NTZ8OTg3'
        assert json_base64_request.get('CARD_PAYMENT_BUTTON') == 'U3VibWl0IFBheW1lbnQ='
        assert json_base64_request.get('HPP_LANG') == 'RU4='
        assert json_base64_request.get('PAYER_REF') == 'UGF5ZXJSZWY='
        assert json_base64_request.get('ACCOUNT') == 'bXlBY2NvdW50'
        comment = 'YS16IEEtWiAwLTkgJyAiLCArIOKAnOKAnSAuXyAtICYgXCAvIEAgISA/ICUgKCApKiA6IMKjICQgJiDigqwgIyBbIF0gfCA9'
        assert json_base64_request.get('COMMENT1') == comment
        assert json_base64_request.get('VAR_REF') == 'VmFyaWFibGVSZWY='
        assert json_base64_request.get('BILLING_CODE') == 'MTIzfDU2'
        assert json_base64_request.get('CARD_STORAGE_ENABLE') == 'MQ=='
        assert json_base64_request.get('TIMESTAMP') == 'MjA5OTAxMDExMjAwMDA='
        assert json_base64_request.get('BILLING_CO') == 'SVJFTEFORA=='
        assert json_base64_request.get('SUPPLEMENTARY_1') == 'U3VwcDE='
        assert json_base64_request.get('SUPPLEMENTARY_2') == 'U3VwcDI='
        assert json_base64_request.get('SUPPLEMENTARY_3') == 'U3VwcDM='
        assert json_base64_request.get('SUPPLEMENTARY_4') == 'U3VwcDQ='

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
