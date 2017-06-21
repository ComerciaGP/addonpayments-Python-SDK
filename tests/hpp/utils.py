# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import os

MERCHANT_ID = 'merchant'
AMOUNT = 100
CURRENCY = 'EUR'
TIMESTAMP = '20170126164000'
ORDER_ID = 'ORD123-11'
PAYER_REF = 'newpayer1'
PMT_REF = 'newcard1'


def only_mandatory_hpp_request():
    return {
        'merchant_id': MERCHANT_ID,
        'amount': AMOUNT,
        'currency': CURRENCY,
        'auto_settle_flag': False,
        'timestamp': TIMESTAMP,
        'order_id': ORDER_ID
    }


def hpp_request_storage_enabled():
    return {
        'merchant_id': MERCHANT_ID,
        'amount': AMOUNT,
        'currency': CURRENCY,
        'auto_settle_flag': False,
        'timestamp': TIMESTAMP,
        'order_id': ORDER_ID,
        'card_storage_enable': True,
        'payer_ref': PAYER_REF,
        'pmt_ref': PMT_REF
    }


def get_sample_path(sample):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), sample)
