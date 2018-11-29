# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_oam_updateoamjob_input import TapiOamUpdateoamjobInput  # noqa: F401,E501
from tapi_server import util


class InlineObject29(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, input=None):  # noqa: E501
        """InlineObject29 - a model defined in OpenAPI

        :param input: The input of this InlineObject29.  # noqa: E501
        :type input: TapiOamUpdateoamjobInput
        """
        self.openapi_types = {
            'input': TapiOamUpdateoamjobInput
        }

        self.attribute_map = {
            'input': 'input'
        }

        self._input = input

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject29':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_29 of this InlineObject29.  # noqa: E501
        :rtype: InlineObject29
        """
        return util.deserialize_model(dikt, cls)

    @property
    def input(self):
        """Gets the input of this InlineObject29.


        :return: The input of this InlineObject29.
        :rtype: TapiOamUpdateoamjobInput
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this InlineObject29.


        :param input: The input of this InlineObject29.
        :type input: TapiOamUpdateoamjobInput
        """

        self._input = input
