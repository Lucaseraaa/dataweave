import psycopg2
from psycopg2 import OperationalError
from dataweave.utils.json import JsonParser
from dataweave.utils.database import create_database_connection_string

class DatabaseConnection:

    def __init__(self, params: dict):

        self.__params: JsonParser = JsonParser(params)
        self.__connection = None

    def __setup_connection(self):
        """
        Method that set up the database connection parameters
        :return:
        """

        database_connection_string = create_database_connection_string(self.__params)

        self.__connection = psycopg2.connect(database_connection_string)


    def test(self):
        """
        Method that test the database connection
        :return: true if the database connection is working, else False
        """

        try:
            self.__setup_connection()
            self.__connection.close()

        except OperationalError as op_error:
            print(op_error)
            return False

        return True



