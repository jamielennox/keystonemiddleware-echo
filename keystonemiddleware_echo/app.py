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

import json
import webob.dec


@webob.dec.wsgify
def echo_app(request):
    """A WSGI application that echoes the CGI environment to the user."""
    return webob.Response(content_type='application/json',
                          body=json.dumps(request.environ, indent=4))


def echo_app_factory(global_conf, **local_conf):
    import ipdb; ipdb.set_trace()
    return echo_app
