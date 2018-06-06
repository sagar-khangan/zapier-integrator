import handler.apihandler as ah
import handler.confighandler as ch
import handler.loghandler as lh

cfg = ch.get_config()


def is_exist_hubspot(email, hapkey):
    try:
        lh.info_log("checking lead {0}  ".format(email))
        api = cfg['schema']['hubspot']['api']
        api = api.format(email, hapkey)
        method = cfg['schema']['hubspot']['method']
        timeout = cfg['api']['timeout']
        resp = ah.call_api_timeout(api, method, timeout)
        success_code = cfg['schema']['hubspot']['success']
        failure_code = cfg['schema']['hubspot']['failure']
        if resp.status_code == success_code:
            return True
        elif resp.status_code == failure_code:
            return False
    except Exception as e:
        print e, "hubspot error"
        lh.error_log("Error {0} for {1}".format(str(e), email))
        pass
