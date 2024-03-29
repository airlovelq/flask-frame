import os
import jwt
from functools import wraps
from datetime import datetime, timedelta
from flask import request
from error_code import UnauthorizedError, InvalidAuthorizationHeaderError
from setting import APP_SECRET, TOKEN_EXPIRATION_HOURS
from database import DbStore

# extend JWT expiration to 1 day!


def generate_token(user_id, use_type, hours=TOKEN_EXPIRATION_HOURS, **kwargs):
    payload = {
        'user_id': user.id,
        'user_type': user.user_type,
        'exp': datetime.utcnow() + timedelta(hours=hours)
    }
    payload = {**kwargs, **payload}
    # TODO: if backend using jwt, how come frontend still
    # needs to configure token in localStorage?
    token = jwt.encode(payload, APP_SECRET, algorithm='HS256')
    return token.decode('utf-8')


def decode_token(token):
    payload = jwt.decode(token, APP_SECRET, algorithms=['HS256'])
    return payload


def auth_check(user_types=[]):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            auth_header = request.headers.get('authorization', None)
            token = extract_token_from_header(auth_header)
            auth = decode_token(token)
            
            # if len(user_types) > 0:
            #     if auth.get('user_type') not in user_types:
            #         raise UnauthorizedError()

            metastore = DbStore()
            with metastore:
                user = metastore.get_user_by_id(user_id=auth.get("user_id"))
                if user is None:
                    raise UnauthorizedError("user is not exist")
                # if user.user_type not in user_types:
                #     raise OperationUnAuthorizedError()

            return f(auth=auth, *args, **kwargs)

        return wrapped

    return decorator


def extract_token_from_header(header):
    if header is None:
        raise InvalidAuthorizationHeaderError()

    parts = header.split(' ')

    if len(parts) != 2:
        raise InvalidAuthorizationHeaderError()

    if parts[0] != 'Bearer':
        raise InvalidAuthorizationHeaderError()

    token = parts[1]
    return token