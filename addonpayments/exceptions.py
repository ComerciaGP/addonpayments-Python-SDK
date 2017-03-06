# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals


class SdkError(Exception):
    """
    An exception class for general SDK errors. All other SDK exceptions will extend this class.
    """

    def __init__(self, msg, original_exception=''):
        super(SdkError, self).__init__(msg + (": %s" % original_exception))
        self.original_exception = original_exception
