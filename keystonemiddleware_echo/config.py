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

import copy

from oslo_log import log as logging
from oslo_config import cfg

CONF = cfg.CONF

OPTS = {
    'paste_deploy': [
        cfg.StrOpt('config_file',
                   default='keystonemiddleware_echo-paste.ini',
                   help='Name of the paste configuration file that defines '
                        'the available pipelines.'),
    ],
}


def configure():
    logging.register_options(CONF)
    logging.setup(CONF, 'echo')

    for k, v in OPTS.items():
        CONF.register_opts(v, group=k)

    CONF(project='keystonemiddleware_echo')
    CONF.log_opt_values(logging.getLogger(__name__), logging.DEBUG)


def list_opts():
    return ((k, copy.deepcopy(v)) for k, v in OPTS.items())
