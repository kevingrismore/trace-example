#!/bin/bash

# Replace <REPLACE-ME> with the actual webhook IDs


# Call Webhook
echo "Emitting kickoff event..."
curl -X POST 'https://api.prefect.cloud/hooks/<REPLACE-ME>' -H "Content-Type: application/json" -d '{
  "event_name": "trace.Trigger",
  "trace_id": "testid123"
}'