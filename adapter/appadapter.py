from adapter.hubspot import *
from adapter.salesforce import *
from adapter.selecthub import *
from handler.loghandler import *


def is_exist(email, provider, params=None, headers=None, auth_heaaders=None):
    try:
        is_exist = False
        info_log("Resolving params for {0} ".format(provider))
        if provider.lower() == 'hubspot':
            hapkey = ''
            for i in params:
                if i['key'].lower() == 'hapkey':
                    hapkey = i['value']
            is_exist = is_exist_hubspot(email, hapkey)
        elif provider.lower() == 'salesforce':
            is_exist = is_exist_salesforce(email, auth_heaaders)
        elif provider.lower() == 'selecthub':
            is_exist = is_exist_selecthub(email, auth_heaaders)
        return is_exist
    except Exception as e:
        print e, "app handler error"
        error_log("Error {0} in checking lead {1} on {2} ".format(str(e), email, provider))
        pass
