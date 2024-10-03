CREATE DATABASE CitasMedicas;
USE CitasMedicas;
-- formulario donde el paciente busca una cita
CREATE TABLE formulario (
  `CURP` varchar(20) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  apellido_paterno varchar(20) not null,
	apellido_materno varchar(20) not null,
  `telefono` varchar(15) NOT NULL,
  `fnacimiento` date NOT NULL,
  `fecha` date NOT NULL,
  `hora` time(6) NOT NULL,
  sexo char not null,
  correoe varchar(100),
  `observaciones` varchar(255) NOT NULL,
  id_formulario int auto_increment primary key
);

-- tabla para relacionar empleados
CREATE TABLE empleados(
ID_EMPLEADO int PRIMARY KEY auto_increment,
area varchar(25) not null,
puesto varchar(25) not null
);


-- consultorios para las citas
create table consultorio (
id_consultorio int auto_increment primary key,
consultorio varchar(50) not null,
piso varchar(50) not null,
edificio varchar(50) not null

);


-- tabla para los medicos
create table medicos(
ID_EMPLEADO int,
especialidad varchar(255) not null,
id_consultorio int ,
hora_entrada time ,
hora_salida time,
foreign key (ID_EMPLEADO) references  empleados(ID_EMPLEADO),
foreign key (id_consultorio) references  consultorio(id_consultorio)

);
-- informaicon personal de medicos se relaciona con empleados
CREATE TABLE informacion_personal_empleados(
nombre varchar(25) not null,
apellidop varchar(25) not null,
apellidom varchar (25) not null,
telefono varchar (25) not null,
correoe varchar(50) not null,
ID_EMPLEADO int,
foreign key (ID_EMPLEADO) references  empleados(ID_EMPLEADO)
);
-- personas que entran al sistema
CREATE TABLE usuarios (
`user` varchar (25) not null,
`password` varchar (25) not null,
ID_EMPLEADO int,
tipo_usuario varchar(50) not null,
foreign key (ID_EMPLEADO) references  empleados(ID_EMPLEADO)
);


-- informacion persoonal de pacientes
create table paciente_datos_personales(
id_paciente int primary key auto_increment,
nombre varchar(30) not null,
apellido_paterno varchar(20) not null,
apellido_materno varchar(20) not null,
telefono varchar(15) not null,
correoe varchar(100) not null,
fnacimiento date not null

);
-- direccion de los pacientes
create table direccion_paciente(
id_direccion_paciente int primary key auto_increment,
calle varchar ( 255) not null,
`#numero_de_casa` varchar(25) not null,
CP int not null
);
-- tabla para relacionar la informacion de los pacientes
create table paciente(
id_paciente int,
id_direccion_paciente int,

-- la llave foranea va en las otras tablas para que las otras tablas referencieen esta tabla o que esta tabla referencee las demas tablas?
foreign key (id_paciente) references paciente_datos_personales (id_paciente),
foreign key (id_direccion_paciente) references direccion_paciente(id_direccion_paciente)
);
-- tabla de la cita

create table cita(
id_cita int primary key auto_increment,
id_paciente int,
ID_EMPLEADO int,
fecha datetime not null,
motivo varchar(255),
estado varchar(50), -- con cita, sin cita, pendiente
foreign key (id_cita) references formulario(id_formulario),
foreign key (ID_EMPLEADO) references empleados(ID_EMPLEADO)
);

-- tabla del historial de citas del paciente

CREATE TABLE expediente (
id_expediente int primary key auto_increment,
id_paciente int,
id_cita int,
fecha datetime not null,
diagnostico varchar(255) not null,
tratamiento varchar(255) not null,
observacion varchar(255) not null,

foreign key (id_paciente) references paciente (id_paciente),
foreign key (id_cita) references cita (id_cita)
);


-- cargar 5 registros de prueba
INSERT INTO formulario (CURP, nombre, apellido_paterno, apellido_materno, telefono, fnacimiento, fecha, hora, sexo, correoe, observaciones)
VALUES
  ('ABSP010198000000', 'Juan', 'Pérez', 'García', '8112345678', 
  '1980-01-01', '2023-12-31', '12:00:00', 'M', 'juanperez@correo.com', 'Ninguna'),
  
  ('ABSP020299000000', 'María', 'López', 'González', 
  '8123456789', '1999-02-02', '2023-12-31', '13:00:00', 'F', 'marialopez@correo.com', 'Requiere atención médica'),
  
  ('ABSP030300000000', 'Carlos', 'Rivera', 'Sánchez', 
  '8134567890', '2000-03-03', '2023-12-31', '14:00:00', 'M', 'carlosrivera@correo.com', 'No hay observaciones'),
  
  ('ABSP040401000000', 'Ana', 'Martínez', 'Ramírez', 
  '8145678901', '2001-04-04', '2023-12-31', '15:00:00', 'F', 'anamartinez@correo.com', 'Acude por segunda vez'),
  
  ('ABSP050502000000', 'Luis', 'Hernández', 'Rodríguez',
  '8156789012', '2002-05-05', '2023-12-31', '16:00:00', 'M', 'luishernandez@correo.com', 'Paciente de primer consulta');
select * from formulario;

insert into empleados (area, puesto)
values
  ('Medicina', 'Médico'),
  ('Administración', 'Secretario'),
  ('Enfermería', 'Enfermero'),
  ('Mantenimiento', 'Técnico'),
  ('Laboratorio', 'Analista');
select * from empleados;
insert into consultorio (consultorio, piso, edificio) values
  (101, '1', 'Principal'),
  (203, '2', 'Principal'),
  (305, '3', 'Anexo'),
  (105, '1', 'Principal'),
  (201, '2', 'Principal');
select * from consultorio;
insert into medicos (ID_EMPLEADO, especialidad, id_consultorio, hora_entrada, hora_salida) values
  (1, 'Cardiología', 1, '08:00:00', '16:00:00'),
  (1, 'Pediatría', 2, '17:00:00', '21:00:00'),
  (3, 'Cuidados Intensivos', 3, '07:00:00', '19:00:00'),
  (5, 'Análisis Clínicos', 4, '08:00:00', '16:00:00'),
  (2, 'Administración', 5, '09:00:00', '17:00:00');
  select * from medicos;
insert into informacion_personal_empleados (nombre, apellidop, apellidom, telefono, correoe, ID_EMPLEADO)values
  ('Juana', 'Pérez', 'Garza', '5555555555', 'juan.perez@correo.com', 1),
  ('María', 'Jose', 'González', '1111111111', 'maria.lopez@correo.com', 2),
  ('Carlos', 'Pausini', 'Sánchez', '3333333333', 'carlos.rivera@correo.com', 3),
  ('Ana', 'Loera', 'Ramírez', '4444444444', 'ana.martinez@correo.com', 4),
  ('Luis', 'Hernández', 'Colosio', '5555555555', 'luis.hernandez@correo.com', 5);
select * from informacion_personal_empleados;
insert into usuarios (user, password, ID_EMPLEADO, tipo_usuario)values
  ('jperez', '12345', 1, 'Administrador'),
  ('mlopez', '67890', 2, 'Usuario'),
  ('crivera', 'abcdef', 3, 'Usuario'),
  ('amartinez', 'ghijkl', 4, 'Invitado'),
  ('lhernandez', 'mnopq', 5, 'Usuario');
  
  select * from usuarios;
insert into paciente_datos_personales (nombre, apellido_paterno, apellido_materno, telefono, correoe, fnacimiento)values
    ('Juan', 'Pérez', 'García', '5555555555', 'juan.perez@correo.com', '1980-01-01'),
    ('María', 'López', 'González', '1111111111', 'maria.lopez@correo.com', '1990-02-02'),
    ('Carlos', 'Rivera', 'Sánchez', '3333333333', 'carlos.rivera@correo.com', '1975-05-15'),
    ('Ana', 'Martínez', 'Ramírez', '4444444444', 'ana.martinez@correo.com', '2000-12-25'),
    ('Luis', 'Hernández', 'Rodríguez', '5555555555', 'luis.hernandez@correo.com', '1995-08-10');
  select * from paciente_datos_personales;

insert into direccion_paciente (calle, `#numero_de_casa`, CP)values
    ('Av. Siempre Viva', '123', 12345),
    ('Calle de las Flores', '456', 54321),
    ('Paseo de los Olivos', '789', 12345),
    ('Calle Principal', '100', 54321),
    ('Avenida Central', '200', 12345);
  select * from direccion_paciente;

insert into paciente (id_paciente, id_direccion_paciente) values
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5);
      select * from paciente;

insert into cita (id_paciente, ID_EMPLEADO, fecha, motivo, estado) values
    (1, 1, '2024-04-15 10:00:00', 'Dolor de cabeza intenso', 'Con cita'),
    (2, 2, '2024-04-16 14:30:00', 'Consulta de rutina', 'Con cita'),
    (3, 1, '2024-04-17 09:00:00', 'Fiebre alta y tos', 'Con cita'),
    (4, 3, '2024-04-18 16:00:00', 'Dolor de rodilla tras caída', 'Con cita'),
    (5, 2, '2024-04-19 11:00:00', 'Solicitar receta para anticonceptivos', 'Con cita');
  select * from cita;

insert into expediente (id_paciente, id_cita, fecha, diagnostico, tratamiento, observacion)values
    (1, 1, '2024-04-15 10:00:00', 'Migraña', 'Analgésicos y reposo', 'Paciente sensible a la luz y el ruido'),
    (2, 2, '2024-04-16 14:30:00', 'Buen estado de salud', 'Seguimiento en 6 meses', 'No se encontraron anomalías'),
    (3, 3, '2024-04-17 09:00:00', 'Gripe común', 'Antivirales y reposo', 'Se recomienda aumentar el consumo de líquidos'),
    (4, 4, '2024-04-18 16:00:00', 'Esguince de rodilla', 'Faja elástica y fisioterapia', 'Evitar cargar peso en la pierna afectada'),
    (5, 5, '2024-04-19 11:00:00', 'Salud reproductiva normal', 'Prescripción de anticonceptivos', 'Próxima cita en 3 meses');
      select * from expediente;
