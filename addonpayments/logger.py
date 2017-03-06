# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import logging


class Logger(object):
    """
    Wraps initialisation of the logging
    """

    initialised = False

    def get_logger(self, name):
        """
        This method initialises the logger when it has not yet been initialized
        :param name: string
        :return: Logging
        """
        if not self.initialised:
            logging.basicConfig(
                format="[%(asctime)s] %(levelname)s %(name)s:  %(message)s",
                level=logging.INFO,
            )
            self.initialised = True
        return logging.getLogger(name)
