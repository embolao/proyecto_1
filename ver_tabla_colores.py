import mysql.connector
from rich.console import Console
from rich.table import Table

# Configuración de conexión (ajusta si cambian tus credenciales)
config = {
    "host": "localhost",
    "user": "usuario",
    "password": "usuario_pass",
    "database": "tu_db",
    "port": 3306,
    "charset": "utf8mb4",
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()
# Obtener todas las tablas
cursor.execute("SHOW TABLES;")
tables = [row[0] for row in cursor.fetchall()]

console = Console()
console.print("[bold magenta]Tablas en la base de datos:[/bold magenta]")
for idx, t in enumerate(tables, 1):
    console.print(f"[cyan]{idx}[/cyan]: {t}")

for tabla in tables:
    console.rule(f"[bold green]Tabla: {tabla}")
    cursor.execute(f"SELECT * FROM `{tabla}` LIMIT 30;")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    table = Table(show_header=True, header_style="bold magenta")
    for col in columns:
        table.add_column(col, style="cyan")
    if rows:
        for row in rows:
            table.add_row(*[str(cell) for cell in row])
    else:
        table.add_row(*["(vacío)" for _ in columns])
    console.print(table)

cursor.close()
conn.close()
