import reflex as rx
from ..states.elementos_state import ElementosState
from .elemento_deslizante import elemento_box

class State(rx.State):
    # Controla la visibilidad del modal
    show_modal: bool = False

    def toggle_modal(self):
        self.show_modal = not self.show_modal

def overlay_busqueda() -> rx.Component:
    return rx.fragment(
        # Botón principal para abrir la vista superpuesta
        rx.button(
            "Buscar Objetos",
            on_click=State.toggle_modal,
            color_scheme="blue",
            icon="search",
        ),
        rx.dialog.root(
            rx.dialog.content(
                rx.dialog.title("Lista de Objetos"),
                rx.dialog.description(
                    "Filtra la lista usando el cuadro de búsqueda."
                ),
                # Cuadro de búsqueda
                rx.input(
                    placeholder="Escribe para filtrar...",
                    width="100%",
                    margin_y="3",
                    on_change=ElementosState.filtrar_elementos
                ),
                # Contenedor con scroll para la lista de objetos
                rx.scroll_area(
                    rx.vstack(
                        rx.foreach(
                            ElementosState.elementos_filtrados,
                            elemento_box,
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    type="always",
                    scrollbars="vertical",
                    style={"height": 250},
                ),
                # Botón de cierre dentro del modal
                rx.flex(
                    rx.dialog.close(
                        rx.button(
                            "Cerrar",
                            variant="soft",
                            color_scheme="gray",
                            on_click=State.toggle_modal,
                        )
                    ),
                    margin_top="4",
                    justify="end",
                ),
                max_width="450px",
            ),
            open=State.show_modal,
            on_open_change=State.toggle_modal,
        ),
    )