import json
import logging

from tornado.web import HTTPError, RequestHandler

from models.user import UserProfile, User
from models.status import Status
from models.token import Token

from api.v1.base_handler import BaseHandler
from auth.token_auth import bearerAuth

from utils.atomFeed import generate_feed

from managers.user_manager import new_user

from tasks.emails import confirm_token

logger = logging.getLogger(__name__)

class ActorHandler(BaseHandler):

    async def get(self, username):
        try:
            person = await self.application.objects.get(User, username=username)
            self.write(json.dumps(person.to_activitystream(), default=str))
                    
        except User.DoesNotExist:

            self.set_status(404)
            self.write({"Error": "User not found"})