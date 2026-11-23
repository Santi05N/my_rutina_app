import reflex as rx
from my_rutina_app.models import Elemento, Rutina
from ..states.elementos_state import ElementosState
from ..states.rutina_state import RutinaState
from ..components.cuadro_busqueda import overlay_busqueda
from ..components.lista_elementos import lista_elementos

def vista_elementos() -> rx.Component:
    return rx.stack(
        rx.flex(
            rx.text('Todos los elementos', weight='bold',size='4'),
            overlay_busqueda(),
        ),
        lista_elementos(ElementosState.elementos),
        # Nav bar
        width='100%',
        height='100%',
        align='stretch',
        direction='column'
    )
