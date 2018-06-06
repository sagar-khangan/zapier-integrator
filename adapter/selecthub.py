import handler.apihandler as ah
import handler.confighandler as ch
import handler.loghandler as lh

cfg = ch.get_config()


def is_exist_selecthub(email, hapkey):
    try:
        lh.info_log("checking lead {0}  ".format(email))
        return None
    except Exception as e:
        print e, "selecthub error"
        lh.error_log("Error {0} for {1}".format(str(e), email))
        pass
