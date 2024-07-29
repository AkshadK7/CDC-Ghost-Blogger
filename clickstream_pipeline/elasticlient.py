from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200'])

# Search for all documents in an index
result = es.search(index='user-tracker', body={
    'query': {
        'match_all': {}
    }
})

print(result)