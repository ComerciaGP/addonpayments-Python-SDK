# -*- encoding: utf-8 -*-

import pytest
from decouple import config

from addonpayments.api.elements import (Cvn, CardWithCvn, Recurring, Mpi, DccInfoWithAmount, PaymentData, CardWithRef,
                                        CardRef, DccInfo, DccInfoWithRateType, Address, PhoneNumbers, Payer, Card)


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
