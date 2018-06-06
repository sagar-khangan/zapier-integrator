"""

take payload dict from mysql
and convert into mysql compatible schema
anbd return dict

"""
from confighandler import *


def generate_payload_generic(data, provider):
    try:
        payload = {}
        cfg = get_config()
        provider_schema = cfg['schema'][provider]['mapping']
        provider_keys = provider_schema.keys()
        org_keys = cfg['schema']['org']

        for i in org_keys:
            if i in provider_keys:
                payload[provider_schema[i]] = data[i]
        info_log("Payload generated")
        return payload
    except Exception as e:
        print e, "Payload generator error"
        error_log("Error in payload generator call for {0}".format(str(e)))
        return None


def generate_payload_hubspot(data, provider):
    try:
        mapping = generate_payload_generic(data, provider)
        payload = {}
        cfg = get_config()
        provider_schema = cfg['schema'][provider]['native']
        payload['properties'] = []
        for i in provider_schema['properties']:
            for k, v in mapping.iteritems():
                if i['property'] == k:
                    i['value'] = v
                    payload['properties'].append(i)
        info_log("Payload generated")
        return payload
        pass
    except Exception as e:
        print e, "payload error"
        error_log("Error in payload generator call for {0}".format(str(e)))
        return None


def payload_resolver(data, provider):
    try:
        if provider == "hubspot!!":
            payload = generate_payload_hubspot(data, provider)
            return payload
        else:
            payload = generate_payload_generic(data, provider)
            return payload
    except Exception as e:
        return None
