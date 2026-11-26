import reflex as rx
from ..states.elementos_state import ElementosState
from .elemento_basico import elemento_box

class State(rx.State):
    # Controla la visibilidad del modal
    show_modal: bool = False

    def toggle_modal(self):
        self.show_modal = not self.show_modal

def cuadro_busqueda() -> rx.Component:
    return rx.hstack(
        rx.debounce_input(
            rx.input(
                placeholder="Buscar por nombre o fig...",
                value=ElementosState.busqueda,
                on_change=ElementosState.filtrar_elementos,
                width="100%",
            ),
            debounce_timeout=300,
        ),
        rx.cond(
            ElementosState.busqueda != "",
            rx.button(
                "Limpiar",
                on_click=ElementosState.limpiar_busqueda,
                variant="soft",
                color_scheme="gray",
            ),
        ),
        width="100%",
        spacing="2",
    )