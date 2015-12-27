
CREATE TABLE siniestros (

	id BIGSERIAL PRIMARY KEY,
	inspectores varchar(100),
	fecha date,
	hora_llegada time,
	calle_1 varchar(150),
	calle_2 varchar(150),
	tipo_arteria_1 varchar(30),
	tipo_arteria_2 varchar(30),
	altura integer,
	v_1 varchar(50),
	v_2 varchar(50),
	v_3 varchar(50),
	v_4 varchar(50)

);

SELECT * FROM siniestros;

DROP TABLE siniestros;