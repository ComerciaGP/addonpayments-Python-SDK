# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import six

from addonpayments.mixins import HashMixin


class SdkResponse(HashMixin):
    """
    Class representing the SDK response. This class is valid for HPP and API

    You can consult the specific documentation of all HPP and API response fields on the website
    https://desarrolladores.addonpayments.com
    """

    SUCCESSFULLY_CODE = '00'

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
        return {key: value for key, value in six.iteritems(self.__dict__)}

    def hash(self, secret):
        """
        Set sha1hash
        :param secret: string
        """
        self.sha1hash = self.generate_hash(secret)

    def is_hash_valid(self, secret):
        """
        Helper method to determine if the HPP or API response security hash is valid.
        :param secret: string
        :return: bool
        """
        generated_hash = self.generate_hash(secret)
        return self.sha1hash == generated_hash
