"""Base class for consumer."""
import abc
from typing import Callable

import pika


class MQConsumer(abc.ABC):
    """Consumer abstract class."""

    def __init__(self):
        """Init."""
        self.connection = None
        self.channel = None

    def set_connection(self, host, port):
        """Set up connection."""
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, port=port)
        )
        self.channel = self.connection.channel()

    def add_consumer_pipeline(
        self,
        exchange: str,
        queue_name: str,
        routing_key: str,
        callback: Callable
    ) -> object:
        """Add concumer pipeline."""

        self.channel.exchange_declare(
            exchange=exchange, exchange_type='direct', durable=True)

        queue = self.channel.queue_declare(
            queue=queue_name,
            durable=True
        )

        self.channel.queue_bind(
            exchange=exchange,
            queue=queue.method.queue,
            routing_key=routing_key
        )

        self.channel.basic_consume(
            # on_message_callback=callback,
            callback,
            queue=queue.method.queue
        )

        return self

    def execute(self):
        self.channel.start_consuming()

    def close_connection(self):
        self.connection.close()
