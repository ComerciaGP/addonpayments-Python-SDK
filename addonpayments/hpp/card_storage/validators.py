# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from addonpayments.utils import ValidateUtils as Validate


class CardStorageValidator(object):
    """
    Attrs validator for fields used in HPP card storage request object.
    A HPP vard storage validator is simply a callable that takes three arguments:
        * The instance that’s being validate
        * The attribute that it’s validating, and finally
        * The value that is passed for it.
    If the validations of the fields fail, the ValueError exception is throw
    """

    @staticmethod
    def hpp_select_stored_card(instance, attribute, value):
        """
        Validator for pmt_ref attribute:
            * Type: Mandatory
            * Format: A-Za-z0-9_-\
            * Length: 0-30
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 1, 50)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[A-Za-z0-9\_\-\\ ]*$',
            'alphanumeric and _-\\ and spaces'
        )

    @staticmethod
    def payer_exist(instance, attribute, value):
        """
        Validator for flag payer_exist, boolean but in XML are represented with '0' or '1'
            * Type: Mandatory
            * Format: True, False, 1, 0, '1', '0'
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        if instance.hpp_select_stored_card:
            if value not in [True, 1, '1']:
                raise ValueError("{} must only True, 1 or '1'".format(attribute.name))
        else:
            if value not in [False, 0, '0']:
                raise ValueError("{} must only False, 0, or '0'".format(attribute.name))

    @staticmethod
    def recurring_type(instance, attribute, value):
        """
        Validator for recurring_type attribute
            * Type: Optional
            * Format: 'fixed', 'variable'
        :param instance: object
        :param attribute:
        :param value:
        """
        if value not in ['fixed', 'variable']:
            raise ValueError("{} must only 'fixed' or 'variable'".format(attribute.name))

    @staticmethod
    def recurring_sequence(instance, attribute, value):
        """
        Validator for recurring_sequence attribute
            * Type: Optional
            * Format: 'first', 'subsequent', 'last'
        :param instance: object
        :param attribute:
        :param value:
        """
        if value not in ['first', 'subsequent', 'last']:
            raise ValueError("{} must only 'first', 'subsequent' or 'last".format(attribute.name))
