from models.user import User 
from models.token import Token

import peewee_async
import functools
from models.base import db

def loadUserToken(token, object):
    
    try:
        candidate = Token.get(key=token)
        return candidate.user
    except Token.DoesNotExist:
        return None


def bearerAuth(method):

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            if self.request.method in ("GET", "HEAD"):
                auth = self.request.headers.get('Authorization')

                if auth:
                    parts = auth.split()

                    if parts[0].lower() != 'bearer':
                        handler._transforms = []
                        handler.set_status(401)
                        handler.write("invalid header authorization")
                        handler.finish()
                    elif len(parts) == 1:
                        handler._transforms = []
                        handler.set_status(401)
                        handler.write("invalid header authorization")
                        handler.finish()
                    elif len(parts) > 2:
                        handler._transforms = []
                        handler.set_status(401)
                        handler.write("invalid header authorization")
                        handler.finish()

                    token = parts[1]
                    t = loadUserToken(token, self.application.objects)
                    kwargs['user'] = t
        return method(self,*args, **kwargs)
    return wrapper
