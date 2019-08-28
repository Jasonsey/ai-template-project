# CIS Analysis
#
# Author: Lin, Max
# Email: max_lin1@dell.com
#
# =============================================================================
"""config file"""

# flask app config
HOST = '0.0.0.0'
PORT = '8080'

# gunicorn server config
workers = 5
worker_class = 'gevent'
bind = '0.0.0.0:8027'

