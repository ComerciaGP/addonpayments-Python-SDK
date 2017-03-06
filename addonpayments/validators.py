# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from addonpayments.utils import ValidateUtils as Validate


class RequestValidator(object):
    """
    Attrs validator for fields used in requests objects.
    A request validator is simply a callable that takes three arguments:
        * The instance that’s being validate
        * The attribute that it’s validating, and finally
        * The value that is passed for it.
    If the validations of the fields fail, the ValueError exception is throw
    """

    @staticmethod
    def merchant_id(instance, attribute, value):
        """
        Validator for merchant id:
            * Type: Mandatory
            * Format: a-zA-Z0-9
            * Length: 1-50
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 1, 50)
        Validate.validate_regex(attribute.name, value, r'^[a-zA-Z0-9]+$', 'alphanumeric')

    @staticmethod
    def timestamp(instance, attribute, value):
        """
        Validator for timestamp:
            * Type: Mandatory (auto-generated)
            * Format: 0-9
            * Length: 14
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length(attribute.name, value, 14)
        Validate.validate_regex(attribute.name, value, r'^[0-9]+$', 'numeric')

    @staticmethod
    def account(instance, attribute, value):
        """
        Validator for account:
            * Type: Optional
            * Format: a-zA-Z0-9
            * Length: 0-30
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 30)
        Validate.validate_regex(attribute.name, value, r'^[a-zA-Z0-9]*$', 'alphanumeric')

    @staticmethod
    def order_id(instance, attribute, value):
        """
        Validator for timestamp:
            * Type: Mandatory (auto-generated)
            * Format: a-zA-Z0-9-_
            * Length: 1-40
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 1, 40)
        Validate.validate_regex(attribute.name, value, r'^[a-zA-Z0-9\-\_]+$', 'alphanumeric and -_')

    @staticmethod
    def sha1hash(instance, attribute, value):
        """
        Validator for sha1hash:
            * Type: Mandatory (auto-generated)
            * Format: a-f0-9
            * Length: 40
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length(attribute.name, value, 40)
        Validate.validate_regex(
            attribute.name, value, r'^[a-f0-9]*$', 'numeric and a-f characters'
        )

    @staticmethod
    def amount(instance, attribute, value):
        """
        Validator for amount attribute:
            * Type: Mandatory
            * Format: 0-9
            * Length: 1-11
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 1, 11)
        Validate.validate_regex(attribute.name, value, r'^[0-9]+$', 'numeric')

    @staticmethod
    def currency(instance, attribute, value):
        """
        Validator for currency attribute:
            * Type: Mandatory
            * Format: A-Z
            * Length: 3
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)
        Validate.validate_length(attribute.name, value, 3)
        Validate.validate_regex(attribute.name, value, r'^[A-Z]+$', 'uppercase alphanumeric')

    @staticmethod
    def flag(instance, attribute, value):
        """
        Validator for flag attributes, boolean but in XML are represented with '0' or '1'
            * Type: Optional
            * Format: True, False, 1, 0, '1', '0'
        :param instance: object
        :param attribute:
        :param value:
        """
        if value not in [True, False, 1, 0, '1', '0']:
            raise ValueError("{} must only True, False, 1, 0, '1' or '0'".format(attribute.name))
