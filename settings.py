"""Settings."""
import logging
import logging.config

# logging setting
logging.config.fileConfig('logging.conf')

ES = {
    'URI': 'http://localhost:9200/',
}
