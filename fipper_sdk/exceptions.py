class FipperException(Exception):
    def __init__(self, message: str):
        self.message = message


class FipperConfigNotFoundException(FipperException):
    def __init__(self):
        super(FipperConfigNotFoundException, self).__init__(message='Config not available')
