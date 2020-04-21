## Snotel data pipeline

Performing streams analysis

# 
curl -i -X POST -H  http://localhost:8083/connectors/ -d @connectors/snowpack_connector.json

Delete a connector
curl -X DELETE localhost:8083/connectors/customers-connector/product

# Console consumer
confluent local consume dbserver.inventory.customer -- --value-format avro --from-beginning --property print.key=true

# List the topics 
kafka-topics --list --zookeeper localhost:2181


# list all schema in psql
SELECT schema_name FROM information_schema.schemata



