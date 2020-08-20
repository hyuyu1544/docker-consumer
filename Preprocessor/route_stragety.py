import abc

from settings import logging

logger = logging.getLogger(__name__)


class Strategy(abc.ABC):
    """Strategy interface"""

    def __init__(self, **kwargs):
        """Init."""
        self.kwargs = kwargs

    @abc.abstractclassmethod
    def execute(self):
        """Implement different strategy."""
        pass


class Context:
    """Execute strategy from client."""

    def __init__(self, strategy: Strategy):
        """Init."""
        self._strategy = strategy

    def execute_strategy(self):
        """Delegate real strategy."""
        self._strategy.execute()


class MyItemStrategy(Strategy):
    """Strategy for `MyItem`."""

    def execute(self):
        """`My` item save to DB strategy."""
        logger.info(f'{self.__name__} execute.')
