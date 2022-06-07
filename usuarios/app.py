import web  #  importa la libreria web.py
import sqlite3  # importa la libreria sqlite3
import hashlib  # importa la libreria hashlib

urls = (
    "/", "Index",
    "/inicio_sesion_seguro", "IniciarSesionSeguro",
    "/inicio_sesion_inseguro", "IniciarSesionInseguro",
    "/bienvenida", "Bienvenida",
)  # define las urls del sistema

app = web.application(urls, globals())  # define la aplicacion web

render = web.template.render(
    "templates/", base="layout"
)  # define el render con la ubicación de los templates y la plantilla base


class Index:
    """_summary_: Pagina de inicio del sistema"""

    def __init__(self):
        """_summary_: Constructor de la clase"""
        pass

    def GET(self):
        """_summary_: Metodo GEt que renderiza la pagina index.html

        Returns:
            html: Renderiza la pagina index.html
        """
        return render.index()


class Bienvenida:
    """_summary_: Pagina de bienvenida del sistema"""

    def __init__(self):
        """_summary_: Constructor de la clase"""
        pass

    def GET(self):
        """_summary_: Metodo GEt que renderiza la pagina bienvenida.html
        Retunrs:
            html: Renderiza la pagina bienvenida.html
        """
        return render.bienvenida()


class IniciarSesionSeguro:
    """_summary_: Pagina de inicio de sesion seguro del sistema"""

    def __init__(self):
        """_summary_: Constructor de la clase"""
        pass

    def GET(self):
        """_summary_: Metodo GEt que renderiza la pagina inicio_sesion_seguro.html
        Returns:
            html: Renderiza la pagina inicio_sesion_seguro.html
        """
        try:
            mensaje = None
            return render.inicio_sesion_seguro(
                mensaje
            )  # Renderiza la pagina inicio_sesion_seguro.html
        except Exception as e:
            print(e)
            mensaje = "Ups algo salio muy mal"
            return render.inicio_sesion_seguro(
                mensaje
            )  # Renderiza la pagina inicio_sesion_seguro.html

    def POST(self):
        """_summary_: Metodo POST que recibe el formalario de inicio_sesion_seguro.html

        Returns:
            hmtl: Redirecciona a la pagina bienvenida.html o a la pagina inicio_sesion_seguro.html
        """
        try:
            mensaje = None
            form = web.input()  # Obtiene los datos del formulario
            email = form.email  # Obtiene el email del formulario
            password = form.password  # Obtiene el password del formulario
            password = hashlib.md5(password.encode())  # Genera un hash del password
            password = password.hexdigest()  # Parsea el password a hexadecimal
            print(email, password)  # Imprime los datos
            conexion = sqlite3.connect(
                "sql/usuarios.sqlite"
            )  # Conecta con la base de datos
            conexion.row_factory = sqlite3.Row  # Establece el row factory
            cursor = conexion.cursor()  # Crea un cursor
            # Utiliza parametros para evitar inyeccion de SQL
            result = cursor.execute(
                "select count(usuarios.uid) as auth from usuarios where usuarios.email=? and usuarios.password=? and usuarios.status='activo';",
                (email, password),
            )
            result = result.fetchall()[0]["auth"]  # Obtiene el primer registro
            if result == 0:  # Si es 0, no existe el usuario
                mensaje = "Verifique usuario y contraseña"  # Asigna el mensaje de error
                return render.inicio_sesion_seguro(
                    mensaje
                )  # Renderiza la pagina inicio_sesion_seguro.html
            if result == 1:  # Si es 1, existe el usuario
                return web.seeother(
                    "/bienvenida"
                )  # Redirecciona a la pagina bienvenida.html
        except Exception as e:
            print(e)
            mensaje = "Ups algo salio muy mal"  # Asigna un mensaje de error
            return render.inicio_sesion_seguro(
                mensaje
            )  # Renderiza la pagina inicio_sesion_seguro.html


class IniciarSesionInseguro:
    """_summary_: Pagina de inicio de sesion inseguro del sistema"""

    def __init__(self):
        """_summary_: Constructor de la clase"""
        pass

    def GET(self):
        """_summary_: Metodo GEt que renderiza la pagina inicio_sesion_inseguro.html

        Returns:
            html: Renderiza la pagina inicio_sesion_inseguro.html
        """
        try:
            mensaje = None  # Inicializa el mensaje
            return render.inicio_sesion_inseguro(
                mensaje
            )  # Renderiza la pagina inicio_sesion_inseguro.html
        except Exception as e:
            print(e)
            mensaje = "Ups algo salio muy mal"  # Asigna el mensaje de error
            return render.inicio_sesion_inseguro(
                mensaje
            )  # Renderiza la pagina inicio_sesion_inseguro.html

    def POST(self):
        """_summary_: Metodo POST que recibe el formalario de inicio_sesion_inseguro.html

        Returns:
            hmtl: Redirecciona a la pagina bienvenida.html o a la pagina inicio_sesion_inseguro.html
        """
        try:
            mensaje = None  # Inicializa el mensaje
            form = web.input()  # Obtiene los datos del formulario
            email = form.email  # Obtiene el email del formulario
            password = form.password  # Obtiene el password del formulario
            password = hashlib.md5(password.encode())  # Genera un hash del password
            password = password.hexdigest()  # Parsea el password a hexadecimal
            print(email, password)  # Imprime los datos para verificar los valores
            # Verifica si el usuario existe
            conexion = sqlite3.connect("sql/usuarios.sqlite")  # Abre la conexion
            conexion.row_factory = sqlite3.Row  # Establece el row factory
            cursor = conexion.cursor()  # Obtiene el cursor
            # Concatena el email y el password, lo hace vulnerable a inyeccion de SQL
            result = cursor.execute(
                "select count(usuarios.uid) as auth from usuarios where usuarios.email='"
                + email
                + "' and usuarios.password='"
                + password
                + "' and usuarios.status='activo';"
            )
            result = result.fetchall()[0]["auth"]  # Obtiene el primer registro
            if result == 0:  # Si es 0, no existe el usuario
                mensaje = "Verifique usuario y contraseña"  # Asigna el mensaje de error
                return render.inicio_sesion_inseguro(
                    mensaje
                )  # Renderiza la pagina inicio_sesion_inseguro.html
            if result == 1:  # Si es 1, existe el usuario
                return web.seeother(
                    "/bienvenida"
                )  # Redirecciona a la pagina bienvenida.html
        except Exception as e:
            print(e)
            mensaje = "Ups algo salio muy mal"  # Asigna el mensaje de error
            return render.inicio_sesion_inseguro(
                mensaje
            )  # Renderiza la pagina inicio_sesion_inseguro.html


if __name__ == "__main__":
    """_summary_: Main de la aplicacion"""
    app.run()
