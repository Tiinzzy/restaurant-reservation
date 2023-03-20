class MenuItems:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__category = None
        self.__price = None
        self.__description = None

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_category(self, category):
        self.__category = category

    def get_category(self):
        return self.__category

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description

    def to_string(self):
        return str(self.__id) + ', ' + str(self.__name) + ', ' + str(self.__category) + ', ' + str(
            self.__price) + ', ' + str(self.__description)
