# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.latency_characteristic import LatencyCharacteristic  # noqa: F401,E501
from tapi_server import util


class TransferTimingPac(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, latency_characteristic: List[LatencyCharacteristic]=None):  # noqa: E501
        """TransferTimingPac - a model defined in Swagger

        :param latency_characteristic: The latency_characteristic of this TransferTimingPac.  # noqa: E501
        :type latency_characteristic: List[LatencyCharacteristic]
        """
        self.swagger_types = {
            'latency_characteristic': List[LatencyCharacteristic]
        }

        self.attribute_map = {
            'latency_characteristic': 'latency-characteristic'
        }

        self._latency_characteristic = latency_characteristic

    @classmethod
    def from_dict(cls, dikt) -> 'TransferTimingPac':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The transfer-timing-pac of this TransferTimingPac.  # noqa: E501
        :rtype: TransferTimingPac
        """
        return util.deserialize_model(dikt, cls)

    @property
    def latency_characteristic(self) -> List[LatencyCharacteristic]:
        """Gets the latency_characteristic of this TransferTimingPac.

        The effect on the latency of a queuing process. This only has significant effect for packet based systems and has a complex characteristic.  # noqa: E501

        :return: The latency_characteristic of this TransferTimingPac.
        :rtype: List[LatencyCharacteristic]
        """
        return self._latency_characteristic

    @latency_characteristic.setter
    def latency_characteristic(self, latency_characteristic: List[LatencyCharacteristic]):
        """Sets the latency_characteristic of this TransferTimingPac.

        The effect on the latency of a queuing process. This only has significant effect for packet based systems and has a complex characteristic.  # noqa: E501

        :param latency_characteristic: The latency_characteristic of this TransferTimingPac.
        :type latency_characteristic: List[LatencyCharacteristic]
        """

        self._latency_characteristic = latency_characteristic