import json
import logging

from tornado.web import HTTPError, RequestHandler

from models.user import UserProfile, User
from models.status import Status
from models.token import Token

from api.base_handler import BaseHandler

from auth.token_auth import bearerAuth
from decorators.get_by_id import retrive_by_id

from managers.user_manager import UserManager

logger = logging.getLogger(__name__)


class StatusHandler(BaseHandler):
    """
    Operate over the status with a given id.
    
    The delete operation requires the token to auth the user

    """

    @retrive_by_id(Status)
    async def get(self, id, target):
        status = self.application.objects.get(Status, id=id)
        self.write(json.dumps(status.to_json(), default=str))
            
    @bearerAuth
    @retrive_by_id(Status)
    async def delete(self, id, user, target):
        if target.user.id == user.id:
            await self.application.objects.delete(target)
        else:
            self.write({"Error": "You can't perform this action"})


class FavouriteStatus(BaseHandler):

    @bearerAuth
    @retrive_by_id(Status)
    async def post(self, id, target, user):
        UserManager(user).like(target)
        self.write(json.dumps(status, default=str))

class UnFavouriteStatus(BaseHandler):

    async def post(self, id, target, user):

        UserManager(user).dislike(target)
        self.write(json.dumps(target, default=str)

class UserStatuses(BaseHandler):

    @is_authenticated
    async def get(self, user, is_authenticated):

        
                   
    
