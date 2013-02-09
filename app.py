# -*- coding: utf-8 -*-
"""


"""
import os
import tornado.web
import tornado.ioloop
from tornado.options import define, options
import aligner
import json


class CheckHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('service online')


class AlignHandler(tornado.web.RequestHandler):
    def get(self):
        p_tokens = self.get_argument("p_tokens", strip=True).split(",")
        h_tokens = self.get_argument("h_tokens", strip=True).split(",")
        weights = self.get_argument("weights", strip=True)
        alignments, score = aligner.align(p_tokens, h_tokens, weights)
        d = json.dumps([vars(a) for a in alignments], sort_keys=True, indent=4)
        self.write(d)

handlers = [
            (r"/check", CheckHandler),
            (r"/align", AlignHandler),
            ]


settings = dict(template_path=os.path.join(
    os.path.dirname(__file__), "templates"))
application = tornado.web.Application(handlers, **settings)
define("port", default=8000, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()