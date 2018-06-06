import json

import handler.apihandler as ah
import handler.confighandler as ch
import handler.loghandler as lh

cfg = ch.get_config()


def is_exist_salesforce(email, header):
    try:
        lh.info_log("checking lead {0}  ".format(email))
        api = cfg['schema']['salesforce']['api']
        api = api.format(email)
        method = cfg['schema']['salesforce']['method']
        timeout = cfg['api']['timeout']
        resp = ah.call_api_timeout(api, method, timeout, header)
        success_code = cfg['schema']['salesforce']['success']
        totalsize = json.loads(resp.text)['totalSize']

        if resp.status_code == success_code and totalsize > 0:
            return True
        else:
            return False

    except Exception as e:
        print e, "salesforce error"
        lh.error_log("Error {0} for {1}".format(str(e), email))
        pass
