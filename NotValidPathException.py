class NotValidPathException(Exception):
    def __init__(self, message="Invalid path provided"):
        super().__init__(message)