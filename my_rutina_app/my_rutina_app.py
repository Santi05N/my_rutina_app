import reflex as rx
from .pruebas.listas_mult import index, Objetos, rutina
from .pages.vista_elementos import vista_elementos
from .pruebas.prueba1 import index

app = rx.App()
app.add_page(vista_elementos, route='/v')
app.add_page(index, route='/')
