import json

from tornado.web import RequestHandler, HTTPError
from models.user import User

class UserHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')

    async def get(self,id):

        try:
            person = await self.application.objects.get(User, User.id==int(id))
            profile = person.profile.get()

            self.write(json.dumps(profile.to_json(), default=str).encode('utf-8'))
            self.set_status(200)
        except User.DoesNotExist:
            raise HTTPError(404, "User not found")
        