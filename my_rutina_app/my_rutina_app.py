import reflex as rx
# from .pruebas.listas_mult import index, Objetos, rutina
# from .pruebas.prueba1 import index
# from .pages.vista_elementos import vista_elementos
from .components.lista_elementos import lista_elementos
from .components.cuadro_busqueda import cuadro_busqueda

def index() -> rx.Component:
    return rx.box(
        cuadro_busqueda(),
        lista_elementos(),
        margin="10px",
        )

app = rx.App()
# app.add_page(vista_elementos, route='/v')
app.add_page(index, route='/')
