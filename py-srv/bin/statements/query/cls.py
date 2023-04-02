import logging
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

from database.data import INDEX_NAME
from statements.cls import Statements
from statements.const import currentFuncName
from statements.query.const  import *

logging.basicConfig(level=logging.INFO)

def print_result(collection: list, server: str, cls:str, func_name: str):
    for item in collection:
        logging.info("from server {} {} {}: {}".format(server,cls,func_name, str(item)))

class ClientQuery(Statements):
    def __init__(self, server, es:Elasticsearch) -> None:
        self.server=server
        self.es = es

    def refresh_query(self, query: dict, func_name: str):
        self.es.indices.refresh(index=INDEX_NAME)
        collection=self.es.search(index=INDEX_NAME, query=query)
        print_result(collection['hits']['hits'], self.server, self.__class__, func_name)

    def range_query(self):
        self.refresh_query(RANGE, currentFuncName())

    def regex_query(self):
        self.refresh_query(REGEX, currentFuncName())

    def must_filter_query(self):
        self.refresh_query(MUST_FILTER, currentFuncName())

    def must_not_query(self):
        self.refresh_query(MUST_NOT_FILTER, currentFuncName())

    def must_query(self):
        self.refresh_query(MUST, currentFuncName())

    def filter_query(self):
        self.refresh_query(FILTER, currentFuncName())

    def get_all_query(self):
        self.refresh_query(SELECT_ALL, currentFuncName())

class DSLQuery(Statements):
    def __init__(self, server, es:Elasticsearch) -> None:
        self.server=server
        self.es = es

    def refresh_query(self, func_name: str, query: Search=Search()):
        self.es.indices.refresh(index=INDEX_NAME)
        s = query.using(self.es).index(INDEX_NAME)
        collection=s.execute()
        print_result(collection, self.server, self.__class__, func_name)
    
    def range_query(self):
        self.refresh_query(currentFuncName(), dsl_range())

    def regex_query(self):
        self.refresh_query(currentFuncName(), dsl_regex())

    def must_filter_query(self):
        self.refresh_query(currentFuncName(), dsl_must_filter())

    def must_not_query(self):
        self.refresh_query(currentFuncName(), dsl_must_not_filter())
    
    def must_query(self):
        self.refresh_query(currentFuncName(), dsl_must())

    def aggregate_query(self):
        pass

    def filter_query(self):
        self.refresh_query(currentFuncName(), dsl_filter())

    def get_all_query(self):
        self.refresh_query(currentFuncName())