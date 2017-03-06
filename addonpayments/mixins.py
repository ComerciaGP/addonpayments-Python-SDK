# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import six

from addonpayments.utils import GenerationUtils


class HashMixin(object):
    """
    This mixin generate hash for every request
    Attributes:
        hash_fields     Hash a string made up of the request values
    """
    hash_fields = []

    def get_hash_values(self):
        """
        This method return a list values to generate hash
        :return: list
        """
        hash_values = []
        for f in self.hash_fields:
            try:
                if getattr(self, f) is None:
                    hash_values.append('')
                else:
                    hash_values.append(getattr(self, f))
            except AttributeError:
                hash_values.append('')
        return hash_values

    def generate_hash(self, secret):
        """
        Generate the security hash from a number of fields and the shared secret.
        :rtype: object
        """
        # Generate string to hash from fields values list
        str_hash = '.'.join(self.get_hash_values())
        # Generate HASH
        gen_utl = GenerationUtils()
        return gen_utl.generate_hash(str_hash, secret)


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
        return {
            key: self.set_flags(key, value) for key, value in six.iteritems(self.__dict__) if self.set_flags(key, value)
        }
