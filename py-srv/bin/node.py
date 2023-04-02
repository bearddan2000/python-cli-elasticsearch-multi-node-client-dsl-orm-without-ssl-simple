import logging
from typing import Any, Dict
from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections

from database.data import DOC
from statements.cls import Statements
from statements.query.cls import ClientQuery, DSLQuery
from statements.aggs.cls import ClientAggs, DSLAggs

logging.basicConfig(level=logging.INFO)

class Cluster():
    def __init__(self) -> None:
        self.hive = [
            Node("es1"),
            Node('es2'),
            Node('es3')
        ]

    def range_query(self):
        for node in self.hive:
            node.range_query()
    
    def regex_query(self):
        for node in self.hive:
            node.regex_query()
    
    def must_query(self):
        for node in self.hive:
            node.must_query()

    def must_not_query(self):
        for node in self.hive:
            node.must_not_query()
    
    def must_filter_query(self):
        for node in self.hive:
            node.must_filter_query()
    
    def filter_query(self):
        for node in self.hive:
            node.filter_query()
    
    def get_all_query(self):
        for node in self.hive:
            node.get_all_query()
    
class Node():

    def __init__(self,server='elasticsearch') -> None:
        self.server = server
        conn = ElasticsearchProxy(server)
        self.es = conn.connect()
        logging.info(self.es.ping())
        self.seed()
        self.query: Statements = [
            ClientQuery(self.server, self.es),
            DSLQuery(self.server, self.es),
            ClientAggs(self.server, self.es),
            DSLAggs(self.server, self.es)
        ]

    def seed(self):
        for record in DOC:
            record.save()
            #resp=self.es.index(index=INDEX_NAME, id="0", document=record)
        logging.info("from {} seed: {} saved".format(self.server, len(DOC)))

    def range_query(self):
        for s in self.query:
            s.range_query()
    
    def regex_query(self):
        for s in self.query:
            s.regex_query()

    def must_not_query(self):
        for s in self.query:
            s.must_not_query()

    def must_query(self):
        for s in self.query:
            s.must_query()
    
    def must_filter_query(self):
        for s in self.query:
            s.must_filter_query()
    
    def filter_query(self):
        for s in self.query:
            s.filter_query()

    def get_all_query(self):
        for s in self.query:
            s.get_all_query()

class ElasticsearchProxy:
    """Proxy for Elasticsearch connection that works with Flask.

    Documentation for Elasticseach:
      https://elasticsearch-py.readthedocs.io

    Documentation for Elasticseach DSL:
      https://elasticsearch-dsl.readthedocs.io
    """

    def __init__(self, server):
        self.server = server

    def connect(self) -> Elasticsearch:

        host = self.server
        if not host:
            raise RuntimeError(
                'Cannot connect to elastic search without a host')

        options: Dict[str, Any] = {
            'hosts': [host],
        }

        username = 'elasticsearch'
        password = 'changeme'

        if username and password:
            options['http_auth'] = (username, password)

        timeout = 10
        if timeout is not None:
            options['timeout'] = timeout

        return connections.create_connection(**options)
