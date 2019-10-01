import random

from tornado.web import RequestHandler


class RootHandler(RequestHandler):
    def initialize(self, cats):
        if not cats:
            raise ValueError("No cats found")
        self.cats = cats

    def get(self):
        self.render("index.html", cat="/static/" + random.choice(self.cats))
