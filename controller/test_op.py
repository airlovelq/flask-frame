from .base_op import BaseOp

class TestOp(BaseOp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def test(self, msg):
        return self._database.get_user_by_id(user_id)