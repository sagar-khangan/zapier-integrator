import ast
import sys
import  time

from adapter.appadapter import *
from handler.apihandler import *
from handler.payloadhandler import *
from testdata import inp

dir_path = os.getcwd()

try:
    cfg = get_config()
    jobid = sys.argv[1]
    data = ast.literal_eval(sys.argv[2])
    data = json.loads(data)
    pid = os.getpid()
    create_logger(jobid)
    info_log("Processing started for JobId {0} at PID {1}".format(jobid, pid))
    info_log("Data Recieved for JobId {0} :: {1} ".format(jobid, data))
    waittime = cfg['api']['waittime']
except Exception as e:
    print e
    pass

try:
    print("Starting new worker .....")

    """get leads from api using key"""
    leads = [inp]

    provider = data["payload"]["provider"]
    api = data['payload']['connection']['api']
    params = data['payload']["connection"]["params"]
    api = create_url(api, params)
    info_log("Url created")
    method = data['payload']['connection']['method']
    info_log("Headers created")
    headers = create_header(data["payload"]["connection"]["headers"])
    auth_headers = create_auth_header(data["payload"]["connection"]["headers"])
    timeout = cfg['api']['timeout']
    """get data of job from mysql api and update status"""

    # jobdetails = get_jobdetails(jobid)
    # update_jobdetails(jobid,cfg['status']['started'])

    for i in leads:

        print("Processing for lead ...")

        """ get lead details from db and update status"""
        info_log("Started process for lead :: {0}".format(i))
        # lead = get_leaddetails(i)
        # update_leaddetails(i,cfg['status']['started'])

        lead = i

        info_log("Payload created for lead :: {0}".format(i))
        payload = payload_resolver(lead, provider)

        # update_leaddetails(i,cfg['status']['processing'])

        response = call_api(api, method, headers, payload)
        info_log("lead {0} inserted into {1}".format(i, provider))

        info_log("Response Code : {0}".format(response.status_code))

        print "Response ....", response.status_code
        
        time.sleep(waittime)

        email = i['email']
        info_log("Checking for lead inserted ....")
        is_exists = is_exist(email, provider, params, headers, auth_headers)
        info_log("Lead inserted :: {0} ".format(is_exists))

        print "Exists ... ", is_exists

        print "completed ..."

    """resposne eror and success"""

    """update to mysql lead status"""

    # update_leaddetails(i,cfg['status']['success'])
    # update_leaddetails(i,cfg['status']['fail'])

    # update_jobdetails(jobid, cfg['status']['completed'])


except Exception as e:
    print e, "worker error"
    error_log("Error in worker for {0}".format(str(e)))
    pass
