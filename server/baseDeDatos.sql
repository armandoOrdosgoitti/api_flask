CREATE DATABASE api_flask;
USE api_flask;
CREATE TABLE datos(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    edad int,
    sexo VARCHAR(100),
    nacionaliadad VARCHAR(100),
    profecion VARCHAR(100)
);    