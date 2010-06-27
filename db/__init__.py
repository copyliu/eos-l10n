from sqlalchemy import MetaData,  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .. import datafolder
from .. import config

gamedata_engine = create_engine(config.gamedata_connectionstring,  echo = config.debug)
gamedata_meta = MetaData()
gamedata_meta.bind = gamedata_engine
gamedata_session = sessionmaker(bind=gamedata_engine)()

saveddata_engine = create_engine(config.saveddata_connectionstring, echo = config.debug)
gamedata_meta = MetaData()
gamedata_meta.bind = gamedata_engine
gamedata_session = sessionmaker(bind=gamedata_engine)()

from gamedata import attribute, category, effect, group, icon, item, marketgroup, metagroup