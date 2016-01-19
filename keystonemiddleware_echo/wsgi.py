# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os

from oslo_config import cfg
import paste.deploy

from keystonemiddleware_echo import config

CONF = cfg.CONF


def echo_app():
    config.configure()

    paste_config = CONF.paste_deploy.config_file
    if not os.path.isabs(paste_config):
        paste_config = CONF.find_file(paste_config)

    return paste.deploy.loadapp('config:%s' % paste_config)
