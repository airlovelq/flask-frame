from .error import BaseException
import traceback

class ParameterError(BaseException):
    def __init__(self, message="Param is error."):
        super().__init__(error_code=100, message=message)

class SystemInternalError(BaseException):
    def __init__(self, message='System Internal Error'):
        super().__init__(error_code=500, \
            message=message, data=traceback.format_exc())

class InvalidAuthorizationHeaderError(BaseException):
    def __init__(self, message="Invalid authorization header."):
        super().__init__(error_code=8000, \
            message=message)

class UnauthorizedError(BaseException):
    def __init__(self, message="Unauthorized Error"):
        super().__init__(error_code=8001, \
            message=message)
