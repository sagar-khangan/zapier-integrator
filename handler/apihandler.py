"""

call a rest api

"""
import json

import requests

from loghandler import *


def call_api(url, method, headers=None, data=None):
    try:
        if method == "GET":
            response = requests.request(method, url, headers=headers)
        else:
            response = requests.request(method, url, data=str(
                json.dumps(data)), headers=headers)
        info_log("response" + response.text + str(response.status_code) + str(response))
        return response
    except Exception as e:
        print e, "API call error"
        error_log("Error in api call for {0}".format(str(e)))
        return None


def call_api_timeout(url, method, timeout, headers=None, data=None):
    try:
        if method == "GET":
            response = requests.request(method, url, timeout=timeout, headers=headers, )
        else:
            response = requests.request(method, url, timeout=timeout, data=str(
                json.dumps(data)), headers=headers)
        info_log("response" + response.text + str(response.status_code) + str(response))
        return response
    except Exception as e:
        print e, "API call error"
        error_log("Error in api call for {0}".format(str(e)))
        return None


def create_header(heads):
    try:
        headers = {}
        for i in heads:
            if i['key'].lower() != 'authorization':
                headers[i['key']] = i['value']
        info_log("header created")
        return headers
    except Exception as e:
        print e, "header call error"
        error_log("Error in head creator for {0}".format(str(e)))
        return {}


def create_auth_header(heads):
    try:
        headers = {}
        for i in heads:
            headers[i['key']] = i['value']
        info_log("header created")
        return headers
    except Exception as e:
        print e, "header call error"
        error_log("Error in head creator for {0}".format(str(e)))
        return {}


def create_url(url, params):
    try:
        if len(params) > 0:
            url += "?"
            for i in params:
                url += "{0}={1}&".format(i['key'], i['value'])
            url = url[:len(url) - 1]
        info_log("url created")
    except Exception as e:
        error_log("Error in url creator for {0}".format(str(e)))
    return url
