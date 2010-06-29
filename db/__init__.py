from sqlalchemy import MetaData,  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .. import config

class ReadOnlyException(Exception):
    pass

#Method to replace flush with for read-only sessions
def abort_ro():
    raise ReadOnlyException()

gamedata_engine = create_engine(config.gamedata_connectionstring,  echo = config.debug)
gamedata_meta = MetaData()
gamedata_meta.bind = gamedata_engine
gamedata_session = sessionmaker(bind=gamedata_engine, autoflush = False)()
#Make gamedata_session read only
gamedata_session.flush = abort_ro

saveddata_engine = create_engine(config.saveddata_connectionstring, echo = config.debug)
saveddata_meta = MetaData()
saveddata_meta.bind = saveddata_engine
saveddata_session = sessionmaker(bind=saveddata_engine)()

from .gamedata import *
from .saveddata import *