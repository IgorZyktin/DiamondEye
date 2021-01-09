# -*- coding: utf-8 -*-

"""Общие сетевые компоненты.
"""
import socket
import socketserver
from abc import abstractmethod, ABC
from typing import Type


def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))


if __name__ == "__main__":
    ip = '127.0.0.1'
    port = 9500
    client(ip, port, "Hello World 1")
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")
