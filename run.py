import json
import subprocess
import sys

from kafka import KafkaConsumer

from handler.confighandler import *
from handler.loghandler import *

dir_path = os.getcwd()


def kafka_consumer():
    cfg = get_config()
    kafka_topic = cfg['kafka']['topic']
    kafka_host = cfg['kafka']['host']
    kafka_port = cfg['kafka']['port']
    kafka_groupid = cfg['kafka']['groupid']
    kafka_domain = kafka_host + ":" + str(kafka_port)
    consumer = KafkaConsumer(kafka_topic, group_id=kafka_groupid,
                             bootstrap_servers=[kafka_domain])
    for message in consumer:
        jobid = message.key
        data = json.dumps(message.value)
        info_log("Packet recived with job id :: {0}".format(jobid))
        """ Location of worker.py """
        loc = '{0}\worker.py'.format(dir_path).replace('\\', '/')
        """Spawn worker process"""
        spawn = subprocess.Popen([sys.executable, loc, jobid, data])
        """communicate with worker process"""
        spawn.communicate()
        # print "completed processing for {0}".format(jobid)
        info_log("Processing completed for :: {0}".format(jobid))


if __name__ == "__main__":
    """Start Kafka consumer"""
    print ("Kafka Consumer Started.....")
    create_logger("main")
    kafka_consumer()
