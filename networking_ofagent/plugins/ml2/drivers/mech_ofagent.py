# Copyright (C) 2014 VA Linux Systems Japan K.K.
# Copyright (C) 2014 Fumihiko Kakuma <kakuma at valinux co jp>
# All Rights Reserved.
#
# Based on openvswitch mechanism driver.
#
# Copyright (c) 2013 OpenStack Foundation
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

import traceback

from oslo_log import log

from neutron.agent import securitygroups_rpc
from neutron.common import constants
from neutron.extensions import portbindings
from neutron.plugins.common import constants as p_constants
from neutron.plugins.ml2.drivers import mech_agent

LOG = log.getLogger(__name__)


class OfagentMechanismDriver(mech_agent.SimpleAgentMechanismDriverBase):
    """Attach to networks using ofagent L2 agent.

    The OfagentMechanismDriver integrates the ml2 plugin with the
    ofagent L2 agent. Port binding with this driver requires the
    ofagent agent to be running on the port's host, and that agent
    to have connectivity to at least one segment of the port's
    network.
    """

    def __init__(self):
        traceback.print_stack()
        sg_enabled = securitygroups_rpc.is_firewall_enabled()
        vif_details = {portbindings.CAP_PORT_FILTER: sg_enabled,
                       portbindings.OVS_HYBRID_PLUG: sg_enabled}
        super(OfagentMechanismDriver, self).__init__(
            constants.AGENT_TYPE_OVS,
            portbindings.VIF_TYPE_OVS,
            vif_details)

    def get_allowed_network_types(self, agent):
        return (agent['configurations'].get('tunnel_types', []) +
                [p_constants.TYPE_LOCAL, p_constants.TYPE_FLAT,
                 p_constants.TYPE_VLAN])

    def get_mappings(self, agent):
        #return dict(agent['configurations'].get('bridge_mappings', {}))
        print dict(agent['configurations'].get('interface_mappings', {}))
        return dict(agent['configurations'].get('interface_mappings', {}))

    def create_port_postcommit(self, context):
        print context.__module__ + "." + context.__class__.__name__
        print dir(context)
        print context.current
        print context.network.current
        print context.host
        print context._binding
        print context.vif_details
        traceback.print_stack()

    def update_port_postcommit(self, context):
        print context.__module__ + "." + context.__class__.__name__
        print dir(context)
        print context.current
        print context.network.current
        print context.host
        print context._binding
        print context.vif_details
        traceback.print_stack()

    def delete_port_postcommit(self, context):
        traceback.print_stack()

    def create_network_postcommit(self, context):
        traceback.print_stack()

    def delete_network_postcommit(self, context):
        traceback.print_stack()

