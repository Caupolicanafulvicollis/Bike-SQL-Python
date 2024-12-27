import psycopg2

class Database:
    def __init__(self, user, password, host, port, database):
        try:
            self.connection = psycopg2.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database
            )
            print("Conexión exitosa a la base de datos.")
        except Exception as e:
            print(f"Error conectando a la base de datos: {e}")
            self.connection = None

    def execute_query(self, query, params=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Exception as e:
            print(f"Error ejecutando la consulta: {e}")
            return []

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")
