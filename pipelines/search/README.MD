# List of indices from ElasticSearch
curl http://localhost:29200/_aliases

# Query 
 curl localhost:29200/estopic/_search | jq


curl -s -i -X PUT -H  "Content-Type:application/json" \
    http://localhost:8083/connectors/sink-elastic-01/config \
    -d '{
            "connector.class": "io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
            "connection.url": "http://elasticsearch7:9200",
            "type.name": "_doc",
            "topics": "sample_topic",
            "key.ignore": "true",
            "schema.ignore": "true"
            }'