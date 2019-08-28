# CIS Analysis
#
# Author: Lin, Max
# Email: max_lin1@dell.com
#
# =============================================================================
"""main entry"""
from deploy.app import app
import config


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=True)

