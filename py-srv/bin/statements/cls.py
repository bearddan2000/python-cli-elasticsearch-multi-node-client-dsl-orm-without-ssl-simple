# This is builtin lib; no requirement needed
from abc import ABC

class Statements(ABC):

    def range_query(self):
        pass

    def regex_query(self):
        pass

    def must_filter_query(self):
        pass

    def must_not_query(self):
        pass

    def must_query(self):
        pass

    def filter_query(self):
        pass

    def get_all_query(self):
        pass