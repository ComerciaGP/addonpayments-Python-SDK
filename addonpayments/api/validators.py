# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from addonpayments.utils import ValidateUtils as Validate


class FieldsValidator(object):
    """
    Attrs validator for fields used in many requests of the API.
    A API validator is simply a callable that takes three arguments:
        * The instance that’s being validate
        * The attribute that it’s validating, and finally
        * The value that is passed for it.
    If the validations of the fields fail, the ValueError exception is throw
    """

    @staticmethod
    def comment(name, value):
        """
        Validator for comment attribute:
            * Type:     Optional
            * Format:   a-zA-Z0-9 \'\",\+“”.\_\-&\\/@!?%()\*\:£$&€#\[\]|=\;
                        ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷ø¤ùúûüýþÿŒŽšœžŸ¥
            * Length:   0-255
        :param name: string
        :param value:
        """
        if not value:
            return
        Validate.validate_str(name, value)
        Validate.validate_length_range(name, value, 0, 255)
        Validate.validate_regex(
            name,
            value,
            r'^[a-zA-Z0-9 \'\",\+“”.\_\-&\\/@!?%()\*\:£$&€#\[\]|=\;'
            r'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷ø¤ùúûüýþÿŒŽšœžŸ¥]*$',
            'alphanumeric and \'",+“”.-_&\\/@!?%()*:£$&€#[]|='
            'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷ø¤ùúûüýþÿŒŽšœžŸ¥ and spaces'
        )

    @staticmethod
    def comments(instance, attribute, value):
        """
        Validator for comments list. For each comment calls comment validator
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_list(attribute.name, value)
        for key, comment in enumerate(value):
            FieldsValidator.comment("{}{}".format(attribute.name, key), comment)

    @staticmethod
    def channel(instance, attribute, value):
        """
        Validator for channel attribute:
            * Type: Optional
            * Format: MOTO, ECOM
            * Length: 4
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        if value not in ['MOTO', 'ECOM']:
            raise ValueError("{} must only 'MOTO' or 'ECOM'".format(attribute.name))

    @staticmethod
    def ref(instance, attribute, value):
        """
        Validator for ref attribute:
            * Type: Mandatory
            * Format: a-zA-Z0-9-_
            * Length: 1-50
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
            r'^[a-zA-Z0-9\-\_\.]+$',
            'alphanumeric and -_.'
        )


class CardValidator(object):
    """
    Attrs validator for fields used in card objects.
    """

    @staticmethod
    def number(instance, attribute, value):
        """
        Validator for card attribute:
            * Type: Mandatory
            * Format: 0-9
            * Length: 12-19
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 12, 19)
        Validate.validate_regex(attribute.name, value, r'^[0-9]+$', 'numeric')

    @staticmethod
    def expdate(instance, attribute, value):
        """
        Validator for expdata (expiration date) attribute:
            * Type: Mandatory
            * Format: 0-9
            * Length: 4
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)
        Validate.validate_length(attribute.name, value, 4)
        Validate.validate_regex(attribute.name, value, r'^[0-9]+$', 'numeric')

    @staticmethod
    def chname(instance, attribute, value):
        """
        Validator for chname (card holder name) attribute:
            * Type: Mandatory
            * Format: a-zA-Z0-9-_
            * Length: 1-100
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 1, 100)
        Validate.validate_regex(attribute.name, value, r'^[a-zA-Z0-9 \-\_]+$', 'alphanumeric and \-_ and spaces')

    @staticmethod
    def type(instance, attribute, value):
        """
        Validator for type (VISA, MC, ...) attribute:
            * Type: Mandatory
            * Format: A-Z
            * Length: 1-15
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 1, 15)
        Validate.validate_regex(attribute.name, value, r'^[A-Z]+$', 'uppercase alphanumeric')


class CvnValidator(object):
    """
    Attrs validator for fields used in cvn of card object.
    """

    @staticmethod
    def number(instance, attribute, value):
        """
        Validator for number attribute:
            * Type: Optional
            * Format: 0-9
            * Length: 3-4
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 3, 4)
        Validate.validate_regex(attribute.name, value, r'^[0-9]+$', 'numeric')

    @staticmethod
    def presind(instance, attribute, value):
        """
        Validator for presind (presence indicator) attribute:
            * Type: Optional
            * Format: 1-4
            * Length: 1
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_length(attribute.name, value, 1)
        Validate.validate_regex(attribute.name, value, r'^[1-4]+$', 'numeric')


class AddressValidator(object):
    """
    Attrs validator for fields used in address (payer) object.
    """

    @staticmethod
    def string_fifty(instance, attribute, value):
        """
        Validator for attributes that have a length of 50 characters:
            * Type: Optional
            * Format: a-zA-Z0-9 -_'".,+
            * Length: 0-50
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 50)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9 \-\_\'\".,\+]*$',
            'alphanumeric and \'\".,-_+ and spaces'
        )

    @staticmethod
    def postcode(instance, attribute, value):
        """
        Validator for postcode attribute:
            * Type: Optional
            * Format: a-zA-Z0-9 -_'".,+
            * Length: 0-20
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 20)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9 \-\_\'\".,\+]*$',
            'alphanumeric and \'\".,-_+ and spaces'
        )

    @staticmethod
    def code(instance, attribute, value):
        """
        Validator for code attribute:
            * Type: Optional
            * Format: a-zA-Z
            * Length: 2
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length(attribute.name, value, 2)
        Validate.validate_regex(attribute.name, value, r'^[a-zA-Z]+$', 'alphanumeric')


class PhoneValidator(object):
    """
    Attrs validator for fields used in phone number (payer) object.
    """

    @staticmethod
    def string_fifty(instance, attribute, value):
        """
        Validator for attributes that have a length of 50 characters:
            * Type: Optional
            * Format: a-zA-Z0-9 -_'".,+()
            * Length: 1-4
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 50)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9 \-\_\'\".,\+\(\)]*$',
            'alphanumeric and \'\".,-_+() and spaces'
        )

    @staticmethod
    def string_twenty(instance, attribute, value):
        """
        Validator for attributes that have a length of 20 characters:
            * Type: Optional
            * Format: a-zA-Z0-9 -_'".,+()
            * Length: 0-20
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 20)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9 \-\_\'\".,\+\(\)]*$',
            'alphanumeric and \'\".,-_+() and spaces'
        )


class PayerValidator(object):
    """
    Attrs validator for fields used in payer object.
    """

    @staticmethod
    def type(instance, attribute, value):
        """
        Validator for type attribute:
            * Type: Mandatory
            * Format: a-zA-Z0-9-_'"+
            * Length: 1-50
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
            r'^[a-zA-Z0-9\-\_\'\"\+]+$',
            'alphanumeric and -_'
        )

    @staticmethod
    def title(instance, attribute, value):
        """
        Validator for title attribute:
            * Type: Optional
            * Format: a-zA-Z0-9 -_'".,+
            * Length: 0-10
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 10)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9 \-\_\'\".,\+]*$',
            'alphanumeric and \'\".,-_+ and spaces'
        )

    @staticmethod
    def firstname(instance, attribute, value):
        """
        Validator for firstanme attribute:
            * Type: Optional
            * Format: a-zA-Z0-9 -_'".,+
            * Length: 1-30
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 1, 30)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9 \-\_\'\".,\+]*$',
            'alphanumeric and \'\".,-_+ and spaces'
        )

    @staticmethod
    def surname(instance, attribute, value):
        """
        Validator for surname attribute:
            * Type: Optional
            * Format: a-zA-Z0-9 -_'".,+
            * Length: 1-50
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 1, 50)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9 \-\_\'\".,\+]*$',
            'alphanumeric and \'\".,-_+ and spaces'
        )

    @staticmethod
    def email(instance, attribute, value):
        """
        Validator for email attribute:
            * Type: Optional
            * Format: a-zA-Z0-9.@-_
            * Length: 0-50
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 50)
        Validate.validate_regex(attribute.name, value, r'^[a-zA-Z0-9\.@\-\_]*$', 'alphanumeric and .@-_')


class DccValidator(object):
    """
    Attrs validator for fields used in DCC object.
    """

    @staticmethod
    def ccp(instance, attribute, value):
        """
        Validator for ccp attribute:
            * Type: Mandatory
            * Format: a-z
            * Length: 1-20
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 1, 20)
        Validate.validate_regex(attribute.name, value, r'^[a-z]+$', 'lower alphanumeric')

    @staticmethod
    def type(instance, attribute, value):
        """
        Validator for type attribute:
            * Type: Mandatory
            * Format: 1-5
            * Length: 1
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)
        Validate.validate_length(attribute.name, value, 1)
        Validate.validate_regex(attribute.name, value, r'^[1-5]+$', 'lower alphanumeric')

    @staticmethod
    def ratetype(instance, attribute, value):
        """
        Validator for ratetype attribute:
            * Type: Mandatory
            * Format: S, R
            * Length: 1
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        if value not in ['S', 'R']:
            raise ValueError("{} must only 'S' or 'R'".format(attribute.name))

    @staticmethod
    def rate(instance, attribute, value):
        """
        Validator for rate attribute:
            * Type: Mandatory
            * Format: 0-9.
            * Length: 1-6
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 1, 6)
        Validate.validate_regex(attribute.name, value, r'^[0-9.]+$', 'numeric and .')


class RecurringValidator(object):
    """
    Attrs validator for fields used in Recurring object.
    """

    @staticmethod
    def type(instance, attribute, value):
        """
        Validator for type attribute:
            * Type: Optional
            * Format: fixed, variable
            * Length: 5-8
        :param instance: object
        :param attribute:
        :param value:
        """
        if value is None:
            return
        if value not in ['fixed', 'variable']:
            raise ValueError("{} must only 'fixed' or 'variable'".format(attribute.name))

    @staticmethod
    def sequence(instance, attribute, value):
        """
        Validator for sequence attribute:
            * Type: Optional
            * Format: first, subsequent, last
            * Length: 4-10
        :param instance: object
        :param attribute:
        :param value:
        """
        if value is None:
            return
        if value not in ['first', 'subsequent', 'last']:
            raise ValueError("{} must only 'first' or 'subsequent' or 'last'".format(attribute.name))


class MpiValidator(object):
    """
    Attrs validator for fields used in Mpi object.
    """

    @staticmethod
    def cavv(instance, attribute, value):
        """
        Validator for cavv attribute:
            * Type: Mandatory
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)

    @staticmethod
    def xid(instance, attribute, value):
        """
        Validator for xid attribute:
            * Type: Mandatory
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)

    @staticmethod
    def eci(instance, attribute, value):
        """
        Validator for eci attribute:
            * Type: Mandatory
            * Format: 0-9.
            * Length: 1
        :param instance: object
        :param attribute:
        :param value:
        """
        Validate.validate_mandatory(attribute.name, value)
        Validate.validate_str(attribute.name, value)
        Validate.validate_length(attribute.name, value, 1)
        Validate.validate_regex(attribute.name, value, r'^[0-9]+$', 'numeric')
