# 🚲 CustomBikes

Este repositorio contiene el proyecto de base de datos y software desarrollado para CustomBikes S.A., una empresa especializada en la manufactura de bicicletas personalizadas. El objetivo principal es proporcionar una solución que integre una base de datos relacional con un software que gestione eficientemente los pedidos, ensamblajes y estadísticas de la empresa.

## ✨ Características del Proyecto

### 🗄️ Base de Datos
- **Modelado:** Utilizando el enfoque entidad-relación (E-R) y normalización hasta la 3FN.
- **Scripts:**
  - Creación de tablas con claves primarias, foráneas y restricciones.
  - Inserción de al menos 100 registros en cada tabla.
  - Consultas SQL optimizadas para los requerimientos del sistema.
  - Procedimientos almacenados para análisis y generación de gráficos.

### 💻 Software en Python
- **Conexión con PostgreSQL:** Usando `psycopg2`.
- **Interfaz gráfica de usuario (GUI):** Desarrollada con `Tkinter`.
- **Funcionalidades principales:**
  - Consultar pedidos por cliente y período.
  - Listar componentes más solicitados.
  - Mostrar bicicletas vendidas y detalles de sus garantías.
  - Identificar técnicos destacados y con incrementos de productividad.
  - Generar gráficos interactivos con `matplotlib`.

## 📋 Requisitos del Sistema

### 🛠️ Tecnologías Utilizadas
- Lenguaje: Python 3.8+
- Base de datos: PostgreSQL
- Librerías:
  - `tkinter`
  - `matplotlib`
  - `psycopg2`
  - `tabulate`
  - `pandas`

### 🌟 Instalación de Dependencias
```bash
pip install -r requirements.txt
```

## 🚀 Cómo Ejecutar el Proyecto

### Clona este repositorio:
```bash
git clone https://github.com/tu_usuario/CustomBikes.git
cd CustomBikes
```

### Configura la Base de Datos:
- Ejecuta el script `database/custombikes.sql` en tu servidor PostgreSQL.
- Actualiza las credenciales de la base de datos en `main.py`:
  ```python
  db = Database(
      user="tu_usuario",
      password="tu_contraseña",
      host="localhost",
      port="5432",
      database="custombike"
  )
  ```

### Ejecuta la Aplicación:
```bash
python main.py
```

## 🖥️ Funcionalidades

### 1️⃣ Consultar Pedidos por Cliente
Permite ingresar el nombre y apellido de un cliente para obtener los pedidos realizados en un período específico.

### 2️⃣ Listar Componentes Más Solicitados
Muestra los componentes más solicitados en los pedidos ordenados por popularidad.

### 3️⃣ Bicicletas y Garantías
Lista las bicicletas vendidas junto con los detalles de sus garantías.

### 4️⃣ Técnicos Destacados
Muestra los técnicos que ensamblaron más bicicletas que el promedio mensual del último año.

### 5️⃣ Técnicos con Incremento
Identifica técnicos que aumentaron la cantidad de ensamblajes entre dos años específicos.

### 6️⃣ Gráfico "Clientes Bike"
Genera un gráfico de barras horizontal que muestra el número de clientes que compraron marcos, ruedas y frenos en un año especificado.

## 📖 Estructura del Proyecto
```
CustomBikes/
├── database/
│   └── custombikes.sql   # Script de creación y población de la base de datos
├── main.py               # Archivo principal para ejecutar la aplicación
├── gui.py                # Código para la interfaz gráfica
├── database.py           # Clase para la conexión y operaciones en la base de datos
├── queries.py            # Módulo con las consultas SQL utilizadas
├── requirements.txt      # Dependencias necesarias para el proyecto
└── venv/                 # Entorno virtual para gestionar las librerías
```

## 👥 Contribuciones
¿Te gustaría colaborar en este proyecto?

- Reporta errores o problemas abriendo un _issue_ en el repositorio.
- Propón mejoras en la interfaz o lógica del programa.
- Realiza un fork del repositorio y envía tus pull requests.

## 📝 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

¡Gracias por revisar este proyecto! 🚴✨
