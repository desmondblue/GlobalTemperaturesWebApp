BEGIN;
DROP TABLE IF EXISTS Global_Land_Temperatures_By_City;

CREATE TABLE Global_Land_Temperatures_By_City(

dt INTEGER,
AverageTemperature REAL,
AverageTemperatureUncertainity REAL,
City TEXT,
Country TEXT,
Latitude TEXT,
Longitude TEXT
);
COMMIT;