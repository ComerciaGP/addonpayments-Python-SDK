# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import attr
import six
from attr import ib as Field

from addonpayments.mixins import DictMixin
from addonpayments.validators import RequestValidator
from addonpayments.api.validators import FieldsValidator as Validator


@attr.s
class FieldsCommentMixin(object):
    """
    This mixin add comment field and necessary definition for parse to XML
    """
    comments = Field(default=[], validator=Validator.comments)
    xml_list_fields = [('comments', 'comment')]


@attr.s
class FieldsMixin(FieldsCommentMixin):
    """
    This mixin add fields used in many requests
    """
    channel = Field(default='', validator=Validator.channel)
    autosettle = Field(default=None, validator=RequestValidator.flag)


@attr.s
class FieldsAmountMixin(object):
    """
    This mixin add amount fields and necessary definition for parse to XML
    """
    currency = Field(default=None, validator=RequestValidator.currency)
    amount = Field(default='', convert=str, validator=RequestValidator.amount)
    xml_grouped_fields = [('amount', 'currency')]


class XmlMixin(DictMixin):
    """
    This Mixin is used to prepare the objects to be parsed to xml with xmltodic library.
    Attributes:
        xml_root_tag            Name of the XML root tag. If it is an object of the type element by default is the name
                                of the class in lowercase or if you have defined a have this.
        xml_root_attributes     List of attributes of the root tag
        xml_grouped_fields      Tuple of attributes grouped in one XML element. The tuple must have 2 values,
                                the first element is the XML tag and the second is an attribute of this element:
                                (amount, currency) -> <amount currency='EUR'>100</amount>
        xml_list_fields         Tuple of attributes represented by a list. The first element represents the XML tag,
                                and the second the name of each tag element:
                                (comments, comment) ->
                                <comments><comment id='1'></comment><comment id='1'></comment></comments>
    All flag fields are represented as follows: <field flag='1'></field>
    """

    xml_root_tag = ''
    xml_root_attributes = []
    xml_grouped_fields = []
    xml_list_fields = []

    def get_xml_root_tag(self):
        """
        This method return the XML root tag of the normalized object.
        For example <request> ... some attributes ... </request>
        :return: string
        """
        if not self.xml_root_tag:
            return self.__class__.__name__.lower()
        else:
            return self.xml_root_tag

    def normalize_xml(self):
        """
        This method return a normalized dictionary for XML parsing (xmltodict).
        In this process there are different options for normalization:
            * The object has an attribute that is also an object
            * The object has grouped fields
            * The object has list fields
            * The object has a root tag
            * The object has a flag field
            * The object has a standard (string, int, ...) field
        :return: dict
        """
        result = {}
        for key, value in six.iteritems(self.to_dict()):
            # This field (key) is an object
            if key in self.object_fields:
                result.update(value.normalize_xml())
            else:
                grouped_fields = [item for item in self.xml_grouped_fields if item[0] == key or item[1] == key]
                list_fields = [item for item in self.xml_list_fields if item[0] == key]
                if grouped_fields:
                    # This field (key) is a field grouped with another
                    result[grouped_fields[0][0]] = {
                        '@{}'.format(grouped_fields[0][1]): getattr(self, grouped_fields[0][1]),
                        '#text': getattr(self, grouped_fields[0][0])
                    }
                elif list_fields:
                    # This field (key) consists of a list of values
                    result[list_fields[0][0]] = {list_fields[0][1]: []}
                    for key_list, element_list in enumerate(getattr(self, list_fields[0][0])):
                        result[list_fields[0][0]][list_fields[0][1]].append({
                            '@id': key_list + 1,
                            '#text': element_list
                        })
                elif key in self.xml_root_attributes:
                    # This field (key) is an attribute of root tag
                    result['@{}'.format(key)] = value
                elif key in self.flag_fields:
                    # This field (key) is a flag field.
                    result[key] = {'@flag': value}
                else:
                    # This field (key) is a standard string/int field
                    result[key] = value
        return {self.get_xml_root_tag(): result}
