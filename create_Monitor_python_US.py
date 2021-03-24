from datadog import initialize, api
import os
import env

os.environ["DD_API_KEY"] = env.DD_API_KEY_US
os.environ["DD_APP_KEY"] = env.DD_APP_KEY_US

options = {
    'api_key': os.environ["DD_API_KEY"],
    'app_key': os.environ["DD_APP_KEY"]
}

initialize(**options)

monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 20
}

tags = ["test:richard", "app:webserver", "frontend"]

try:
    apiResult = api.Monitor.create(
        type="metric alert",
        query="avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
        name="# Bytes received on host0",
        message="We may need to add web hosts if this is consistently high.",
        tags=tags,
        options=monitor_options)
    print(apiResult)
except:
    print("Error")
