import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

engine = create_engine('postgresql://postgres:postgres@localhost/planilla')
metadata = MetaData(bind=engine)


siniestros = Table('siniestros', metadata, autoload=True)
#victimas = Table('victimas', metadata, autoload=True)


def insert(table, *args):
    conn = engine.connect()
    ins = table.insert().values(args)
    conn.execute(ins)
    conn.close()

#insert(siniestros, 9, 'a', ' ', None, '01:00:00', 'callao', 'santa fe')

#insert(vehiculos, 1, 'BICICLETA')