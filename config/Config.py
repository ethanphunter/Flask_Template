import os

BASE_CONFIGPATH = "./config/"

class Config(object):
    """ Determines which config to use at runtime """

    def __init__(self):
        super(Config, self).__init__()
        try:
            environment = os.environ['env']
        except Exception as e:
            environment = 'dev'
        if (environment == 'prod'):
            self.CONFIGPATH = BASE_CONFIGPATH + "ProductionConfig.json"
        else:
            self.CONFIGPATH = BASE_CONFIGPATH + "DefaultConfig.json"
