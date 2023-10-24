from app.config.mysql_connection import connect_to_mysql

class User:
    def __init__(self,data) -> None:
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.correo = data["correo"]
        self.contrasenha = data["contrasenha"]

    @classmethod
    def guardar(cls,data:dict):
        query = """
                INSERT INTO user (nombre,apellido,correo,contrasenha)
                VALUES (%(nombre)s,%(apellido)s,%(correo)s,%(contrasenha)s);
                """
        return connect_to_mysql().query_db(query,data)
    
    @classmethod
    def obtener_por_correo(cls,data:dict):
        query = "SELECT * FROM user WHERE correo = %(correo)s"
        resultado = connect_to_mysql().query_db(query,data)
        if resultado:
            return cls(resultado[0])
        return None

    
