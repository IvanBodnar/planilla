from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, select, func, dialects
from PyQt4.QtGui import *
from PyQt4 import QtSql

engine = create_engine('postgresql://postgres:postgres@localhost/planilla')
metadata = MetaData(bind=engine)


siniestros = Table('siniestros', metadata, autoload=True)
victimas = Table('victimas', metadata, autoload=True)


def insert_siniestro(table, inspectores, fecha, hora_llegada, calle_1,
           calle_2, tipo_arteria_1, tipo_arteria_2, altura,
           v_1, v_2, v_3, v_4, fuerza_seguridad, sistema_salud,
           total_victimas, homicidio, observaciones):
    conn = engine.connect()
    ins = table.insert().values(inspectores=inspectores, fecha=fecha, hora_llegada=hora_llegada,
                                calle_1=calle_1, calle_2=calle_2, tipo_arteria_1=tipo_arteria_1,
                                tipo_arteria_2=tipo_arteria_2, altura=altura, v_1=v_1, v_2=v_2,
                                v_3=v_3, v_4=v_4, fuerza_seguridad=fuerza_seguridad,
                                sistema_salud=sistema_salud, total_victimas=total_victimas,
                                homicidio=homicidio, observaciones=observaciones)
    conn.execute(ins)
    conn.close()


def insert_victima(table, siniestro_id, sexo, edad, hospital_deriva, causa):
    conn = engine.connect()
    ins = table.insert().values(siniestro_id=siniestro_id, sexo=sexo, edad=edad,
                                hospital_deriva=hospital_deriva, causa=causa)
    conn.execute(ins)
    conn.close()


def connect_qt():
    db = QtSql.QSqlDatabase.addDatabase("QPSQL")
    db.setHostName('localhost')
    db.setPort(5432)
    db.setDatabaseName('planilla')
    db.setUserName('postgres')
    db.setPassword('postgres')
    db.open()
    if not db.open():
        QMessageBox.critical(None, "Database Error", db.lastError().text())
    return True


def max_id():
    conn = engine.connect()
    sel = select([func.max(siniestros.c.id)])
    result = conn.execute(sel)
    return [x for x in result][0][0]


