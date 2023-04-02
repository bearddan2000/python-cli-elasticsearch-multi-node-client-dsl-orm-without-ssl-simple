from elasticsearch_dsl import Search

aggs = [
    '_avg', '_count', '_max',
    '_min', '_sum', '_distinct_count',
    '_all_stats', '_stats'
]

all_stats_subkey = [
    'count', 'sum', 'avg', 
    'min', 'max', "sum_of_squares", 
    "variance", "std_deviation"
]

def dsl_average(s: Search) -> Search:
    s.aggs.metric('_avg', 'avg', field='height')
    return s

AVG_AGGR = {
  "_avg": {
    "avg": {"field": "height" }
  }
}

def dsl_count(s: Search) -> Search:
    s.aggs.metric('_count', 'value_count', field='id')
    return s

COUNT_AGGR = {
  "_count": {
    "value_count": {"field": "id" }
  }
}

def dsl_max(s: Search) -> Search:
    s.aggs.metric('_max', 'max', field='height')
    return s

MAX_AGGR = {
  "_max": {
    "max": {"field": "height" }
  }
}

def dsl_min(s: Search) -> Search:
    s.aggs.metric('_min', 'min', field='height')
    return s

MIN_AGGR = {
  "_min": {
    "min": {"field": "height" }
  }
}

def dsl_sum(s: Search) -> Search:
    s.aggs.metric('_sum', 'sum', field='height')
    return s

SUM_AGGR = {
  "_sum": {
    "sum": {"field": "height" }
  }
}

def dsl_distinct_count(s: Search) -> Search:
    s.aggs.metric('_distinct_count', 'cardinality', field='height')
    return s

DISTINCT_AGGR = {
    "_distinct_count":{
      "cardinality":{"field":"height"}
    }
}

def dsl_stats(s: Search) -> Search:
    s.aggs.metric('_stats', 'stats', field='height')
    return s

STATS_AGGR = {
    "_stats" : { "stats" : { "field" : "height" } }
}

def dsl_all_stats(s: Search) -> Search:
    s.aggs.metric('_all_stats', 'extended_stats', field='height')
    return s

ALL_STATS_AGGR = {
    "_all_stats" : { "extended_stats" : { "field" : "height" } }
}