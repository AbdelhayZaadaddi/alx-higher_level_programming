-- CREATES DATABSE hbtn_0d_usa AND THE TABLE cities
-- CITIES DESCRIPTION
-- ID INT UNIQUE AUTO GENREATE NOT NULL
-- STATE ID INT CANT BE NULL FOREIGN KEY THE REFRENCES TO ID OF THE STATE TABLE
-- NAME VARCHAR NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (satte_id) REFERENCES states(id)
);