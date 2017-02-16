# -*- encoding: utf-8 -*-


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
