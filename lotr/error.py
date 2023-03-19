class CustomError(Exception):
    """
    custom error class, can be extended for other errors
    """

    def __init__(self, message=None) -> None:
        super(CustomError, self).__init__(message)

        self.message = message

    def __str__(self) -> str:
        msg = self.message or ""
        return msg

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(message={str(self)})"
