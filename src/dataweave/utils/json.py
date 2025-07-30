class JsonParser:

    def __init__(self, json_dict: dict):
        self.__object = json_dict


    def get_key_unsafe(self, key):
        """
        Method used to value of a specifc key in a dict, if exists. If not exists, the method will raise an error.
        :param key: key
        :return: object value
        """

        return self.__object[key]

    def get_key(self, key: str):
        """
        Method used to value of a specifc key in a dict, if exists.
        :param key: key to select the object
        :return: the value or null
        """

        return self.__object[key] if key in self.__object else None


    def set_key(self, key: str, value):
        """
        Method used write/overwrite an element in a dict.
        :param key: key of the object to overwrite
        :param value: value to overwrite
        :return: the past object, or null
        """

        old_value = self.__object[key] if key in self.__object else None
        self.__object[key] = value

        return old_value

