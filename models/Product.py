from sqlalchemy import Table
from Config.db import meta, engine

products =Table('saucer', meta, autoload= True, autoload_with=engine)