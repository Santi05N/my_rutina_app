import reflex as rx
import uuid
import dataclasses

@dataclasses.dataclass
class Elemento:
    nombre: str
    fig: str
    posicion: str | None
    dificultad: int
    direccion: str | None

@dataclasses.dataclass
class Rutina:
    id: uuid
    nombre: str
    dificultad_total: int
    sexo: str
    elementos: list[Elemento]
