# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_notification_getnotificationlist_input import TapiNotificationGetnotificationlistInput  # noqa: F401,E501
from tapi_server import util


class InlineObject19(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, input=None):  # noqa: E501
        """InlineObject19 - a model defined in OpenAPI

        :param input: The input of this InlineObject19.  # noqa: E501
        :type input: TapiNotificationGetnotificationlistInput
        """
        self.openapi_types = {
            'input': TapiNotificationGetnotificationlistInput
        }

        self.attribute_map = {
            'input': 'input'
        }

        self._input = input

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject19':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_19 of this InlineObject19.  # noqa: E501
        :rtype: InlineObject19
        """
        return util.deserialize_model(dikt, cls)

    @property
    def input(self):
        """Gets the input of this InlineObject19.


        :return: The input of this InlineObject19.
        :rtype: TapiNotificationGetnotificationlistInput
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this InlineObject19.


        :param input: The input of this InlineObject19.
        :type input: TapiNotificationGetnotificationlistInput
        """

        self._input = input
