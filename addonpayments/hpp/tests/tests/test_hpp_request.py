# -*- encoding: utf-8 -*-


class TestHppRequest:
    secret = "mysecret"

    def test_hash(self, valid_hpp_request):
        """
        Test hash HppResponse success case.
        :param valid_hpp_request: PaymentRequest
        """
        expected_hash = 'c721e6b12ef61d764b840e769b57f559b09963ef'
        valid_hpp_request.hash(self.secret)
        assert valid_hpp_request.sha1hash == expected_hash

    def test_hash_storage_enabled(self, valid_hpp_request_storage_enabled):
        """
        Test hash HppResponse with card storage enabled success case.
        :param valid_hpp_request_storage_enabled: CardStorageRequest
        """
        expected_hash = '7aafc6dcbf83bf3cb8519d90ecd623974fd06cf3'
        valid_hpp_request_storage_enabled.hash(self.secret)
        assert valid_hpp_request_storage_enabled.sha1hash == expected_hash
