#!/bin/bash

# Wait for Elasticsearch to be up and running
until curl -s http://elasticsearch01:9200/_cluster/health | grep '"status":"green"' > /dev/null; do
  echo "Waiting for Elasticsearch to start..."
  sleep 5
done

echo "Elasticsearch is up. Performing reroute..."

# Perform reroute
curl -X POST "http://elasticsearch01:9200/_cluster/reroute" -H 'Content-Type: application/json' -d'
{
  "commands": [
    {
      "allocate_empty_primary": {
        "index": "user-tracker",
        "shard": 0,
        "node": "es02",
        "accept_data_loss": true
      }
    },
    {
      "allocate_replica": {
        "index": "user-tracker",
        "shard": 1,
        "node": "es03"
      }
    }
  ]
}
'
