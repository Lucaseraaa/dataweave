
class DatabaseConnectionException(Exception):
    """Generic database connection exception"""
    pass

class ConnectionStringException(DatabaseConnectionException):

    def __init__(self, key: str):
        message = f"Connection string failed. You miss {key} param in the connection string."
        super().__init__(message)
