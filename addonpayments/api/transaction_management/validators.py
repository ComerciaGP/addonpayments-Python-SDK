# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from addonpayments.utils import ValidateUtils as Validate


class TransactionManagementValidator(object):
    """
    Attrs validator for fields used in transaction manager requests.
    A transaction management validator is simply a callable that takes three arguments:
        * The instance that’s being validate
        * The attribute that it’s validating, and finally
        * The value that is passed for it.
    If the validations of the fields fail, the ValueError exception is throw
    """

    @staticmethod
    def pasref(instance, attribute, value):
        """
        Validator for pasref attribute:
            * Type: Mandatory
            * Format: a-zA-Z0-9
            * Length: 1-50
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 1, 50)
        Validate.validate_regex(attribute.name, value, r'^[a-zA-Z0-9]+$', 'alphanumeric')

    @staticmethod
    def authcode(instance, attribute, value):
        """
        Validator for authcode attribute:
            * Type: Mandatory
            * Format: a-zA-Z0-9
            * Length: 1-10
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 1, 10)
        Validate.validate_regex(attribute.name, value, r'^[a-zA-Z0-9]+$', 'alphanumeric')
