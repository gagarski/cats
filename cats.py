#!/usr/bin/env python3
import os

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler

from find_cats import find_cats
from handlers import RootHandler
from settings import STATIC_ROOT, TEMPLATE_ROOT, PORT


def main():
    app = Application([
        (r"/", RootHandler, {"cats": find_cats()}),
        (r"/static/.*", StaticFileHandler)
    ], static_path=STATIC_ROOT, template_path=TEMPLATE_ROOT)
    server = HTTPServer(app)
    server.bind(PORT)
    server.start(0)  # forks one process per cpu
    IOLoop.current().start()


if __name__ == "__main__":
    main()
