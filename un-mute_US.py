import requests
import env

host_name = "host_name"
DD_API_KEY = env.DD_API_KEY_US
DD_APP_KEY = env.DD_APP_KEY_US
cycle = 1

header = {
    "Content-Type": "application/json",
    "DD-API-KEY": DD_API_KEY,
    "DD-APPLICATION-KEY": DD_APP_KEY
}

data = {
    "message": "Downtime triggered by script",
    "override": True,
    "end": 1630011353
}

## GET AN OVERVIEW OF ALL YOUR HOSTS TO POPULATE host_name VARIABLE
# response = requests.get(
#     "https://api.datadoghq.com/api/v1/hosts", headers=header)
# print(response.content)

while 1:
    print(cycle)
    response = requests.post(
        f'https://api.datadoghq.com/api/v1/host/{host_name}/mute', headers=header, json=data)
    print("mute")
    print(response.content)
    print(response.status_code)
    if response.status_code == 200:
        response = requests.post(
            f'https://api.datadoghq.com/api/v1/host/{host_name}/unmute', headers=header)
        print("unmute")
        print(response.content)
        print(response.status_code)
    else:
        break
    cycle += 1
