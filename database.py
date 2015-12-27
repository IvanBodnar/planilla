from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

engine = create_engine('postgresql://postgres:postgres@localhost/planilla')
metadata = MetaData(bind=engine)


siniestros = Table('siniestros', metadata, autoload=True)
#victimas = Table('victimas', metadata, autoload=True)


def insert(table, inspectores, fecha, hora_llegada, calle_1,
           calle_2, tipo_arteria_1, tipo_arteria_2, altura,
           v_1, v_2, v_3, v_4, fuerza_seguridad, sistema_salud):
    conn = engine.connect()
    ins = table.insert().values(inspectores=inspectores, fecha=fecha, hora_llegada=hora_llegada,
                                calle_1=calle_1, calle_2=calle_2, tipo_arteria_1=tipo_arteria_1,
                                tipo_arteria_2=tipo_arteria_2, altura=altura, v_1=v_1, v_2=v_2,
                                v_3=v_3, v_4=v_4, fuerza_seguridad=fuerza_seguridad,
                                sistema_salud=sistema_salud)
    conn.execute(ins)
    conn.close()

#insert(siniestros, 9, 'a', ' ', None, '01:00:00', 'callao', 'santa fe')

#insert(vehiculos, 1, 'BICICLETA')