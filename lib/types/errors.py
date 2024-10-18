class UserDoesNotExist(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidHexColorCode(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ElementDoesNotExist(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
