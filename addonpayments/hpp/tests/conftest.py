# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import codecs
import pytest

from addonpayments.hpp.card_storage.requests import CardStorageRequest
from addonpayments.hpp.payment.requests import PaymentRequest
from addonpayments.hpp.tests.utils import get_sample_path, only_mandatory_hpp_request, hpp_request_storage_enabled
from addonpayments.hpp.utils import JsonUtils


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
