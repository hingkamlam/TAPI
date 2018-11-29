# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_photonic_media_media_channel_service_interface_point_spec import TapiPhotonicMediaMediaChannelServiceInterfacePointSpec  # noqa: F401,E501
from tapi_server import util


class TapiPhotonicMediaEndPointAugmentation1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, media_channel_service_interface_point_spec=None):  # noqa: E501
        """TapiPhotonicMediaEndPointAugmentation1 - a model defined in OpenAPI

        :param media_channel_service_interface_point_spec: The media_channel_service_interface_point_spec of this TapiPhotonicMediaEndPointAugmentation1.  # noqa: E501
        :type media_channel_service_interface_point_spec: TapiPhotonicMediaMediaChannelServiceInterfacePointSpec
        """
        self.openapi_types = {
            'media_channel_service_interface_point_spec': TapiPhotonicMediaMediaChannelServiceInterfacePointSpec
        }

        self.attribute_map = {
            'media_channel_service_interface_point_spec': 'media-channel-service-interface-point-spec'
        }

        self._media_channel_service_interface_point_spec = media_channel_service_interface_point_spec

    @classmethod
    def from_dict(cls, dikt) -> 'TapiPhotonicMediaEndPointAugmentation1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.photonic.media.EndPointAugmentation1 of this TapiPhotonicMediaEndPointAugmentation1.  # noqa: E501
        :rtype: TapiPhotonicMediaEndPointAugmentation1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def media_channel_service_interface_point_spec(self):
        """Gets the media_channel_service_interface_point_spec of this TapiPhotonicMediaEndPointAugmentation1.


        :return: The media_channel_service_interface_point_spec of this TapiPhotonicMediaEndPointAugmentation1.
        :rtype: TapiPhotonicMediaMediaChannelServiceInterfacePointSpec
        """
        return self._media_channel_service_interface_point_spec

    @media_channel_service_interface_point_spec.setter
    def media_channel_service_interface_point_spec(self, media_channel_service_interface_point_spec):
        """Sets the media_channel_service_interface_point_spec of this TapiPhotonicMediaEndPointAugmentation1.


        :param media_channel_service_interface_point_spec: The media_channel_service_interface_point_spec of this TapiPhotonicMediaEndPointAugmentation1.
        :type media_channel_service_interface_point_spec: TapiPhotonicMediaMediaChannelServiceInterfacePointSpec
        """

        self._media_channel_service_interface_point_spec = media_channel_service_interface_point_spec
