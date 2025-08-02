from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

# 🏷️ Producto
class Producto(BaseModel):
    id: UUID
    codigo_barras: str
    nombre: str
    descripcion: Optional[str]
    categoria: Optional[str]
    stock: int
    stock_minimo: int
    precio_unitario: float
    ubicacion_id: Optional[UUID]
    activo: bool
    fecha_creacion: datetime

# 🗃️ Ubicacion (Estante, Casilla)
class Ubicacion(BaseModel):
    id: UUID
    codigo: str
    estante: str
    nivel: int
    casilla: str
    descripcion: Optional[str]

# 👤 Usuario
class Usuario(BaseModel):
    id: UUID
    nombre: str
    email: EmailStr
    rol: str
    activo: bool
    fecha_creacion: datetime

# 🔄 Movimiento (Entrada/Salida/Ajuste)
class Movimiento(BaseModel):
    id: UUID
    producto_id: UUID
    usuario_id: UUID
    tipo_movimiento: str  # 'entrada', 'salida', 'ajuste'
    cantidad: int
    motivo: Optional[str]
    timestamp: datetime

# 📝 Log (Auditoría de Acciones)
class Log(BaseModel):
    id: UUID
    usuario_id: UUID
    accion: str
    entidad: str
    entidad_id: UUID
    descripcion: Optional[str]
    timestamp: datetime