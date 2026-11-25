import reflex as rx
# from .pruebas.listas_mult import index, Objetos, rutina
# from .pruebas.prueba1 import index
# from .pages.vista_elementos import vista_elementos
from .components.lista_elementos import lista_elementos
from .funciones.cargar import cargar

def index() -> rx.Component:
    return rx.box(
        lista_elementos(cargar()),
        border="4px solid white",
        border_radius="8px",
        margin="10px",
        )

app = rx.App()
# app.add_page(vista_elementos, route='/v')
app.add_page(index, route='/')
