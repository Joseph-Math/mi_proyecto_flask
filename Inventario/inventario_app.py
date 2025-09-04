
# inventario_app.py
# Sistema de gestión de inventario (POO + Colecciones + SQLite)
# Autor: José Luis Maldonado (adaptado por ChatGPT)
# Uso: python inventario_app.py

import sqlite3
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional

DB_PATH = "inventario.db"

@dataclass
class Producto:
    """
    Representa un producto del inventario.
    Atributos:
        id: int (único)
        nombre: str
        cantidad: int
        precio: float
    """
    id: int
    nombre: str
    cantidad: int
    precio: float

    # Métodos "get" y "set" implícitos por dataclass; se incluyen setters controlados:
    def set_cantidad(self, nueva_cantidad: int) -> None:
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio: float) -> None:
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = nuevo_precio

class Inventario:
    """
    Maneja una colección de productos utilizando un diccionario para acceso O(1) por ID.
    Sincroniza las operaciones con una base de datos SQLite para persistencia.
    """
    def __init__(self, db_path: str = DB_PATH) -> None:
        self.db_path = db_path
        # Colección principal en memoria: dict[int, Producto]
        self._productos: Dict[int, Producto] = {}
        self._con = sqlite3.connect(self.db_path)
        self._con.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )
        """)
        self._con.commit()
        self._cargar_desde_db()

    # --------------- Utilitarios internos -----------------
    def _cargar_desde_db(self) -> None:
        self._productos.clear()
        cur = self._con.cursor()
        cur.execute("SELECT id, nombre, cantidad, precio FROM productos")
        for pid, nombre, cantidad, precio in cur.fetchall():
            self._productos[pid] = Producto(pid, nombre, cantidad, precio)

    def _insertar_db(self, p: Producto) -> None:
        self._con.execute(
            "INSERT INTO productos (id, nombre, cantidad, precio) VALUES (?, ?, ?, ?)",
            (p.id, p.nombre, p.cantidad, p.precio),
        )
        self._con.commit()

    def _eliminar_db(self, producto_id: int) -> None:
        self._con.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
        self._con.commit()

    def _actualizar_db(self, p: Producto) -> None:
        self._con.execute(
            "UPDATE productos SET nombre=?, cantidad=?, precio=? WHERE id=?",
            (p.nombre, p.cantidad, p.precio, p.id),
        )
        self._con.commit()

    # --------------- API pública --------------------------
    def anadir_producto(self, producto: Producto) -> None:
        if producto.id in self._productos:
            raise KeyError(f"Ya existe un producto con ID {producto.id}.")
        # Inserta primero en DB; si falla, no ensucia la memoria
        self._insertar_db(producto)
        self._productos[producto.id] = producto

    def eliminar_producto(self, producto_id: int) -> None:
        if producto_id not in self._productos:
            raise KeyError(f"No existe un producto con ID {producto_id}.")
        self._eliminar_db(producto_id)
        del self._productos[producto_id]

    def actualizar_producto(
        self,
        producto_id: int,
        nueva_cantidad: Optional[int] = None,
        nuevo_precio: Optional[float] = None,
        nuevo_nombre: Optional[str] = None,
    ) -> None:
        if producto_id not in self._productos:
            raise KeyError(f"No existe un producto con ID {producto_id}.")
        p = self._productos[producto_id]
        if nueva_cantidad is not None:
            p.set_cantidad(nueva_cantidad)
        if nuevo_precio is not None:
            p.set_precio(nuevo_precio)
        if nuevo_nombre is not None and nuevo_nombre.strip():
            p.nombre = nuevo_nombre.strip()
        self._actualizar_db(p)

    def buscar_por_nombre(self, texto: str) -> List[Producto]:
        """
        Búsqueda flexible (case-insensitive) por coincidencia parcial.
        Retorna una lista (colección) de Productos.
        """
        t = texto.strip().lower()
        return [p for p in self._productos.values() if t in p.nombre.lower()]

    def obtener(self, producto_id: int) -> Optional[Producto]:
        return self._productos.get(producto_id)

    def todos(self) -> List[Producto]:
        # Convertimos el dict a lista para presentación ordenada por ID
        return [self._productos[k] for k in sorted(self._productos.keys())]

    def resumen_por_nombres(self) -> Dict[str, int]:
        """
        Usa colecciones para obtener un resumen: total de ítems por nombre.
        Demuestra uso de dict + set/list comprehensions.
        """
        resumen: Dict[str, int] = {}
        for p in self._productos.values():
            resumen[p.nombre] = resumen.get(p.nombre, 0) + p.cantidad
        return resumen

    def cerrar(self) -> None:
        self._con.close()

# ----------------- Interfaz de usuario (CLI) -----------------
def imprimir_producto(p: Producto) -> None:
    print(f"ID={p.id} | Nombre={p.nombre} | Cantidad={p.cantidad} | Precio={p.precio:.2f}")

def menu() -> None:
    inv = Inventario()
    print("=== Sistema de Inventario (Ferretería/Panadería/Librería, etc.) ===")
    print("Base de datos:", DB_PATH)
    try:
        while True:
            print("\nSeleccione una opción:")
            print("1) Añadir producto")
            print("2) Eliminar producto por ID")
            print("3) Actualizar producto (cantidad/precio/nombre)")
            print("4) Buscar productos por nombre")
            print("5) Mostrar todos los productos")
            print("6) Resumen por nombre (total de unidades)")
            print("0) Salir")

            op = input("> ").strip()
            if op == "1":
                try:
                    pid = int(input("ID (entero único): ").strip())
                    nombre = input("Nombre: ").strip()
                    cantidad = int(input("Cantidad: ").strip())
                    precio = float(input("Precio: ").strip())
                    inv.anadir_producto(Producto(pid, nombre, cantidad, precio))
                    print("✓ Producto añadido.")
                except Exception as e:
                    print("✗ Error al añadir:", e)

            elif op == "2":
                try:
                    pid = int(input("ID a eliminar: ").strip())
                    inv.eliminar_producto(pid)
                    print("✓ Producto eliminado.")
                except Exception as e:
                    print("✗ Error al eliminar:", e)

            elif op == "3":
                try:
                    pid = int(input("ID a actualizar: ").strip())
                    campos = input("¿Actualizar [c]antidad, [p]recio, [n]ombre o [t]odo?: ").strip().lower()
                    nueva_cantidad = None
                    nuevo_precio = None
                    nuevo_nombre = None
                    if campos in ("c", "t"):
                        nueva_cantidad = int(input("Nueva cantidad: ").strip())
                    if campos in ("p", "t"):
                        nuevo_precio = float(input("Nuevo precio: ").strip())
                    if campos in ("n", "t"):
                        nuevo_nombre = input("Nuevo nombre: ").strip()
                    inv.actualizar_producto(pid, nueva_cantidad, nuevo_precio, nuevo_nombre)
                    print("✓ Producto actualizado.")
                except Exception as e:
                    print("✗ Error al actualizar:", e)

            elif op == "4":
                texto = input("Texto a buscar (nombre parcial): ").strip()
                resultados = inv.buscar_por_nombre(texto)
                if resultados:
                    print(f"Resultados ({len(resultados)}):")
                    for p in resultados:
                        imprimir_producto(p)
                else:
                    print("No se encontraron coincidencias.")

            elif op == "5":
                productos = inv.todos()
                if productos:
                    print("Inventario actual:")
                    for p in productos:
                        imprimir_producto(p)
                else:
                    print("(Inventario vacío)")

            elif op == "6":
                resumen = inv.resumen_por_nombres()
                if resumen:
                    print("Total de unidades por nombre:")
                    for nombre, total in resumen.items():
                        print(f"- {nombre}: {total}")
                else:
                    print("(Sin datos)")

            elif op == "0":
                print("Saliendo...")
                break
            else:
                print("Opción no válida.")
    finally:
        inv.cerrar()

if __name__ == "__main__":
    menu()
