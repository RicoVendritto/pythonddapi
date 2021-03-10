import datadog
import os
import env

os.environ["DD_API_KEY"] = env.DD_API_KEY_US
os.environ["DD_APP_KEY"] = env.DD_APP_KEY_US
monitorID = 21298045 # EXAMPLE ID


def fetch_monitors():
    return datadog.api.Monitor.get(monitorID)


if __name__ == "__main__":
    datadog.initialize(
        api_key=os.environ["DD_API_KEY"],
        app_key=os.environ["DD_APP_KEY"],
        host_name="https://api.datadoghq.com"
    )


print(fetch_monitors())
