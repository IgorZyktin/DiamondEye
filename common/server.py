# -*- coding: utf-8 -*-

"""Общие сетевые компоненты.
"""
import socketserver
from abc import abstractmethod, ABC
from typing import Type


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Базовый класс TCP сервера.
    """


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler, ABC):
    """Базовый класс обработчика запросов.
    """

    @abstractmethod
    def handle(self) -> None:
        """Обработать запрос.
        """


def get_server(config, handler_type: Type[ThreadedTCPRequestHandler]) \
        -> ThreadedTCPServer:
    """Создать экземпляр сервера.
    """
    return ThreadedTCPServer(
        (config.HOST, config.PORT),
        handler_type
    )


def serve_forever(server: ThreadedTCPServer) -> None:
    """Бесконечный цикл обработки данных.
    """
    with server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.shutdown()
