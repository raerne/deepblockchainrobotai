# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Position(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, row: int=None, col: int=None):  # noqa: E501
        """Position - a model defined in Swagger

        :param row: The row of this Position.  # noqa: E501
        :type row: int
        :param col: The col of this Position.  # noqa: E501
        :type col: int
        """
        self.swagger_types = {
            'row': int,
            'col': int
        }

        self.attribute_map = {
            'row': 'row',
            'col': 'col'
        }
        self._row = row
        self._col = col

    @classmethod
    def from_dict(cls, dikt) -> 'Position':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Position of this Position.  # noqa: E501
        :rtype: Position
        """
        return util.deserialize_model(dikt, cls)

    @property
    def row(self) -> int:
        """Gets the row of this Position.


        :return: The row of this Position.
        :rtype: int
        """
        return self._row

    @row.setter
    def row(self, row: int):
        """Sets the row of this Position.


        :param row: The row of this Position.
        :type row: int
        """

        self._row = row

    @property
    def col(self) -> int:
        """Gets the col of this Position.


        :return: The col of this Position.
        :rtype: int
        """
        return self._col

    @col.setter
    def col(self, col: int):
        """Sets the col of this Position.


        :param col: The col of this Position.
        :type col: int
        """

        self._col = col
