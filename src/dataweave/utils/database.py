from dataweave.utils.json import JsonParser
from dataweave.exceptions.database_connection_exceptions import ConnectionStringException

def create_database_connection_string(params: JsonParser) -> str:
    """
    Function that creates a database connection string, using json params
    :return:
    """

    try:
        connection_string = f"postgresql://{params.get_key_unsafe('user')}:{params.get_key_unsafe('password')}@{params.get_key_unsafe('host')}:{params.get_key_unsafe('port')}/{params.get_key_unsafe('database')}"
    except KeyError as missed_key:
        raise ConnectionStringException(str(missed_key))

    return connection_string