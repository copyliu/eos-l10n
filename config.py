import os.path
debug = True
gamedata_connectionstring = 'sqlite:///' + os.path.expanduser(os.path.join("~", ".pyfa","eve.db"))
saveddata_connectionstring = 'sqlite:///:memory:'
