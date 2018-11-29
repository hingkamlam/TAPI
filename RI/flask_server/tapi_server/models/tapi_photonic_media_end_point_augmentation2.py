# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_photonic_media_otsi_connectivity_service_end_point_spec import TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec  # noqa: F401,E501
from tapi_server import util


class TapiPhotonicMediaEndPointAugmentation2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, otsi_connectivity_service_end_point_spec=None):  # noqa: E501
        """TapiPhotonicMediaEndPointAugmentation2 - a model defined in OpenAPI

        :param otsi_connectivity_service_end_point_spec: The otsi_connectivity_service_end_point_spec of this TapiPhotonicMediaEndPointAugmentation2.  # noqa: E501
        :type otsi_connectivity_service_end_point_spec: TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec
        """
        self.openapi_types = {
            'otsi_connectivity_service_end_point_spec': TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec
        }

        self.attribute_map = {
            'otsi_connectivity_service_end_point_spec': 'otsi-connectivity-service-end-point-spec'
        }

        self._otsi_connectivity_service_end_point_spec = otsi_connectivity_service_end_point_spec

    @classmethod
    def from_dict(cls, dikt) -> 'TapiPhotonicMediaEndPointAugmentation2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.photonic.media.EndPointAugmentation2 of this TapiPhotonicMediaEndPointAugmentation2.  # noqa: E501
        :rtype: TapiPhotonicMediaEndPointAugmentation2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def otsi_connectivity_service_end_point_spec(self):
        """Gets the otsi_connectivity_service_end_point_spec of this TapiPhotonicMediaEndPointAugmentation2.


        :return: The otsi_connectivity_service_end_point_spec of this TapiPhotonicMediaEndPointAugmentation2.
        :rtype: TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec
        """
        return self._otsi_connectivity_service_end_point_spec

    @otsi_connectivity_service_end_point_spec.setter
    def otsi_connectivity_service_end_point_spec(self, otsi_connectivity_service_end_point_spec):
        """Sets the otsi_connectivity_service_end_point_spec of this TapiPhotonicMediaEndPointAugmentation2.


        :param otsi_connectivity_service_end_point_spec: The otsi_connectivity_service_end_point_spec of this TapiPhotonicMediaEndPointAugmentation2.
        :type otsi_connectivity_service_end_point_spec: TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec
        """

        self._otsi_connectivity_service_end_point_spec = otsi_connectivity_service_end_point_spec
