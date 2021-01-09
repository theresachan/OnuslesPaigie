class Entry:
    count_id = 0

    def __init__(self, cost_category, expenses):
        Entry.count_id += 1
        self.__entry_id = Entry.count_id
        self.__cost_category = cost_category
        self.__expenses = expenses

    def get_entry_id(self):
        return self.__entry_id

    def get_cost_category(self):
        return self.__cost_category

    def get_expenses(self):
        return self.__expenses

    def set_user_id(self, entry_id):
        self.__entry_id = entry_id

    def set_cost_category(self, cost_category):
        self.__cost_category = cost_category

    def set_expenses(self, expenses):
        self.__expenses = expenses

