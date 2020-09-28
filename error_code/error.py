from response import BaseResponse

class BaseException(BaseResponse, Exception):
    def __init__(self, success=1, error_code=500, message='Base Error', data=None):
        super().__init__(success=success, \
            error_code=error_code, message=message, data=data)
