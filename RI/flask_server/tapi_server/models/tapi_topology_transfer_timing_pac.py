# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_topology_latency_characteristic import TapiTopologyLatencyCharacteristic  # noqa: F401,E501
from tapi_server import util


class TapiTopologyTransferTimingPac(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, latency_characteristic=None):  # noqa: E501
        """TapiTopologyTransferTimingPac - a model defined in OpenAPI

        :param latency_characteristic: The latency_characteristic of this TapiTopologyTransferTimingPac.  # noqa: E501
        :type latency_characteristic: List[TapiTopologyLatencyCharacteristic]
        """
        self.openapi_types = {
            'latency_characteristic': List[TapiTopologyLatencyCharacteristic]
        }

        self.attribute_map = {
            'latency_characteristic': 'latency-characteristic'
        }

        self._latency_characteristic = latency_characteristic

    @classmethod
    def from_dict(cls, dikt) -> 'TapiTopologyTransferTimingPac':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.topology.TransferTimingPac of this TapiTopologyTransferTimingPac.  # noqa: E501
        :rtype: TapiTopologyTransferTimingPac
        """
        return util.deserialize_model(dikt, cls)

    @property
    def latency_characteristic(self):
        """Gets the latency_characteristic of this TapiTopologyTransferTimingPac.

        The effect on the latency of a queuing process. This only has significant effect for packet based systems and has a complex characteristic.  # noqa: E501

        :return: The latency_characteristic of this TapiTopologyTransferTimingPac.
        :rtype: List[TapiTopologyLatencyCharacteristic]
        """
        return self._latency_characteristic

    @latency_characteristic.setter
    def latency_characteristic(self, latency_characteristic):
        """Sets the latency_characteristic of this TapiTopologyTransferTimingPac.

        The effect on the latency of a queuing process. This only has significant effect for packet based systems and has a complex characteristic.  # noqa: E501

        :param latency_characteristic: The latency_characteristic of this TapiTopologyTransferTimingPac.
        :type latency_characteristic: List[TapiTopologyLatencyCharacteristic]
        """

        self._latency_characteristic = latency_characteristic
