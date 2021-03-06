# Copyright 2017 NTT DATA
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

""" VM libvirt events

These are the events which needs to be processed by masakari in case of
instance recovery failure.
"""

INSTANCE_EVENTS = {
    # Add more events and vir_domain_events here.
    'LIFECYCLE': ['STOPPED_FAILED'],
    'IO_ERROR': ['IO_ERROR_REPORT']
}


def is_valid_event(payload):
    vir_domain_event_list = INSTANCE_EVENTS.get(payload.get('event'))
    if vir_domain_event_list and payload.get(
            'vir_domain_event') in vir_domain_event_list:
        return True
    return False
