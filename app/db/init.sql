 -- Crea la base de datos
 CREATE DATABASE IF NOT EXISTS mydatabase;
 USE mydatabase;

 -- Crea una tabla
 CREATE TABLE usuarios (
 id_usuario INT AUTO_INCREMENT PRIMARY KEY,
 nombre VARCHAR(50),
 apellido VARCHAR(50)
 );

 -- Inserta valores por defecto en tabla usuarios
INSERT INTO usuarios (nombre, apellido) VALUES ('Juan','Alvarez');
INSERT INTO usuarios (nombre, apellido) VALUES ('Marta','Rodriguez');
INSERT INTO usuarios (nombre, apellido) VALUES ('Pedro','Seminario');
INSERT INTO usuarios (nombre, apellido) VALUES ('Luis','Garcia');
INSERT INTO usuarios (nombre, apellido) VALUES ('Karina','Almarales');
INSERT INTO usuarios (nombre, apellido) VALUES ('Andrea','Aybar');
INSERT INTO usuarios (nombre, apellido) VALUES ('Angel','De la Torre');
INSERT INTO usuarios (nombre, apellido) VALUES ('Julia','Aponte');
INSERT INTO usuarios (nombre, apellido) VALUES ('Domingo','Suarez');
INSERT INTO usuarios (nombre, apellido) VALUES ('Miguel','Guillen');
INSERT INTO usuarios (nombre, apellido) VALUES ('Maria','Rojas');

-- Crear la tabla de asignaturas
CREATE TABLE asignaturas (
  id_asignatura INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(60),
  descripción TEXT,
  id_usuario INT,
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- Inserta valores por defecto en tabla Asignaturas
INSERT INTO asignaturas (id_asignatura, nombre, descripcion) VALUES ('1','Programacion','asignatura para maestria Bigdata','1');
INSERT INTO asignaturas (id_asignatura, nombre, descripcion) VALUES ('2','Cloud','asignatura para maestria Bigdata','1');
INSERT INTO asignaturas (id_asignatura, nombre, descripcion) VALUES ('3','Estadistica','asignatura para maestria Bigdata','1');