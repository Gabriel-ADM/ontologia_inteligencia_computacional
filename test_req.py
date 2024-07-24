import requests
import json

# Define the SWISH endpoint
swish_url = "https://swish.swi-prolog.org/p/TUpNKYFR.pl"  # Adjust this URL based on your SWISH setup

# Define the Prolog query
prolog_query = """
generate_report('com_implante', 'com_tomossintese', 'sem_limitacao', Relatorio).
"""

# Prepare the JSON payload
# payload = json.dumps({'query': prolog_query})
payload = {"query": prolog_query}

# Set headers to indicate JSON content
headers = {"Content-Type": "application/json"}

# Send the query to SWISH
response = requests.post(swish_url, json=payload, headers=headers)

print(json.dumps(response.json(), indent=4))
