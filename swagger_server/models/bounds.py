# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Bounds(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, rows: int=None, cols: int=None):  # noqa: E501
        """Bounds - a model defined in Swagger

        :param rows: The rows of this Bounds.  # noqa: E501
        :type rows: int
        :param cols: The cols of this Bounds.  # noqa: E501
        :type cols: int
        """
        self.swagger_types = {
            'rows': int,
            'cols': int
        }

        self.attribute_map = {
            'rows': 'rows',
            'cols': 'cols'
        }
        self._rows = rows
        self._cols = cols

    @classmethod
    def from_dict(cls, dikt) -> 'Bounds':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Bounds of this Bounds.  # noqa: E501
        :rtype: Bounds
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rows(self) -> int:
        """Gets the rows of this Bounds.


        :return: The rows of this Bounds.
        :rtype: int
        """
        return self._rows

    @rows.setter
    def rows(self, rows: int):
        """Sets the rows of this Bounds.


        :param rows: The rows of this Bounds.
        :type rows: int
        """

        self._rows = rows

    @property
    def cols(self) -> int:
        """Gets the cols of this Bounds.


        :return: The cols of this Bounds.
        :rtype: int
        """
        return self._cols

    @cols.setter
    def cols(self, cols: int):
        """Sets the cols of this Bounds.


        :param cols: The cols of this Bounds.
        :type cols: int
        """

        self._cols = cols
