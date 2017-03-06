# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import attr
from attr import ib as Field

from addonpayments.api.mixins import FieldsCommentMixin, XmlMixin, FieldsAmountMixin
from addonpayments.api.validators import (FieldsValidator, CardValidator, CvnValidator, AddressValidator,
                                          PhoneValidator, PayerValidator, DccValidator, RecurringValidator,
                                          MpiValidator)


@attr.s
class Cvn(XmlMixin):
    """
    Class representing the card verification details.
    """
    number = Field(default='', validator=CvnValidator.number)
    presind = Field(default='', convert=str, validator=CvnValidator.presind)


@attr.s
class CardRef(XmlMixin):
    """
    Class represents the card reference and payer reference
    """
    # Mandatory fields
    ref = Field(default='', validator=FieldsValidator.ref)
    payerref = Field(default='', validator=FieldsValidator.ref)
    xml_root_tag = 'card'


@attr.s
class Card(XmlMixin):
    """
    Class represents the card
    """
    # Mandatory fields
    number = Field(validator=CardValidator.number)
    expdate = Field(validator=CardValidator.expdate)
    chname = Field(validator=CardValidator.chname)
    type = Field(validator=CardValidator.type)


@attr.s
class CardWithCvn(Card):
    """
    Class represents the card with Cvn
    """
    cvn = Field(default=None, validator=attr.validators.instance_of(Cvn))
    object_fields = ['cvn']
    xml_root_tag = 'card'


@attr.s
class CardWithRef(CardRef, Card):
    """
    Class represents the card with CardRef
    """
    xml_root_tag = 'card'


@attr.s
class PaymentData(XmlMixin):
    """
    Class representing the payment data (cvn)
    """
    cvn_number = Field(default='', validator=CvnValidator.number)

    def normalize_xml(self):
        return {self.__class__.__name__.lower(): {'cvn': {'number': self.cvn_number}}}


@attr.s
class Address(XmlMixin):
    """
    Class representing the address of the customer
    """
    line1 = Field(default='', validator=AddressValidator.string_fifty)
    line2 = Field(default='', validator=AddressValidator.string_fifty)
    line3 = Field(default='', validator=AddressValidator.string_fifty)
    city = Field(default='', validator=AddressValidator.string_fifty)
    county = Field(default='', validator=AddressValidator.string_fifty)
    country = Field(default='', validator=AddressValidator.string_fifty)
    code = Field(default='', validator=AddressValidator.code)
    postcode = Field(default='', validator=AddressValidator.postcode)

    xml_grouped_fields = [('country', 'code')]


@attr.s
class PhoneNumbers(XmlMixin):
    """
    Class representing the phone number of the customer
    """
    home = Field(default='', validator=PhoneValidator.string_fifty)
    work = Field(default='', validator=PhoneValidator.string_twenty)
    fax = Field(default='', validator=PhoneValidator.string_twenty)
    mobile = Field(default='', validator=PhoneValidator.string_twenty)


@attr.s
class Payer(FieldsCommentMixin, XmlMixin):
    """
    Class representing Payer information to be passed to API
    """
    ref = Field(default='', validator=FieldsValidator.ref)
    type = Field(default='', validator=PayerValidator.type)
    title = Field(default='', validator=PayerValidator.title)
    firstname = Field(default='', validator=PayerValidator.firstname)
    surname = Field(default='', validator=PayerValidator.surname)
    company = Field(default='', validator=PayerValidator.surname)
    email = Field(default='', validator=PayerValidator.email)
    address = Field(default=None, validator=attr.validators.optional(attr.validators.instance_of(Address)))
    phonenumbers = Field(default=None, validator=attr.validators.optional(attr.validators.instance_of(PhoneNumbers)))

    object_fields = ['address', 'phonenumbers']
    xml_root_attributes = ['ref', 'type']


@attr.s
class DccInfo(XmlMixin):
    """
    Class representing the DCC information
    """
    ccp = Field(default='', validator=DccValidator.ccp)
    type = Field(convert=str, default='', validator=DccValidator.type)


@attr.s
class DccInfoWithRateType(DccInfo):
    """
    Class representing the DCC information with rate type
    """
    ratetype = Field(default='', validator=DccValidator.ratetype)
    xml_root_tag = 'dccinfo'


@attr.s
class DccInfoWithAmount(FieldsAmountMixin, DccInfo):
    """
    Class representing the DCC information with rate type and amount (amount, currency)
    """
    ratetype = Field(default='', validator=DccValidator.ratetype)
    rate = Field(default='', validator=DccValidator.rate)
    xml_root_tag = 'dccinfo'


@attr.s
class Recurring(XmlMixin):
    """
    Class representing the recurring payments
    """
    type = Field(default=None, validator=RecurringValidator.type)
    sequence = Field(default=None, validator=RecurringValidator.sequence)

    xml_root_attributes = ['type', 'sequence']


@attr.s
class Mpi(XmlMixin):
    """
    Class representing the mpi payments
    """
    cavv = Field(default='', validator=MpiValidator.cavv)
    xid = Field(default='', validator=MpiValidator.xid)
    eci = Field(convert=str, default='', validator=MpiValidator.eci)
