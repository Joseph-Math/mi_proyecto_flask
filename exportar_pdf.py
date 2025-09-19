import mysql.connector
from fpdf import FPDF
import pandas as pd
import os

# ==========================
# Conexión a MariaDB
# ==========================
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc123abc123",
    database="liceo_policial"
)

cursor = conexion.cursor()

# ==========================
# Obtener todas las tablas
# ==========================
cursor.execute("SHOW TABLES")
tablas = [table[0] for table in cursor.fetchall()]

# ==========================
# Crear PDF en landscape
# ==========================
pdf = FPDF(orientation="L", unit="mm", format="A4")
pdf.set_auto_page_break(auto=True, margin=15)

# ==========================
# Recorrer todas las tablas
# ==========================
for tabla in tablas:
    cursor.execute(f"SELECT * FROM {tabla}")
    datos = cursor.fetchall()
    columnas = [desc[0] for desc in cursor.description]

    # Crear DataFrame para mejor visualización
    df = pd.DataFrame(datos, columns=columnas)

    # Nueva página por tabla
    pdf.add_page()
    pdf.set_font("helvetica", "B", 14)
    pdf.cell(0, 10, f"Tabla: {tabla}", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(5)

    pdf.set_font("helvetica", size=10)
    for i, row in df.iterrows():
        fila_texto = " | ".join(str(x) for x in row.values)
        
        # Dividir la fila en trozos si es muy larga
        max_chars = 200  # ajustable según cantidad de columnas
        lineas = [fila_texto[i:i+max_chars] for i in range(0, len(fila_texto), max_chars)]
        for linea in lineas:
            pdf.multi_cell(0, 8, linea)
        pdf.ln(2)  # separación entre filas

# ==========================
# Guardar PDF en Descargas
# ==========================
ruta_pdf = os.path.expanduser("~/Descargas/liceo_policial.pdf")
pdf.output(ruta_pdf)

print(f"PDF generado correctamente en: {ruta_pdf}")

# ==========================
# Cerrar conexión
# ==========================
cursor.close()
conexion.close()
