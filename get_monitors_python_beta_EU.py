import datadog
import os
import env

os.environ["DD_API_KEY"] = env.DD_API_KEY_EU
os.environ["DD_APP_KEY"] = env.DD_APP_KEY_EU
monitorID = 237773  # EXAMPLE ID


def fetch_monitors():
    # return datadog.api.Monitor.get_all()
    return datadog.api.Monitor.get(monitorID)


if __name__ == "__main__":
    datadog.initialize(
        api_key=os.environ["DD_API_KEY"],
        app_key=os.environ["DD_APP_KEY"],
        api_host="https://api.datadoghq.eu"
    )

print(fetch_monitors())
