from elasticsearch_dsl import Search

SELECT_ALL = {"match_all": {}}

def dsl_range() -> Search:
    return Search().filter("range", id={'gt': 2})

RANGE = {
  "bool": {
    "filter": {"range": {"id": {"gt": 2}}}
  }
}

def dsl_regex() -> Search:
    return Search().query("regexp", color="white*")

REGEX = {
    "bool": {
      "must": {"regexp": { "color": "white*" }}
    }
}

def dsl_must() -> Search:
    return Search().query("match", name="Bruno")

MUST = {
  "bool": {
    "must": [{"match": {"name": "Bruno"}}]
  }
}

def dsl_must_filter() -> Search:
    return Search() \
      .filter("term", color="brown") \
      .query("match", name="Bruno")

MUST_FILTER = {
  "bool": {
    "filter": {"term": {"color": "brown"}},
    "must": [{"match": {"name": "Bruno"}}]
  }
}

def dsl_must_not_filter() -> Search:
    return Search() \
      .filter("term", color="brown") \
      .query("match", name="Bruno") \
      .exclude("term", color="white")

MUST_NOT_FILTER = {
  "bool": {
    "filter": {"term": {"color": "brown"}},
    "must": [{"match": {"name": "Bruno"}}],
    "must_not": [{"term": {"color": "white"}}]
  }
}

def dsl_filter() -> Search:
    return Search() \
      .filter("term", color="brown")

FILTER = {
  "bool": {
    "filter": {"term": {"color": "brown"}}
  }
}