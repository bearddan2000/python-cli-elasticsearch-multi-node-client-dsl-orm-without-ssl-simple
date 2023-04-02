import logging
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

from database.data import INDEX_NAME
from statements.cls import Statements
from statements.const import currentFuncName
from statements.aggs.const  import *
from statements.query.const  import *

logging.basicConfig(level=logging.INFO)


def print_result(item, server: str, cls:str, func_name: str):
    logging.info("from server {} {} {}: {}".format(server,cls,func_name, str(item)))

class ClientAggs(Statements):

    def __init__(self, server, es:Elasticsearch) -> None:
        self.server=server
        self.es = es

    def refresh_query(self, aggregate: dict, query: dict=None):
        self.es.indices.refresh(index=INDEX_NAME)
        return self.es.search(index=INDEX_NAME, query=query, aggs=aggregate)
            
    def stats_query(self, key, aggregate: dict, func_name: str, subkey: list, query: dict=None):
        collection=self.refresh_query(aggregate, query)
        for s in subkey:
            print_result(collection['aggregations'][key][s], self.server, self.__class__, key+'_'+s+'_'+func_name)

    def normal_query(self, key, aggregate: dict, func_name: str, query: dict=None):
        collection=self.refresh_query(aggregate, query)
        print_result(collection['aggregations'][key]['value'], self.server, self.__class__, key+'_'+func_name)

    def rollup(self, fun_name, query: dict=None):

        aggs_const = [
            AVG_AGGR,
            COUNT_AGGR,
            MAX_AGGR,
            MIN_AGGR,
            SUM_AGGR,
            DISTINCT_AGGR,
            ALL_STATS_AGGR,
            STATS_AGGR,
        ]
   
        i = 0
   
        for k in aggs:
            if '_all_stats' in k:
                self.stats_query(k, aggs_const[i], fun_name, all_stats_subkey, query)
            elif '_stats' in k:
                self.stats_query(k, aggs_const[i], fun_name, all_stats_subkey[:5], query)
            else:
                self.normal_query(k, aggs_const[i], fun_name, query)
            i += 1


    def range_query(self):
        self.rollup(currentFuncName(), RANGE)

    def regex_query(self):
        self.rollup(currentFuncName(), REGEX)

    def must_filter_query(self):
        self.rollup(currentFuncName(), MUST_FILTER)

    def must_not_query(self):
        self.rollup(currentFuncName(), MUST_NOT_FILTER)

    def must_query(self):
        self.rollup(currentFuncName(), MUST)

    def filter_query(self):
        self.rollup(currentFuncName(), FILTER)

    def get_all_query(self):
        self.rollup(currentFuncName())

class DSLAggs(Statements):
    def __init__(self, server, es:Elasticsearch) -> None:
        self.server=server
        self.es = es

    def refresh_query(self, aggregation: Search, query: Search=Search()):
        self.es.indices.refresh(index=INDEX_NAME)
        s = query.using(self.es).index(INDEX_NAME)
        a = aggregation(s)
        return a.execute()
            
    def stats_query(self, key, aggregate: Search, func_name: str, subkey: list, query: Search=Search()):
        collection=self.refresh_query(aggregate, query)
        for s in subkey:
            print_result(collection.aggregations[key][s], self.server, self.__class__, key+'_'+s+'_'+func_name)

    def normal_query(self, key, aggregate: Search, func_name: str, query: Search=Search()):
        collection=self.refresh_query(aggregate, query)
        print_result(collection.aggregations[key]['value'], self.server, self.__class__, key+'_'+func_name)

    def rollup(self, fun_name, query: Search=Search()):

        aggs_const: Search = [
            dsl_average,
            dsl_count,
            dsl_max,
            dsl_min,
            dsl_sum,
            dsl_distinct_count,
            dsl_all_stats,
            dsl_stats,
        ]
        
        i = 0
   
        for k in aggs:
            if '_all_stats' in k:
                self.stats_query(k, aggs_const[i], fun_name, all_stats_subkey, query)
            elif '_stats' in k:
                self.stats_query(k, aggs_const[i], fun_name, all_stats_subkey[:5], query)
            else:
                self.normal_query(k, aggs_const[i], fun_name, query)
            i += 1
            
    def range_query(self):
        self.rollup(currentFuncName(), dsl_range())

    def regex_query(self):
        self.rollup(currentFuncName(), dsl_regex())

    def must_filter_query(self):
        self.rollup(currentFuncName(), dsl_filter())

    def must_not_query(self):
        self.rollup(currentFuncName(), dsl_must_not_filter())
    
    def must_query(self):
        self.rollup(currentFuncName(), dsl_must())

    def filter_query(self):
        self.rollup(currentFuncName(), dsl_filter())

    def get_all_query(self):
        self.rollup(currentFuncName())