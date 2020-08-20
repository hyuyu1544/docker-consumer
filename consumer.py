from conn.conn_mq import MQConsumer
from settings import logging
import json
import os
from Preprocessor.route_stragety import Context, MyItemStrategy
logger = logging.getLogger(__name__)


class Consumer(MQConsumer):
    """Implement Consumer."""

    def __init__(self):
        pass

    def callback(self, channel, method, properties, body):
        """MQ consumer callback."""
        logger.info(f'received: {method.routing_key}')
        item = json.loads(body.decode())
        logger.info(item)
        kwargs = {
            'item': item
        }
        if method.routing_key == 'my_route':
            context = Context(MyItemStrategy(**kwargs))
        context.execute_strategy()

        channel.basic_ack(delivery_tag=method.delivery_tag)
        logger.info('Done')

    def construct(self):
        """Construct consumer pipline."""

        pipeline_list = [
            {
                'exchange': 'data_collections',
                'queue': 'my_queue',
                'routing_key': 'my_route'
            },
        ]
        for pipe in pipeline_list:
            self.add_consumer_pipeline(
                exchange=pipe['exchange'],
                queue_name=pipe['queue'],
                routing_key=pipe['routing_key'],
                callback=self.callback
            )


def main():
    """Execute function."""
    consumer = Consumer()
    consumer.set_connection(
        host=os.environ['RABBITMQ_HOST'],
        port=os.environ['RABBITMQ_PORT']
    )
    consumer.construct()
    logger.info('start consumer...')
    consumer.execute()
    consumer.close_connection()


if __name__ == '__main__':
    main()
