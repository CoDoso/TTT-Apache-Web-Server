import sys
import logging
from app import app as application

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/flaskapp")
