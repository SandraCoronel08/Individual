from app.config.mysql_connection import connect_to_mysql

class Tabla:
    def __init__(self,data) -> None:
        self.id = data['id']
        self.modelo = data['modelo']
        self.usuario = data['usuario']
        self.user_id = data['user_id']


    @classmethod

    def obtener_todos(cls):
        query = """
                SELECT * FROM receta
                JOIN usuario ON receta.user_id = user.id
                """