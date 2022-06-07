# Ejemplo de inicio de sesión

Se muestra el inicio de sesión de forma segura y de forma no segura utiilzando SQL Injection.

## Instrucciones

### 1. Instalar python3

```bash
$ sudo apt-get install python3
```

### 2. Instalar pip3

```bash
$ sudo apt-get install python3-pip
```

### 3. Instalar dependencias

Para este proyecto se utilizará web.py con web Framework.

```bash
$ pip3 install -r requirements.txt
```

### 4. Crear la base de datos y tabla usuarios

Para este proyecto se utilizará una base de datos llamada `usuarios.sqlite`, y se utilza SQLite3.

### 5. Crear el script de la base de datos

Crear un script de la base de datos de nombre `usuarios.sql` con el siguiente contenido:

```sql
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
```

### 6. Crear la base de datos

```bash
$ sqlite3 usuarios.sql
```


### 7. Correr el script de la base de datos

```bash
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite>.read usuarios.sql
```

### 8. Ejectuar la app

```bash
$ python3 app.py
```

### 9. Abrir el navegador

```bash
http://localhost:8080
```

### 10. Iniciar sesión

    * Email: admin@email.com
    * Contraseña: admin

### 11. Probar la seguridad de la aplicación

En este ejemplo se utilza SQL Injection para probar la seguridad de la aplicación.

    * Email: admin@email.com'--
    * Contraseña: misupercontraseña

**Nota:** cuando las consultas que se realizan concantenan los caracteres que se ingresan, el sistema es vulnerable a SQL Injection.

```bash
result = cursor.execute(
    "select count(usuarios.uid) as auth from usuarios where usuarios.email='"
    + email
    + "' and usuarios.password='"
    + password
    + "' and usuarios.status='activo';"
)
```

**Nota:** cuando las consultas se realizan utilizando parámentros, el sistema se protege contra SQL Injection.

```bash
result = cursor.execute(
    "select count(usuarios.uid) as auth from usuarios where usuarios.email=? and usuarios.password=? and usuarios.status='activo';",
    (email, password),
)
```
---
## Notas

Una primer forma de validar los valores, es directamente desde HTML5 utilizando el tipo correcto para el campo. En el ejemplo siguiente se usa un input de tipo **text** para el campo **email** y **password**, lo que no permite validar los valores.

```html
<form action="" method="POST">
    <label for="email">Email</label>
    <input type="text" name="email" value="admin@email.com">
    <br>
    <label for="password">Password</label>
    <input type="text" required name="password" value="admin">
    <br>
    <input type="submit" value="Iniciar sesion">
</form>
```

En este ejemplo se utiliza un input de tipo **email** para el campo **email**, y el tipo **password** para el campo **password**, lo que permite validar los valores, y no permite que se ingresen caracteres no permitidos.

```html
<form action="" method="POST">
    <label for="email">Email</label>
    <input type="email" name="email" value="admin@email.com">
    <br>
    <label for="password">Password</label>
    <input type="password" required name="password" value="admin">
    <br>
    <input type="submit" value="Iniciar sesion">
</form>
```


### 12. Probar la seguridad de la aplicación

Utilizar curl para validar el inicio de sesión.

    * Email: admin@email.com
    * Contraseña: admin

```bash
curl -X POST -F 'email=admin@email.com' -F 'password=admin' http://localhost:8080/inicio_sesion_seguro
```

Resultado:
```bash
303 See Other
```

```bash
curl -X POST -F 'email=admin@email.com' -F 'password=admin' http://localhost:8080/inicio_sesion_inseguro
```

Resultado:

```bash
303 See Other
```

Utilizar curl para validar el inicio de sesión implamentando SQL Injection.

    * Email: admin@email.com'--
    * Contraseña: admin

```bash
curl -X POST -F "email=admin@email.com'--" -F 'password=misupercontraseña' http://localhost:8080/inicio_sesion_inseguro
```


Resultado:

```bash
303 See Other
```


```bash
curl -X POST -F "email=admin@email.com'--" -F 'password=misupercontraseña' http://localhost:8080/inicio_sesion_seguro
```

Resultado:

```html
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Ejemplos de inicio de sesion</title>
    <link rel="stylesheet" href="../static/css/stylesheet.css">
    <meta name="description" content="Ejemplos de inicio de sesion">
</head>

<h1>Incio de sesion seguro</h1>

<p>Verifique usuario y contraseña</p>

<form action="" method="POST">
    <label for="email">Email</label>
    <input type="text" name="email" value="admin@email.com">
    <br>
    <label for="password">Password</label>
    <input type="text" required name="password" value="admin">
    <br>
    <input type="submit" value="Iniciar sesion">
</form>

    </div>
</body>

</html>
```
