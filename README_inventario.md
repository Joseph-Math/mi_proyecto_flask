
# Sistema de Gestión de Inventario (POO + Colecciones + SQLite)

## Cómo ejecutar
1. Asegúrate de tener Python 3.9+.
2. Guarda `inventario_app.py` y ejecuta:
   ```bash
   python inventario_app.py
   ```
   Se creará automáticamente la base de datos `inventario.db` con la tabla `productos` si no existe.

## Diseño (POO + Colecciones)
- **Producto** (dataclass): id, nombre, cantidad, precio. Incluye validaciones y setters controlados.
- **Inventario**: usa un **diccionario** (`dict[int, Producto]`) para búsquedas O(1) por ID, y **listas** para presentar resultados.
  - `buscar_por_nombre` retorna una **lista** de productos filtrados (list comprehension).
  - `resumen_por_nombres` construye un **diccionario** {nombre: total_cantidad}.
  - Se demuestra el uso de **tuplas** en retornos/iteraciones y **sets** implícitos en validaciones si se extiende.
- Persistencia con **SQLite (sqlite3)**. CRUD sincronizado con la tabla `productos`.

## Operaciones disponibles (CRUD + utilidades)
- Añadir producto
- Eliminar producto por ID
- Actualizar cantidad / precio / nombre
- Buscar por nombre (insensible a mayúsculas/minúsculas)
- Mostrar todos los productos
- Resumen por nombre (totales)

## Estructura de la DB
```sql
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL
);
```

## Sugerencias de integración con tu proyecto existente (Flask)
- Puedes envolver la clase `Inventario` en **servicios** o **blueprints** y exponer endpoints REST.
- Reutiliza `inventario.db` o configura otra ruta vía el argumento `db_path` en `Inventario`.
- Para pruebas unitarias, crea una DB temporal en memoria con `Inventario(":memory:")`.

## Pruebas rápidas (ejemplo interactivo)
1) Opción 1: Añade un producto con ID=1, nombre="Tornillos", cantidad=100, precio=0.05
2) Opción 5: Verifica que aparezca en el listado.
3) Opción 3: Actualiza su precio a 0.08
4) Opción 4: Búscalo por "torn"
5) Opción 6: Observa el resumen por nombre.
