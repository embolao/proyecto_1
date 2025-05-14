import mysql.connector
from rich.console import Console
from rich.table import Table

# Configuración de conexión (ajusta si cambian tus credenciales)
config = {
    'host': 'localhost',
    'user': 'usuario',
    'password': 'usuario_pass',
    'database': 'tu_db',
    'port': 3306,
    'charset': 'utf8mb4',
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()
cursor.execute("SELECT * FROM intenciones LIMIT 30;")
rows = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]

console = Console()
table = Table(show_header=True, header_style="bold magenta")
for col in columns:
    table.add_column(col, style="cyan")

for row in rows:
    table.add_row(*[str(cell) for cell in row])

console.print(table)

cursor.close()
conn.close()
