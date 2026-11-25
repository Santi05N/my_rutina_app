import reflex as rx
from .elemento_basico import elemento_box

def lista_elementos(lista: list) -> rx.Component:
    # return rx.scroll_area(
    #     rx.foreach(lista, elemento_deslizante_agregar),
    #     scrollbars='vertical',
    #     type='hover',
    #     scroll_hide_delay=250
    # )
    return rx.vstack(
        rx.foreach(lista, lambda item: elemento_box(item, "agregar")),
        margin="10px",
        spacing="2",

    )