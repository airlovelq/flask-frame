from .response import BaseResponse

class ResultSuccess(BaseResponse):
    def __init__(self, data=None):
        super().__init__(data=data)