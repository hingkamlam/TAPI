# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_admin_state_pac import TapiCommonAdminStatePac  # noqa: F401,E501
from tapi_server.models.tapi_common_administrative_state import TapiCommonAdministrativeState  # noqa: F401,E501
from tapi_server.models.tapi_common_layer_protocol_name import TapiCommonLayerProtocolName  # noqa: F401,E501
from tapi_server.models.tapi_common_lifecycle_state import TapiCommonLifecycleState  # noqa: F401,E501
from tapi_server.models.tapi_common_local_class import TapiCommonLocalClass  # noqa: F401,E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: F401,E501
from tapi_server.models.tapi_common_operational_state import TapiCommonOperationalState  # noqa: F401,E501
from tapi_server.models.tapi_common_port_direction import TapiCommonPortDirection  # noqa: F401,E501
from tapi_server.models.tapi_common_service_interface_point_ref import TapiCommonServiceInterfacePointRef  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_connectivity_service_end_point_ref import TapiConnectivityConnectivityServiceEndPointRef  # noqa: F401,E501
from tapi_server.models.tapi_oam_mep_ref import TapiOamMepRef  # noqa: F401,E501
from tapi_server.models.tapi_oam_mip_ref import TapiOamMipRef  # noqa: F401,E501
from tapi_server import util


class TapiOamOamServiceEndPoint(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, operational_state=None, lifecycle_state=None, administrative_state=None, name=None, local_id=None, peer_mep_identifier=None, connectivity_service_end_point=None, mip=None, service_interface_point=None, layer_protocol_name=None, mep=None, mep_identifier=None, direction=None):  # noqa: E501
        """TapiOamOamServiceEndPoint - a model defined in OpenAPI

        :param operational_state: The operational_state of this TapiOamOamServiceEndPoint.  # noqa: E501
        :type operational_state: TapiCommonOperationalState
        :param lifecycle_state: The lifecycle_state of this TapiOamOamServiceEndPoint.  # noqa: E501
        :type lifecycle_state: TapiCommonLifecycleState
        :param administrative_state: The administrative_state of this TapiOamOamServiceEndPoint.  # noqa: E501
        :type administrative_state: TapiCommonAdministrativeState
        :param name: The name of this TapiOamOamServiceEndPoint.  # noqa: E501
        :type name: List[TapiCommonNameAndValue]
        :param local_id: The local_id of this TapiOamOamServiceEndPoint.  # noqa: E501
        :type local_id: str
        :param peer_mep_identifier: The peer_mep_identifier of this TapiOamOamServiceEndPoint.  # noqa: E501
        :type peer_mep_identifier: List[str]
        :param connectivity_service_end_point: The connectivity_service_end_point of this TapiOamOamServiceEndPoint.  # noqa: E501
        :type connectivity_service_end_point: TapiConnectivityConnectivityServiceEndPointRef
        :param mip: The mip of this TapiOamOamServiceEndPoint.  # noqa: E501
        :type mip: TapiOamMipRef
        :param service_interface_point: The service_interface_point of this TapiOamOamServiceEndPoint.  # noqa: E501
        :type service_interface_point: TapiCommonServiceInterfacePointRef
        :param layer_protocol_name: The layer_protocol_name of this TapiOamOamServiceEndPoint.  # noqa: E501
        :type layer_protocol_name: TapiCommonLayerProtocolName
        :param mep: The mep of this TapiOamOamServiceEndPoint.  # noqa: E501
        :type mep: TapiOamMepRef
        :param mep_identifier: The mep_identifier of this TapiOamOamServiceEndPoint.  # noqa: E501
        :type mep_identifier: str
        :param direction: The direction of this TapiOamOamServiceEndPoint.  # noqa: E501
        :type direction: TapiCommonPortDirection
        """
        self.openapi_types = {
            'operational_state': TapiCommonOperationalState,
            'lifecycle_state': TapiCommonLifecycleState,
            'administrative_state': TapiCommonAdministrativeState,
            'name': List[TapiCommonNameAndValue],
            'local_id': str,
            'peer_mep_identifier': List[str],
            'connectivity_service_end_point': TapiConnectivityConnectivityServiceEndPointRef,
            'mip': TapiOamMipRef,
            'service_interface_point': TapiCommonServiceInterfacePointRef,
            'layer_protocol_name': TapiCommonLayerProtocolName,
            'mep': TapiOamMepRef,
            'mep_identifier': str,
            'direction': TapiCommonPortDirection
        }

        self.attribute_map = {
            'operational_state': 'operational-state',
            'lifecycle_state': 'lifecycle-state',
            'administrative_state': 'administrative-state',
            'name': 'name',
            'local_id': 'local-id',
            'peer_mep_identifier': 'peer-mep-identifier',
            'connectivity_service_end_point': 'connectivity-service-end-point',
            'mip': 'mip',
            'service_interface_point': 'service-interface-point',
            'layer_protocol_name': 'layer-protocol-name',
            'mep': 'mep',
            'mep_identifier': 'mep-identifier',
            'direction': 'direction'
        }

        self._operational_state = operational_state
        self._lifecycle_state = lifecycle_state
        self._administrative_state = administrative_state
        self._name = name
        self._local_id = local_id
        self._peer_mep_identifier = peer_mep_identifier
        self._connectivity_service_end_point = connectivity_service_end_point
        self._mip = mip
        self._service_interface_point = service_interface_point
        self._layer_protocol_name = layer_protocol_name
        self._mep = mep
        self._mep_identifier = mep_identifier
        self._direction = direction

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOamOamServiceEndPoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.oam.OamServiceEndPoint of this TapiOamOamServiceEndPoint.  # noqa: E501
        :rtype: TapiOamOamServiceEndPoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def operational_state(self):
        """Gets the operational_state of this TapiOamOamServiceEndPoint.


        :return: The operational_state of this TapiOamOamServiceEndPoint.
        :rtype: TapiCommonOperationalState
        """
        return self._operational_state

    @operational_state.setter
    def operational_state(self, operational_state):
        """Sets the operational_state of this TapiOamOamServiceEndPoint.


        :param operational_state: The operational_state of this TapiOamOamServiceEndPoint.
        :type operational_state: TapiCommonOperationalState
        """

        self._operational_state = operational_state

    @property
    def lifecycle_state(self):
        """Gets the lifecycle_state of this TapiOamOamServiceEndPoint.


        :return: The lifecycle_state of this TapiOamOamServiceEndPoint.
        :rtype: TapiCommonLifecycleState
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """Sets the lifecycle_state of this TapiOamOamServiceEndPoint.


        :param lifecycle_state: The lifecycle_state of this TapiOamOamServiceEndPoint.
        :type lifecycle_state: TapiCommonLifecycleState
        """

        self._lifecycle_state = lifecycle_state

    @property
    def administrative_state(self):
        """Gets the administrative_state of this TapiOamOamServiceEndPoint.


        :return: The administrative_state of this TapiOamOamServiceEndPoint.
        :rtype: TapiCommonAdministrativeState
        """
        return self._administrative_state

    @administrative_state.setter
    def administrative_state(self, administrative_state):
        """Sets the administrative_state of this TapiOamOamServiceEndPoint.


        :param administrative_state: The administrative_state of this TapiOamOamServiceEndPoint.
        :type administrative_state: TapiCommonAdministrativeState
        """

        self._administrative_state = administrative_state

    @property
    def name(self):
        """Gets the name of this TapiOamOamServiceEndPoint.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this TapiOamOamServiceEndPoint.
        :rtype: List[TapiCommonNameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TapiOamOamServiceEndPoint.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this TapiOamOamServiceEndPoint.
        :type name: List[TapiCommonNameAndValue]
        """

        self._name = name

    @property
    def local_id(self):
        """Gets the local_id of this TapiOamOamServiceEndPoint.

        none  # noqa: E501

        :return: The local_id of this TapiOamOamServiceEndPoint.
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this TapiOamOamServiceEndPoint.

        none  # noqa: E501

        :param local_id: The local_id of this TapiOamOamServiceEndPoint.
        :type local_id: str
        """

        self._local_id = local_id

    @property
    def peer_mep_identifier(self):
        """Gets the peer_mep_identifier of this TapiOamOamServiceEndPoint.

        This attribute models the MI_PeerMEP_ID[i] defined in G.8021 and configured as specified in G.8051. It provides the identifiers of the MEPs which are peer to the subject MEP.                      This attribute is not specified in case the OSEP relates to the provisioing of an MIP.                      In case of P2P, there is only one peer  # noqa: E501

        :return: The peer_mep_identifier of this TapiOamOamServiceEndPoint.
        :rtype: List[str]
        """
        return self._peer_mep_identifier

    @peer_mep_identifier.setter
    def peer_mep_identifier(self, peer_mep_identifier):
        """Sets the peer_mep_identifier of this TapiOamOamServiceEndPoint.

        This attribute models the MI_PeerMEP_ID[i] defined in G.8021 and configured as specified in G.8051. It provides the identifiers of the MEPs which are peer to the subject MEP.                      This attribute is not specified in case the OSEP relates to the provisioing of an MIP.                      In case of P2P, there is only one peer  # noqa: E501

        :param peer_mep_identifier: The peer_mep_identifier of this TapiOamOamServiceEndPoint.
        :type peer_mep_identifier: List[str]
        """

        self._peer_mep_identifier = peer_mep_identifier

    @property
    def connectivity_service_end_point(self):
        """Gets the connectivity_service_end_point of this TapiOamOamServiceEndPoint.


        :return: The connectivity_service_end_point of this TapiOamOamServiceEndPoint.
        :rtype: TapiConnectivityConnectivityServiceEndPointRef
        """
        return self._connectivity_service_end_point

    @connectivity_service_end_point.setter
    def connectivity_service_end_point(self, connectivity_service_end_point):
        """Sets the connectivity_service_end_point of this TapiOamOamServiceEndPoint.


        :param connectivity_service_end_point: The connectivity_service_end_point of this TapiOamOamServiceEndPoint.
        :type connectivity_service_end_point: TapiConnectivityConnectivityServiceEndPointRef
        """

        self._connectivity_service_end_point = connectivity_service_end_point

    @property
    def mip(self):
        """Gets the mip of this TapiOamOamServiceEndPoint.


        :return: The mip of this TapiOamOamServiceEndPoint.
        :rtype: TapiOamMipRef
        """
        return self._mip

    @mip.setter
    def mip(self, mip):
        """Sets the mip of this TapiOamOamServiceEndPoint.


        :param mip: The mip of this TapiOamOamServiceEndPoint.
        :type mip: TapiOamMipRef
        """

        self._mip = mip

    @property
    def service_interface_point(self):
        """Gets the service_interface_point of this TapiOamOamServiceEndPoint.


        :return: The service_interface_point of this TapiOamOamServiceEndPoint.
        :rtype: TapiCommonServiceInterfacePointRef
        """
        return self._service_interface_point

    @service_interface_point.setter
    def service_interface_point(self, service_interface_point):
        """Sets the service_interface_point of this TapiOamOamServiceEndPoint.


        :param service_interface_point: The service_interface_point of this TapiOamOamServiceEndPoint.
        :type service_interface_point: TapiCommonServiceInterfacePointRef
        """

        self._service_interface_point = service_interface_point

    @property
    def layer_protocol_name(self):
        """Gets the layer_protocol_name of this TapiOamOamServiceEndPoint.


        :return: The layer_protocol_name of this TapiOamOamServiceEndPoint.
        :rtype: TapiCommonLayerProtocolName
        """
        return self._layer_protocol_name

    @layer_protocol_name.setter
    def layer_protocol_name(self, layer_protocol_name):
        """Sets the layer_protocol_name of this TapiOamOamServiceEndPoint.


        :param layer_protocol_name: The layer_protocol_name of this TapiOamOamServiceEndPoint.
        :type layer_protocol_name: TapiCommonLayerProtocolName
        """

        self._layer_protocol_name = layer_protocol_name

    @property
    def mep(self):
        """Gets the mep of this TapiOamOamServiceEndPoint.


        :return: The mep of this TapiOamOamServiceEndPoint.
        :rtype: TapiOamMepRef
        """
        return self._mep

    @mep.setter
    def mep(self, mep):
        """Sets the mep of this TapiOamOamServiceEndPoint.


        :param mep: The mep of this TapiOamOamServiceEndPoint.
        :type mep: TapiOamMepRef
        """

        self._mep = mep

    @property
    def mep_identifier(self):
        """Gets the mep_identifier of this TapiOamOamServiceEndPoint.

        This attribute contains the identifier of the MEP.                      This attribute is empty in case the OSEP relates to the provisioing of an MIP.                        # noqa: E501

        :return: The mep_identifier of this TapiOamOamServiceEndPoint.
        :rtype: str
        """
        return self._mep_identifier

    @mep_identifier.setter
    def mep_identifier(self, mep_identifier):
        """Sets the mep_identifier of this TapiOamOamServiceEndPoint.

        This attribute contains the identifier of the MEP.                      This attribute is empty in case the OSEP relates to the provisioing of an MIP.                        # noqa: E501

        :param mep_identifier: The mep_identifier of this TapiOamOamServiceEndPoint.
        :type mep_identifier: str
        """

        self._mep_identifier = mep_identifier

    @property
    def direction(self):
        """Gets the direction of this TapiOamOamServiceEndPoint.


        :return: The direction of this TapiOamOamServiceEndPoint.
        :rtype: TapiCommonPortDirection
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this TapiOamOamServiceEndPoint.


        :param direction: The direction of this TapiOamOamServiceEndPoint.
        :type direction: TapiCommonPortDirection
        """

        self._direction = direction
