DROP TABLE IF EXISTS adres, admin, meterSensor, location, historian;
CREATE TABLE adres (
ID_Adres INT NOT NULL Auto_Increment,
NameOfStreet VARCHAR(255),
NumberOfBuilding INT NOT NULL,
NumberOfFlat INT,
City VARCHAR(255) NOT NULL,
Country VARCHAR(255) NOT NULL,
Province VARCHAR(255),
Postcode VARCHAR(6),
Primary key(ID_Adres)
);

CREATE TABLE admin (
	ID_Admin INT NOT NULL Auto_Increment,
	Name VARCHAR(255),
	Surname VARCHAR(255),
	email VARCHAR(255) CHECK (email like '%@%'),
	NumberOfPhone VARCHAR(9),
	PRIMARY KEY (ID_Admin)
);

CREATE TABLE meterSensor (
	Model VARCHAR(255),
	Medium VARCHAR(255),
	Tolerance INT,
	UnitOfMensurment VARCHAR(255),
	PRIMARY KEY (Model,Medium)
);

CREATE TABLE location (
	ID_Location INT NOT NULL Auto_Increment,
	ID_Adres INT,
	Position INT NOT NULL,
	ID_ADMIN INT,
	ModelOfSensor VARCHAR(255),
	Medium VARCHAR(255),
	Primary KEY (ID_Location),
	Foreign key (ID_Adres) REFERENCES adres(ID_Adres),
	Foreign KEY (ID_ADMIN) REFERENCES admin(ID_Admin),
	Foreign KEY (ModelOfSensor,Medium) REFERENCES meterSensor(Model,Medium)
);

CREATE TABLE historian (
	ID_Historian INT NOT NULL Auto_Increment,
	ID_Location INT,
	timeOfProbe Timestamp,
	Status Enum('OK','NOK') NOT NULL,
	Value FLOAT,
	Primary key (ID_Historian),
	UNIQUE (ID_Location,timeOfProbe),
	Foreign key (ID_Location) REFERENCES location(ID_Location)
);

INSERT INTO adres (NameOfStreet,NumberOfBuilding,City,Country,Postcode)
VALUES ('aleja Adama Mickiewicza',30,'Krakow','Poland','30-059');

INSERT INTO admin (Name,Surname,email,NumberOfPhone)
VALUES ('The','Dukato','The@Dukato.com','123456789');

INSERT INTO meterSensor 
VALUES ('BMP280','Temperature','1%','Celcius');
INSERT INTO meterSensor 
VALUES ('DS18x20','Temperature','1%','Celcius');

INSERT INTO location (ID_Adres,Position,ID_ADMIN,ModelOfSensor,Medium)
VALUES (1,1,1,'BMP280','Temperature');
INSERT INTO location (ID_Adres,Position,ID_ADMIN,ModelOfSensor,Medium)
VALUES (1,2,1,'DS18x20','Temperature');

INSERT INTO historian (ID_Location,timeOfProbe,Status,Value)
VALUES (1,'2008-11-11 13:23:44','OK',4.56);

SELECT * FROM adres