from app.config.mysql_connection import connect_to_mysql

class Auto:
    def __init__(self,data) -> None:
        self.id = data['id']
        self.marca = data['marca']
        self.modelo = data['modelo']
        self.ingredientes = data['ingredientes']
        self.descripcion = data['descripcion']
        self.precio = data['precio']
        self.user_id = data['user_id']
    
    @classmethod
    def todos(cls):
        query = "SELECT * FROM auto"
        results = connect_to_mysql().query_db(query)
        autos = []
        for auto in results:
            autos.append(cls(auto))
        return autos
    
    @classmethod
    def uno(cls,data:dict):
        query = "SELECT * FROM auto WHERE id = %(id)s"
        results = connect_to_mysql().query_db(query,data)
        print(cls(results[0]))
        return cls(results[0])
    
    @classmethod
    def guardar(cls,data:dict):
        query = """
                INSERT INTO auto (marca,modelo,ingredientes,descripcion,precio,user_id)
                VALUES (%(marca)s,%(modelo)s,%(ingredientes)s,%(descripcion)s,%(precio)s,%(user_id)s)
                """
        return connect_to_mysql().query_db(query,data)

    @classmethod
    def editar(cls,data):
        query = """
                UPDATE auto
                SET marca = %(marca)s,modelo = %(modelo)s,ingredientes = %(ingredientes)s,descripcion = %(descripcion)s, precio = %(precio)s
                WHERE id = %(id)s
                """
        return connect_to_mysql().query_db(query,data)
    
    @classmethod
    def borrar(cls,data:dict):
        query = "DELETE FROM auto WHERE id = %(id)s"
        return connect_to_mysql().query_db(query,data)
    