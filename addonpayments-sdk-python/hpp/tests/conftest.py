# -*- encoding: utf-8 -*-

import pytest

from hpp.card_storage.requests import CardStorageRequest
from hpp.payment.requests import PaymentRequest
from hpp.tests.utils import sample_path, only_mandatory_hpp_request, hpp_request_storage_enabled
from hpp.utils import JsonUtils

CHARSET = "utf-8"
HPP_PAYMENT_REQUEST_VALID_JSON_PATH = "samples/hpp_payment_request.json"
HPP_PAYMENT_REQUEST_SUPPLEMENTARY_JSON_PATH = "samples/hpp_payment_request_supplementary_data.json"
HPP_PAYMENT_REQUEST_ENCODED_JSON_PATH = "samples/hpp_payment_request_encoded.json"
HPP_CARD_STORAGE_REQUEST_VALID_JSON_PATH = "samples/hpp_card_storage_request.json"
HPP_CARD_STORAGE_REQUEST_SUPPLEMENTARY_JSON_PATH = "samples/hpp_card_storage_request_supplementary_data.json"
HPP_CARD_STORAGE_REQUEST_ENCODED_JSON_PATH = "samples/hpp_card_storage_request_encoded.json"


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
    with open(sample_path(HPP_PAYMENT_REQUEST_VALID_JSON_PATH)) as data_file:
        yield JsonUtils.from_json_hpp_request(data_file, CHARSET, False)


@pytest.fixture()
def json_hpp_payment_request_supplementary_data():
    with open(sample_path(HPP_PAYMENT_REQUEST_SUPPLEMENTARY_JSON_PATH)) as data_file:
        yield JsonUtils.from_json_hpp_request(data_file, CHARSET, False)


@pytest.fixture()
def json_hpp_payment_request_encoded():
    with open(sample_path(HPP_PAYMENT_REQUEST_ENCODED_JSON_PATH)) as data_file:
        yield JsonUtils.from_json_hpp_request(data_file, CHARSET, True)


@pytest.fixture()
def json_hpp_card_storage_request_valid():
    with open(sample_path(HPP_CARD_STORAGE_REQUEST_VALID_JSON_PATH)) as data_file:
        yield JsonUtils.from_json_hpp_request(data_file, CHARSET, False)


@pytest.fixture()
def json_hpp_card_storage_request_supplementary_data():
    with open(sample_path(HPP_CARD_STORAGE_REQUEST_SUPPLEMENTARY_JSON_PATH)) as data_file:
        yield JsonUtils.from_json_hpp_request(data_file, CHARSET, False)


@pytest.fixture()
def json_hpp_card_storage_request_encoded():
    with open(sample_path(HPP_CARD_STORAGE_REQUEST_ENCODED_JSON_PATH)) as data_file:
        yield JsonUtils.from_json_hpp_request(data_file, CHARSET, True)
