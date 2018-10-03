import tornado.ioloop
import tornado.web
from tornado.platform.asyncio import AsyncIOMainLoop
import asyncio

import peewee_async

from models.base import db

from api.v1.user import (UserHandler, ProfileManager)
from api.v1.status import (StatusHandler, UserStatuses, FavouriteStatus,
                            UnFavouriteStatus    
                        )

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/api/v1/accounts/(?P<id>[\d+])', UserHandler),
        (r'/api/v1/accounts/(?P<id>[\d+])/statuses', UserStatuses),
        (r'/api/v1/accounts/update_credentials', ProfileManager),

        (r'/api/v1/statuses/', UserStatuses),
        (r'/api/v1/statuses/(?P<pid>[\d+]+)', StatusHandler),
        (r'/api/v1/statuses/(?P<pid>[\d+]+)/favourite', FavouriteStatus),
        (r'/api/v1/statuses/(?P<pid>[\d+]+)/unfavourite', UnFavouriteStatus),
    ], debug=True)

if __name__ == "__main__":
    #AsyncIOMainLoop().install()
    app = make_app()

    app.listen(8888)
    app.objects = peewee_async.Manager(db)
    #loop = asyncio.get_event_loop().run_forever()
    tornado.ioloop.IOLoop.current().start()