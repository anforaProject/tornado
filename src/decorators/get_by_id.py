from models.user import User 
from models.token import Token

import peewee_async
import functools
from models.base import db

def retrive_by_id(method, model):

    @functools.wraps(method)
    async def wrapper(self, *args, **kwargs):
        #id is one of the arguments of the function
        try:
            obj = await self.application.objects.get(model, id=id)
            kwargs["target"] = obj
        except:
            handler.set_status(404)
            handler.write("Object not found")
            handler.finish()
        return method(self,*args, **kwargs)
    return wrapper
