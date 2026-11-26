import reflex as rx
from .elemento_basico import elemento_box
from ..states.elementos_state import ElementosState

def lista_elementos() -> rx.Component:
    # return rx.scroll_area(
    #     rx.foreach(lista, elemento_deslizante_agregar),
    #     scrollbars='vertical',
    #     type='hover',
    #     scroll_hide_delay=250
    # )
    return rx.box(
        rx.box(
            rx.foreach(ElementosState.elementos_visibles, lambda item: elemento_box(item, "agregar")),
            rx.cond(
                ElementosState.hay_mas_elementos,
                rx.button(
                    "Cargar más",
                    on_click=ElementosState.cargar_mas,
                    variant="soft",
                    width="100%",
                ),
                rx.text(
                    "Mostrando todos los elementos",
                    size="2",
                    color_scheme="gray",
                ),
            ),
        ),
        on_mount=ElementosState.rellenar_lista,
        border="2px solid gray",
        border_radius="8px",
    )