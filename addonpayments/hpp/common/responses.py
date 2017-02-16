# -*- encoding: utf-8 -*-

from addonpayments.utils import GenerationUtils


class HppResponse(object):
    """
    Class representing the HPP response.

    You can consult the specific documentation of all HPP response fields on the website
    https://desarrolladores.addonpayments.com
    """

    def __init__(self, **kwargs):
        """
        Store the recieved data response from the tpv into the class
        :param kwargs: dictionary
        """
        # Define sha1 hash to set after
        self.sha1hash = None

        # Set all fields
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def to_dict(self):
        """
        return the data response as a dictionary
        :return: dict
        """
        return {key: value for key, value in self.__dict__.items()}

    def hash(self, secret):
        """
        Creates the security hash from a number of fields and the shared secret.
        :param secret: string
        """
        self.sha1hash = self.generate_hash(secret)

    def generate_hash(self, secret):
        """
        Creates the security hash from a number of fields and the shared secret.
        :param secret: string
        :return: string
        """
        fields_for_hash = ['timestamp', 'merchant_id', 'order_id', 'result', 'message', 'pasref', 'authcode']
        str_hash = '.'.join([str(getattr(self, field)) for field in fields_for_hash])

        # Generate HASH
        gen_utl = GenerationUtils()
        return gen_utl.generate_hash(str_hash, secret)

    def is_hash_valid(self, secret):
        """
        Helper method to determine if the HPP response security hash is valid.
        :param secret: string
        :return: bool
        """
        generated_hash = self.generate_hash(secret)
        return self.sha1hash == generated_hash
