import os.path

debug = True
datafolder = "/home/cncfanatics/.pyfa"

def getDataFile(*args):
    return os.path.expanduser(os.path.join(datafolder,  *args))

gamedata_connectionstring = 'sqlite:///' + getDataFile("eve.db")
saveddata_connectionstring = 'sqlite:///' + getDataFile("pyfa.db")