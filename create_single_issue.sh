#!/bin/bash
# Helper script to create a single issue using GitHub REST API

TITLE="$1"
LABELS="$2"
BODY="$3"
REPO="Merlissa09/ClassCrawler"

# Create JSON payload
JSON_PAYLOAD=$(jq -n \
  --arg title "$TITLE" \
  --arg body "$BODY" \
  --arg labels "$LABELS" \
  '{
    title: $title,
    body: $body,
    labels: ($labels | split(","))
  }')

# Create issue using GitHub API
RESPONSE=$(curl -s -w "\nHTTP_STATUS:%{http_code}" \
  -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Content-Type: application/json" \
  -d "$JSON_PAYLOAD" \
  "https://api.github.com/repos/$REPO/issues")

# Extract status code
HTTP_STATUS=$(echo "$RESPONSE" | grep "HTTP_STATUS:" | cut -d: -f2)
BODY_RESPONSE=$(echo "$RESPONSE" | sed '/HTTP_STATUS:/d')

if [ "$HTTP_STATUS" = "201" ]; then
  echo "✓ Successfully created: $TITLE"
  echo "$BODY_RESPONSE" | jq -r '.html_url'
  exit 0
else
  echo "✗ Failed to create: $TITLE"
  echo "Status: $HTTP_STATUS"
  echo "$BODY_RESPONSE" | jq -r '.message // .'
  exit 1
fi
