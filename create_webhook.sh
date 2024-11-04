#!/bin/bash

# Note: change create to update if you want to update the webhook

# Create Mainframe Webhook
prefect cloud webhook create trace-demo \
    --description "For triggering traceable flows" \
    --template '{ "event": "{{ body.event_name }}", "resource": { "prefect.resource.id": "prefect.webhook.trace-demo", "prefect.resource.name": "prefect.webhook.trace-demo", "trace_id": "{{ body.trace_id }}" } }'
