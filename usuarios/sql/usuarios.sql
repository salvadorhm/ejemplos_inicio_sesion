.headers ON

DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios (
  uid INTEGER PRIMARY KEY AUTOINCREMENT,
  email varchar(32) NOT NULL,
  password varchar(32) NOT NULL,
  nombre varchar(50) NOT NULL,
  primer_apellido varchar(50) NOT NULL,
  segundo_apellido varchar(50) NOT NULL,
  rol varchar(50) CHECK(rol IN ('administrador', 'usuario')) NOT NULL,
  status varchar(50) CHECK(status IN ('activo', 'inactivo')) NOT NULL,
  timestamp TIMESTAMP DEFAULT (datetime('now','localtime'))
 );

CREATE UNIQUE INDEX usuarios_email ON usuarios (email);

INSERT INTO usuarios (email, password, nombre, primer_apellido, segundo_apellido, rol, status) VALUES
('admin@email.com', '21232f297a57a5a743894a0e4a801fc3', 'Admin nombre', 'admin primer', 'admin segundo', 'administrador', 'activo');

INSERT INTO usuarios (email, password, nombre, primer_apellido, segundo_apellido, rol, status) VALUES
('user@email.com', 'ee11cbb19052e40b07aac0ca060c23ee', 'User nombre', 'user primer', 'user segundo', 'usuario', 'activo');

SELECT * FROM usuarios;
