from database import DbStore

class BaseOp(object):
    def __init__(self, **kwargs):
        self._database = DbStore()

    def __enter__(self):
        self.connect()

    def connect(self):
        self._database.connect()

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_value is None:
            self.disconnect(commit=True)
        else:
            self.disconnect(commit=False)

    def disconnect(self, commit):
        self._database.disconnect(commit=commit)