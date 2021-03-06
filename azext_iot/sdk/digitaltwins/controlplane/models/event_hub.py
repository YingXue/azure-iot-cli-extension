# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .digital_twins_endpoint_resource_properties import DigitalTwinsEndpointResourceProperties


class EventHub(DigitalTwinsEndpointResourceProperties):
    """Properties related to EventHub.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar provisioning_state: The provisioning state. Possible values include:
     'Provisioning', 'Deleting', 'Succeeded', 'Failed', 'Canceled', 'Deleted',
     'Warning', 'Suspending', 'Restoring', 'Moving', 'Disabled'
    :vartype provisioning_state: str or
     ~azure.mgmt.digitaltwins.models.EndpointProvisioningState
    :ivar created_time: Time when the Endpoint was added to
     DigitalTwinsInstance.
    :vartype created_time: datetime
    :param dead_letter_secret: Dead letter storage secret. Will be obfuscated
     during read.
    :type dead_letter_secret: str
    :param endpoint_type: Required. Constant filled by server.
    :type endpoint_type: str
    :param connection_string_primary_key: Required. PrimaryConnectionString of
     the endpoint. Will be obfuscated during read.
    :type connection_string_primary_key: str
    :param connection_string_secondary_key: SecondaryConnectionString of the
     endpoint. Will be obfuscated during read.
    :type connection_string_secondary_key: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'created_time': {'readonly': True},
        'endpoint_type': {'required': True},
        'connection_string_primary_key': {'required': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'dead_letter_secret': {'key': 'deadLetterSecret', 'type': 'str'},
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'connection_string_primary_key': {'key': 'connectionStringPrimaryKey', 'type': 'str'},
        'connection_string_secondary_key': {'key': 'connectionStringSecondaryKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EventHub, self).__init__(**kwargs)
        self.connection_string_primary_key = kwargs.get('connection_string_primary_key', None)
        self.connection_string_secondary_key = kwargs.get('connection_string_secondary_key', None)
        self.endpoint_type = 'EventHub'
