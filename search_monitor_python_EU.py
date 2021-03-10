from datadog import initialize, api
import env

monitorID = 237773  # EXAMPLE ID

options = {
	'api_key': env.DD_API_KEY_EU,
	'app_key': env.DD_APP_KEY_EU,
    'api_host': "https://api.datadoghq.eu"
}

initialize(**options)

# Search monitors
outputAPI = api.Monitor.search(query="id:237773")
print(outputAPI)

# Examples of possible query parameters:
# api.Monitor.search(query="id:7100311")
# api.Monitor.search(query="title:foo metric:system.core.idle status:Alert")