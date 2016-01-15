﻿
CREATE TABLE siniestros (

	id SERIAL PRIMARY KEY,
	inspectores varchar(100),
	fecha date,
	hora_llegada time,
	hora_siniestro time,
	calle_1 varchar(150),
	calle_2 varchar(150),
	tipo_arteria_1 varchar(30),
	tipo_arteria_2 varchar(30),
	altura integer,
	v_1 varchar(50),
	v_2 varchar(50),
	v_3 varchar(50),
	v_4 varchar(50),
	fuerza_seguridad varchar(20),
	sistema_salud varchar(10),
	observaciones varchar(2000)
);

CREATE TABLE victimas (

	siniestro_id integer references siniestros(id),
	sexo varchar(5),
	edad integer,
	hospital_deriva varchar(20),
	causa varchar(20)
);





SELECT * FROM siniestros;

SELECT * FROM victimas;

DROP TABLE;

DELETE FROM siniestros;

