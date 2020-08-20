
from elasticsearch_dsl import connections
from settings import logging, ES

logger = logging.getLogger(__name__)

try:
    ES_CONN = connections.create_connection(
        hosts=[ES.get('URI')], timeout=30
    )
except Exception as e:
    logger.critical(e)
