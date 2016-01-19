import os

from oslo_config import cfg
from paste.deploy import loadapp
from wsgiref import simple_server

from keystonemiddleware_echo import config

CONF = cfg.CONF

config.configure()

paste_config = CONF.paste_deploy.config_file
if not os.path.isabs(paste_config):
    paste_config = CONF.find_file(paste_config)

app = loadapp('config:%s' % paste_config)

server = simple_server.make_server('', 8000, app)
print('Serving on port 8000 (Ctrl+C to end)...')
server.serve_forever()
