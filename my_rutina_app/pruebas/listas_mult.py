import reflex as rx
import json
import uuid
import dataclasses

datos = [
    {
    'nombre': 'Elemento 1',
    'valor': 1
    },
    {
    'nombre': 'Elemento 2',
    'valor': 2
    },
    {
    'nombre': 'Elemento 3',
    'valor': 3
    },
    {
    'nombre': 'Elemento 4',
    'valor': 4
    },
    {
    'nombre': 'Elemento 5',
    'valor': 5
    },
    {
    'nombre': 'Elemento 6',
    'valor': 6
    },
    {
    'nombre': 'Elemento 7',
    'valor': 7
    },
    {
    'nombre': 'Elemento 8',
    'valor': 8
    },
    {
    'nombre': 'Elemento 9',
    'valor': 9
    },
    {
    'nombre': 'Elemento 10',
    'valor': 10
    },
]

@dataclasses.dataclass
class Elemento:
    nombre: str
    valor: int

@dataclasses.dataclass
class Rutina:
    id: uuid
    nombre: str
    lista_elementos: list[Elemento]
    dificultad: int

class Objetos(rx.State):
    lista_elementos: list[Elemento] = []
    lista_rutinas: list[Rutina] = []
    rutina: Rutina | None = None

    def cargar(self):
        self.lista_elementos = [Elemento(**d) for d in datos]

    rx.event
    def crear_rutina(self):
        self.rutina = Rutina(id=uuid.uuid4(), nombre='Nueva Rutina', lista_elementos = [], dificultad=0)

    rx.event
    def agregar_a_rutina(self, item: Elemento):
        if not self.rutina:
            self.crear_rutina()
        self.rutina.lista_elementos.append(item)

    rx.event
    def eliminar_de_rutina(self, item: Elemento):
        self.rutina.lista_elementos.remove(item)

def caja_elemento_todos(e : Elemento) -> rx.Component:

    return rx.center(
        rx.hstack(
            rx.text(e.nombre),
            rx.text(e.valor)
        ),
        rx.button(rx.icon('plus'),on_click=Objetos.agregar_a_rutina(e)),
        size='2',
        direction='row',
        align='center',
        spacing='2',
        border_radius="0.5rem",
        width='100%'
    )

def caja_elemento_rutina(e: Elemento)-> rx.Component:
    return rx.center(
            rx.hstack(
                rx.text(e.nombre),
                rx.text(e.valor)
            ),
            rx.button(rx.icon('minus'),on_click=Objetos.eliminar_de_rutina(e)),
            size='2',
            direction='row',
            align='center',
            spacing='2',
            border_radius="0.5rem",
            width='100%'
        )

def index() -> rx.Component:
    return rx.vstack(
        rx.foreach(Objetos.lista_elementos, caja_elemento_todos)
    )

def rutina() -> rx.Component:
    return rx.vstack(
            rx.foreach(Objetos.rutina.lista_elementos, caja_elemento_rutina)
        )
