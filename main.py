from database import Database
from gui import CustomBikeApp

if __name__ == "__main__":
    # Configuración de la conexión a la base de datos
    db = Database(
    user="tu_usuario",              # Usuario de la base de datos
    password="tu_contraseña",       # Contraseña
    host="localhost",               # Servidor (localhost si es local)
    port="5432",                    # Puerto de PostgreSQL (por defecto es 5432)
    database="custombike"           # Nombre de la base de datos
    )
    try:
        app = CustomBikeApp(db)
        app.run()
    finally:
        db.close()
