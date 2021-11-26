from __future__ import print_function
from ctypes import sizeof
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint
import json
import re
from dotenv import load_dotenv
import os


load_dotenv()

def get_alerts():
    """gets the alerts and returns an array of them """
    alerts = api_instance.get_alert_list(size=3000)
    alerts = alerts.to_dict()
    return alerts

def alerts_to_json(alerts):
    """spits out alerts to a json file specified in a directory in .env"""
    filepath = os.getenv("JSON_PATH")
    with open(filepath, 'w') as fp:
        json.dump(alerts, fp)

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = os.getenv("COMPANY")
configuration.access_id = os.getenv("ACCESS_ID")
configuration.access_key = os.getenv("ACCESS_KEY")

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))


if __name__ == "__main__":
    alarms = get_alerts()
    alerts_to_json(alarms)