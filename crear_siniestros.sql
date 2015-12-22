
CREATE TABLE siniestros (

	id BIGSERIAL PRIMARY KEY,
	inspectores varchar(100),
	fecha date,
	hora_llegada time,
	calle_1 varchar(150),
	calle_2 varchar(150),
	altura integer

);

SELECT * FROM siniestros;

DROP TABLE siniestros;