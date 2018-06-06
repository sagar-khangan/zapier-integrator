import yaml

from loghandler import *


def get_config():
    try:

        with open(os.path.abspath("config.yaml"), 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        info_log("Config loaded")
        return cfg

    except Exception as e:
        print e, "onfig handler error"
        error_log("Error in Config handler for {0}".format(str(e)))
        return {}
