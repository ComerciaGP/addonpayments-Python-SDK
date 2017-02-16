# -*- encoding: utf-8 -*-

import re

from utils import GenerationUtils


class TestGenerationUtils:
    def test_generate_hash(self):
        """
        Test Hash generation success case.
        """
        test_string = "20120926112654.thestore.ORD453-11.00.Successful.3737468273643.79347"
        secret = "mysecret"
        expected_result = "368df010076481d47a21e777871012b62b976339"
        result = GenerationUtils.generate_hash(test_string, secret)
        assert expected_result == result

    def test_generate_timestamp(self):
        """
        Test timestamp generation. Hard to test this in a meaningful way. Checking length and valid characters.
        """
        result = GenerationUtils().generate_timestamp()
        match = re.match(r'([0-9]{14})', result)
        assert match

    def test_generate_order_id(self):
        """
        Test order Id generation. Hard to test this in a meaningful way. Checking length and valid characters.
        """
        result = GenerationUtils().generate_order_id()
        match = re.match(r'[A-Za-z0-9-_]{32}', result)
        assert match
