import json
import traceback

class BaseResponse(object):
    def __init__(self, success=0, error_code=0, message='Result is Success', data=None):
        self.error_code = error_code
        self.success = success
        self.message = message
        self.data = data

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return '{}:{}'.format(self.__class__.__name__,  json.dumps(self.__dict__))

    def __iter__(self):
        for item in self.__dict__:
            yield (item, self.__dict__[item])