from sqlalchemy import Integer, String, Table, Column
from config.db import meta, engine

productos = Table("productos", meta, 
    Column("id", Integer, primary_key=True),
    Column("ref", Integer), 
    Column("name", String(255)),
    Column("price", Integer),
    Column("stock", Integer))

meta.create_all(engine)
