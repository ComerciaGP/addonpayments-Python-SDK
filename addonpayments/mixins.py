# -*- encoding: utf-8 -*-

import attr

from addonpayments.utils import GenerationUtils


class HashMixin(object):
    """
    This mixin generate hash for every request
    Attributes:
        hash_values     Hash a string made up of the request values
    """
    hash_values = []

    def get_hash_values(self):
        """
        This method return a list values to generate hash
        :return: list
        """
        return [getattr(self, f) for f in self.hash_values]

    def hash(self, secret):
        """
        Creates the security hash from a number of fields and the shared secret.
        :param secret: string
        """
        # Generate string to hash from fields values list
        str_hash = '.'.join(self.get_hash_values())
        # Generate HASH
        gen_utl = GenerationUtils()
        self.sha1hash = gen_utl.generate_hash(str_hash, secret)
        # Validate hash
        attr.validate(self)
        return self.sha1hash


class DictMixin(object):
    """
    This mixin parse object to dict.
    Attributes:
        flag_fields     List of fields that represents a flag field (boolean field)
        object_fields   List of fields that represents a object
    """

    flag_fields = []
    object_fields = []

    def set_flags(self, attribute, value):
        """
        Parse boolean values to string: True = '1', False = '0'
        :param attribute: string
        :param value:
        :return: string
        """
        if value is not None and attribute in self.flag_fields:
            return str(int(value))
        else:
            return value

    def to_dict(self):
        """
        Return the class attributes in a dictionary
        :return: dict
        """
        return {key: self.set_flags(key, value) for key, value in self.__dict__.items() if self.set_flags(key, value)}
