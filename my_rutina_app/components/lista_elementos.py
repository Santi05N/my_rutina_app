import reflex as rx
from .elemento_deslizante import elemento_deslizante_agregar

def lista_elementos(lista: list) -> rx.Component:
    return rx.scroll_area(
        rx.foreach(lista, elemento_deslizante_agregar),
        scrollbars='vertical',
        type='hover',
        scroll_hide_delay=250
    )