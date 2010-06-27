from sqlalchemy import MetaData,  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .. import datafolder
from .. import config

gamedata_engine = create_engine(,  echo = config.debug)

gamedata_meta = MetaData()
gamedata_meta.bind = gamedata_engine

gamedata_session = sessionmaker(bind=gamedata_engine)()

#saveddata_engine = create_engine("sqlite:///" + datafolder.getDataFile("saved_data.db"), echo = config.debug)

from gamedata import attribute, category, effect, group, icon, item, marketgroup, metagroup