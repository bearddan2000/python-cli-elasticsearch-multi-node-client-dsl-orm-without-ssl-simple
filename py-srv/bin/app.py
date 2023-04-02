from node import Cluster

es_node = Cluster()
es_node.range_query()
es_node.regex_query()
es_node.must_not_query()
es_node.must_query()
es_node.must_filter_query()
es_node.filter_query()
es_node.get_all_query()