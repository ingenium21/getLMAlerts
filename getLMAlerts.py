from __future__ import print_function
from ctypes import sizeof
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint
import json
import re
from dotenv import load_dotenv

load_dotenv()

def get_alerts():
    """gets the alerts and returns an array of them """
    alerts = api_instance.get_alert_list(size=3000)
    alerts = alerts.to_dict()
    alerts = alerts["items"]
    return alerts

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = COMPANY
configuration.access_id = ACCESS_ID
configuration.access_key = ACCESS_KEY

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))


if __name__ == "__main__":
    alarms = get_alerts()
    pprint(alarms[0])