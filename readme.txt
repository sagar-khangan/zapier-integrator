* Steps to start *

- Stark Zookeper
- Start Kafka
- Start kafka producer
- python run.py

* Changes required *

- configuration in config.yaml
- add db api in dbhandler



* Code Documentation *

- run.py  : Starting file to poll Kafka queue and spawn a new worker for a job
- worker.py : starting file for a worker, to read data from queue , get lead data from apis, create lead into marketing automation tool and cehck if lead is created or not and updates status
              through api.
- config.yaml : configuration should be written in this file.
- handler : generic handlers for handling logging, api call, payload , db apis and configuration
- adapter : create adapter for marketing automation tool and logoc to call that in appadapter.py  , customize adapters according to mapping


 * Flow *

- Run.py polls kafka queue
- New job reciveed
- Spawn a new process worker.py with job data
- worker.py initialises configuration.
- creates payload , header, url , params
- call db api to get lead data
- call marketing automation api to dump lead
- call api to check if lead created or not.
- updates status in db api

* kafka packet format *

# zapier

# hubspot
# 456:{"payload": {"leads": [1, 2, 3],"provider":"hubspot","connection": {"api":"<zap webhook>","method": "POST","params": [{"key":"hapkey","value":"demo"}],"headers": [{"key":"content-type","value":"application/json"},{"key":"cache-control","value":"no-cache"}]}}}

# salesforce
# 456:{"payload": {"leads": [1, 2, 3],"provider":"salesforce","connection": {"api":"<zap webhook>","method": "POST","params": [],"headers": [{"key":"content-type","value":"application/json"},{"key":"cache-control","value":"no-cache"},{"key":"Authorization","value":"Bearer <SFDC APP TOKEN>"}]}}}

* Zapier *

- create zap
- trigger would be webhook
- action - marketing automation tool
- map fields
- connect to account where leads are to be created


* SFDC *

- dev account
-- create connected app - to get consumerkey and consumer secret(client)

- professional account - for profile
--enable api
--reset security token

- generate auth token (for this accoutn lead will be created and link this account to zapier
--curl -X POST \
  https://<instance>.salesforce.com/services/oauth2/token \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&client_id=<consumer key for connected app>&client_secret=<consumer secret for connected app>&username=<username of account >&password=<password+secret token for account>'

