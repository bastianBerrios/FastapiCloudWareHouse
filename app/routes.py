# endpoints api

from fastapi import APIRouter, HTTPException
from uuid import UUID
from .crud import (
    get_all_productos, get_producto_by_id, create_producto, update_producto, delete_producto,
    get_all_ubicaciones, get_all_usuarios, get_all_movimientos, create_movimiento,
    get_all_logs, create_log
)

router = APIRouter()

# --- PRODUCTOS ---
@router.get("/productos")
async def listar_productos():
    return {"productos": await get_all_productos()}

@router.get("/productos/{producto_id}")
async def obtener_producto(producto_id: UUID):
    producto = await get_producto_by_id(producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/productos")
async def crear_producto(producto: dict):
    return await create_producto(producto)

@router.put("/productos/{producto_id}")
async def editar_producto(producto_id: UUID, producto: dict):
    return await update_producto(producto_id, producto)

@router.delete("/productos/{producto_id}")
async def eliminar_producto(producto_id: UUID):
    await delete_producto(producto_id)
    return {"mensaje": "Producto eliminado"}

# --- UBICACIONES ---
@router.get("/ubicaciones")
async def listar_ubicaciones():
    return {"ubicaciones": await get_all_ubicaciones()}

# --- USUARIOS ---
@router.get("/usuarios")
async def listar_usuarios():
    return {"usuarios": await get_all_usuarios()}

# --- MOVIMIENTOS ---
@router.get("/movimientos")
async def listar_movimientos():
    return {"movimientos": await get_all_movimientos()}

@router.post("/movimientos")
async def registrar_movimiento(movimiento: dict):
    return await create_movimiento(movimiento)

# --- LOGS ---
@router.get("/logs")
async def listar_logs():
    return {"logs": await get_all_logs()}

@router.post("/logs")
async def registrar_log(log: dict):
    await create_log(log)
    return {"mensaje": "Log registrado"}