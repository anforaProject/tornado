import tornado.ioloop
import tornado.web
from tornado.platform.asyncio import AsyncIOMainLoop
import asyncio

import peewee_async

from models.base import db

from api.user import UserHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/user/(?P<id>[^\/]+)', UserHandler)
    ], debug=True)

if __name__ == "__main__":
    #AsyncIOMainLoop().install()
    app = make_app()

    app.listen(8888)
    app.objects = peewee_async.Manager(db)
    #loop = asyncio.get_event_loop().run_forever()
    tornado.ioloop.IOLoop.current().start()