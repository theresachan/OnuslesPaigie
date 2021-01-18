class Returns:
    count_id = 0

    def __init__(self, product, quantity, reason, remarks):
        Returns.count_id += 1
        self.__user_id = Returns.count_id
        self.__product = product
        self.__quantity = quantity
        self.__reason = reason
        self.__remarks = remarks

    def get_user_id(self):
        return self.__user_id

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def get_reason(self):
        return self.__reason

    def get_remarks(self):
        return self.__remarks

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_product(self, product):
        self.__product = product

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_reason(self, reason):
        self.__reason = reason

    def set_remarks(self, remarks):
        self.__remarks = remarks

