from sqlalchemy import MetaData,  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .. import datafolder
from .. import config

engine = create_engine('sqlite:///' + datafolder.getDataFile("eve.db"),  echo = config.debug)

meta = MetaData()
meta.bind = engine

Session = sessionmaker(bind=engine)

base = declarative_base()

import attribute, category, effect, group, icon, item, marketgroup, metagroup
from queries import getVariations, getItem, searchItems