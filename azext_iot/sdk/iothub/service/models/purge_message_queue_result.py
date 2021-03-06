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

from msrest.serialization import Model


class PurgeMessageQueueResult(Model):
    """Result of a device message queue purge operation.

    :param total_messages_purged:
    :type total_messages_purged: int
    :param device_id: The ID of the device whose messages are being purged.
    :type device_id: str
    :param module_id: The ID of the device whose messages are being purged.
    :type module_id: str
    """

    _attribute_map = {
        'total_messages_purged': {'key': 'totalMessagesPurged', 'type': 'int'},
        'device_id': {'key': 'deviceId', 'type': 'str'},
        'module_id': {'key': 'moduleId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PurgeMessageQueueResult, self).__init__(**kwargs)
        self.total_messages_purged = kwargs.get('total_messages_purged', None)
        self.device_id = kwargs.get('device_id', None)
        self.module_id = kwargs.get('module_id', None)
