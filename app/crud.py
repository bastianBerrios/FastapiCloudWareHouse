# funciones de acceso a la base de datos

from .database import get_db_connection
from .models import Producto, Ubicacion, Usuario, Movimiento, Log
from typing import List, Dict, Any
import uuid

# --- PRODUCTOS ---
async def get_all_productos() -> List[Dict[str, Any]]:
    conn = await get_db_connection()
    rows = await conn.fetch('SELECT * FROM productos')
    await conn.close()
    return [dict(row) for row in rows]

async def get_producto_by_id(producto_id: uuid.UUID):
    conn = await get_db_connection()
    row = await conn.fetchrow('SELECT * FROM productos WHERE id = $1', producto_id)
    await conn.close()
    return dict(row) if row else None

async def create_producto(producto_data: dict):
    conn = await get_db_connection()
    row = await conn.fetchrow('''
        INSERT INTO productos (codigo_barras, nombre, descripcion, categoria, stock, stock_minimo, precio_unitario, ubicacion_id, activo)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
        RETURNING *
    ''', producto_data['codigo_barras'], producto_data['nombre'], producto_data.get('descripcion'),
         producto_data.get('categoria'), producto_data['stock'], producto_data['stock_minimo'],
         producto_data['precio_unitario'], producto_data.get('ubicacion_id'), producto_data['activo'])
    await conn.close()
    return dict(row)

async def update_producto(producto_id: uuid.UUID, update_data: dict):
    conn = await get_db_connection()
    await conn.execute('''
        UPDATE productos
        SET nombre = $1, descripcion = $2, categoria = $3, stock = $4, stock_minimo = $5,
            precio_unitario = $6, ubicacion_id = $7, activo = $8
        WHERE id = $9
    ''', update_data['nombre'], update_data.get('descripcion'), update_data.get('categoria'),
         update_data['stock'], update_data['stock_minimo'], update_data['precio_unitario'],
         update_data.get('ubicacion_id'), update_data['activo'], producto_id)
    await conn.close()
    return await get_producto_by_id(producto_id)

async def delete_producto(producto_id: uuid.UUID):
    conn = await get_db_connection()
    await conn.execute('DELETE FROM productos WHERE id = $1', producto_id)
    await conn.close()

# --- UBICACIONES ---
async def get_all_ubicaciones():
    conn = await get_db_connection()
    rows = await conn.fetch('SELECT * FROM ubicaciones')
    await conn.close()
    return [dict(row) for row in rows]

# --- USUARIOS ---
async def get_all_usuarios():
    conn = await get_db_connection()
    rows = await conn.fetch('SELECT id, nombre, email, rol, activo, fecha_creacion FROM usuarios')
    await conn.close()
    return [dict(row) for row in rows]

# --- MOVIMIENTOS ---
async def get_all_movimientos():
    conn = await get_db_connection()
    rows = await conn.fetch('SELECT * FROM movimientos ORDER BY timestamp DESC')
    await conn.close()
    return [dict(row) for row in rows]

async def create_movimiento(movimiento_data: dict):
    conn = await get_db_connection()
    row = await conn.fetchrow('''
        INSERT INTO movimientos (producto_id, usuario_id, tipo_movimiento, cantidad, motivo)
        VALUES ($1, $2, $3, $4, $5)
        RETURNING *
    ''', movimiento_data['producto_id'], movimiento_data['usuario_id'], movimiento_data['tipo_movimiento'],
         movimiento_data['cantidad'], movimiento_data.get('motivo'))
    await conn.close()
    return dict(row)

# --- LOGS ---
async def get_all_logs():
    conn = await get_db_connection()
    rows = await conn.fetch('SELECT * FROM logs ORDER BY timestamp DESC')
    await conn.close()
    return [dict(row) for row in rows]

async def create_log(log_data: dict):
    conn = await get_db_connection()
    await conn.execute('''
        INSERT INTO logs (usuario_id, accion, entidad, entidad_id, descripcion)
        VALUES ($1, $2, $3, $4, $5)
    ''', log_data['usuario_id'], log_data['accion'], log_data['entidad'], log_data['entidad_id'], log_data.get('descripcion'))
    await conn.close()