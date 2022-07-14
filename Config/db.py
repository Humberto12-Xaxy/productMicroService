from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://user.javafx:INGRID070520@localhost:3307/ufood')

conn = engine.connect()

meta = MetaData()
