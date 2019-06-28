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

        try:
            db_url = os.environ['db_url']
        except Exception as e:
            self.db_url = "postgres://username:password@localhost:5432/flask-template-db"

        if (environment == 'prod'):
            self.CONFIGPATH = BASE_CONFIGPATH + "ProductionConfig.json"
        else:
            self.CONFIGPATH = BASE_CONFIGPATH + "DefaultConfig.json"
