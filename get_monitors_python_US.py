from datadog import initialize, api
import os
import env

os.environ["DD_API_KEY"] = env.DD_API_KEY_US
os.environ["DD_APP_KEY"] = env.DD_APP_KEY_US
monitorID = 21298045 # EXAMPLE ID

options = {
    'api_key': os.environ["DD_API_KEY"],
    'app_key': os.environ["DD_APP_KEY"]
}

initialize(**options)

# Get a monitor's details
apiCallResult = api.Monitor.get(monitorID, group_states='all')

# print(api.Monitor.get_all())
print(apiCallResult)
