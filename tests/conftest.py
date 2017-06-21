# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import codecs
import pytest

from decouple import config

from addonpayments.hpp.card_storage.requests import CardStorageRequest
from addonpayments.hpp.payment.requests import PaymentRequest
from addonpayments.hpp.utils import JsonUtils
from tests.hpp.utils import get_sample_path, only_mandatory_hpp_request, hpp_request_storage_enabled

from addonpayments.api.elements import (Cvn, CardWithCvn, Recurring, Mpi, DccInfoWithAmount, PaymentData, CardWithRef,
                                        CardRef, DccInfo, DccInfoWithRateType, Address, PhoneNumbers, Payer, Card)


@pytest.fixture()
def valid_hpp_request():
    data = only_mandatory_hpp_request()
    yield PaymentRequest(**data)


@pytest.fixture()
def valid_hpp_request_storage_enabled():
    data = hpp_request_storage_enabled()
    yield CardStorageRequest(**data)


@pytest.fixture()
def json_hpp_payment_request_valid():
    path = get_sample_path('samples/hpp_payment_request.json')
    with codecs.open(path, 'r', encoding='utf-8') as data_file:
        yield JsonUtils.from_json_hpp_request(data_file.read(), 'utf-8', False)


@pytest.fixture()
def json_hpp_payment_request_supplementary_data():
    path = get_sample_path('samples/hpp_payment_request_supplementary_data.json')
    with codecs.open(path, 'r', encoding='utf-8') as data_file:
        yield JsonUtils.from_json_hpp_request(data_file.read(), 'utf-8', False)


@pytest.fixture()
def json_hpp_payment_request_encoded():
    path = get_sample_path('samples/hpp_payment_request_encoded.json')
    with codecs.open(path, 'r', encoding='utf-8') as data_file:
        yield JsonUtils.from_json_hpp_request(data_file.read(), 'utf-8', True)


@pytest.fixture()
def json_hpp_card_storage_request_valid():
    path = get_sample_path('samples/hpp_card_storage_request.json')
    with codecs.open(path, 'r', encoding='utf-8') as data_file:
        yield JsonUtils.from_json_hpp_request(data_file.read(), 'utf-8', False)


@pytest.fixture()
def json_hpp_card_storage_request_supp_data():
    path = get_sample_path('samples/hpp_card_storage_request_supplementary_data.json')
    with codecs.open(path, 'r', encoding='utf-8') as data_file:
        yield JsonUtils.from_json_hpp_request(data_file.read(), 'utf-8', False)


@pytest.fixture()
def json_hpp_card_storage_request_encoded():
    path = get_sample_path('samples/hpp_card_storage_request_encoded.json')
    with codecs.open(path, 'r', encoding='utf-8') as data_file:
        yield JsonUtils.from_json_hpp_request(data_file.read(), 'utf-8', True)


###


class BaseTest(object):
    """
    This class defines the static variables used in all tests
    """
    merchant_id = config('MERCHANT_ID', default='yourmerchantid')
    secret = config('SHARED_SECRET', default='yoursecretkey')
    payer_ref = 'ref-payer-test'
    card_ref = 'ref-card-test'


@pytest.fixture()
def valid_card():
    card = Card(type='VISA', number='4263970000005262', expdate='1220', chname='card owner')
    yield card


@pytest.fixture()
def valid_card_with_cvn():
    cvn = Cvn(number='123', presind=1)
    card = CardWithCvn(type='VISA', number='4263970000005262', expdate='1220', cvn=cvn, chname='card owner')
    yield card


@pytest.fixture()
def valid_card_with_ref():
    yield CardWithRef(
        type='VISA',
        number='4263970000005262',
        expdate='1220',
        chname='new card owner',
        ref=BaseTest().card_ref,
        payerref=BaseTest().payer_ref
    )


@pytest.fixture()
def declined_card():
    card = Card(type='VISA', number='4000120000001154', expdate='1220', chname='card owner')
    yield card


@pytest.fixture()
def declined_card_with_cvn():
    cvn = Cvn(number='123', presind=1)
    card = CardWithCvn(type='VISA', number='4000120000001154', expdate='1220', cvn=cvn, chname='card owner')
    yield card


@pytest.fixture()
def declined_card_with_ref():
    yield CardWithRef(
        type='VISA',
        number='4000120000001154',
        expdate='1220',
        chname='new card owner',
        ref=BaseTest().card_ref,
        payerref=BaseTest().payer_ref
    )


@pytest.fixture()
def card_ref():
    yield CardRef(ref=BaseTest().card_ref, payerref=BaseTest().payer_ref)


@pytest.fixture()
def recurring():
    yield Recurring(type='fixed', sequence='first')


@pytest.fixture()
def mpi():
    yield Mpi(cavv='AAACBllleHchZTBWIGV4AAAAAAA', xid='crqAeMwkEL9r4POdxpByWJ1', eci=5)


@pytest.fixture()
def dcc_info():
    yield DccInfo(ccp='ccp', type=1)


@pytest.fixture()
def dcc_info_with_amount():
    yield DccInfoWithAmount(ccp='ccp', type=1, ratetype='S', rate='1.6728', amount=100, currency='EUR')


@pytest.fixture()
def dcc_info_with_rate_type():
    yield DccInfoWithRateType(ccp='ccp', type=1, ratetype='S')


@pytest.fixture()
def payment_data():
    yield PaymentData('123')


@pytest.fixture()
def payer():
    address = Address(
        line1='Flat 123',
        line2='House 456',
        line3='The Cul-De-Sac',
        city='Palma',
        county='Balearic islands',
        postcode='07121',
        code='ES',
        country='Spain'
    )
    phone_numbers = PhoneNumbers(
        home='+34312345678',
        work='+3431987654321',
        fax='+124546871258',
        mobile='+25544778544'
    )
    yield Payer(
        type='Retail',
        ref=BaseTest().payer_ref,
        title='Mr',
        firstname='James',
        surname='Mason',
        company='Addon Payments',
        address=address,
        phonenumbers=phone_numbers,
        email='text@example.com',
        comments=['comment one', 'comment two']
    )
