from datadog import initialize, api
import os
import env

os.environ["DD_API_KEY"] = env.DD_API_KEY_EU
os.environ["DD_APP_KEY"] = env.DD_APP_KEY_EU
monitorID = 237773  # EXAMPLE ID

options = {
    'api_key': os.environ["DD_API_KEY"],
    'app_key': os.environ["DD_APP_KEY"],
    'api_host': "https://api.datadoghq.eu"
}

initialize(**options)


try:
    apiCallResult = api.Monitor.get(monitorID, group_states='all')
    print(apiCallResult)
except:
    print("error")
