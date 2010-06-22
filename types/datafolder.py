import os.path
import config

def getDataFile(*args):
    return os.path.expanduser(os.path.join(config.datafolder,  *args))
