import reflex as rx
from ..models import Elemento
from ..states.rutina_state import RutinaState
from .elemento_basico import elemento_box

class MotionDiv(rx.Component):
    library = "framer-motion"
    tag = "motion.div"

    # Propiedades soportadas por framer-motion
    drag: rx.Var[str]
    drag_constraints: rx.Var[dict]
    drag_elastic: rx.Var[float]
    drag_snap_to_origin: rx.Var[bool]

    # Handlers de eventos
    on_drag_end: rx.EventHandler[lambda info: [info]]


# Instancia del componente
motion_div = MotionDiv.create


class State(rx.State):

    def ejecutar_accion(self, info, item: Elemento):
        offset_x = info.get('offset',{}).get('x',0)

        if offset_x > 100:
            RutinaState.agregar_elemento(item)


def elemento_deslizante_agregar(item: Elemento) -> rx.Component:
    
    return rx.box(
        rx.flex(
            rx.flex(
                rx.icon(tag="plus", size=22, color="white"),
                rx.text("Añadir", color="white", weight="bold"),
                spacing="2",
                align="center",
            ),
            bg=rx.color("green", 9),
            border_radius="var(--radius-3)",
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            padding_x="4",
            align="center",
            justify="start",
        ),
        motion_div(
            elemento_box(item),
            drag="x",
            drag_constraints={"left": 0, "right": 140},
            drag_elastic=0.2,
            drag_snap_to_origin=True,
            on_drag_end=lambda info: State.ejecutar_accion(
                info, item.nombre
            ),
            style={
                "position": "relative",
                "z_index": 1,
                "touch_action": "none",
            },
        ),
        position="relative",
        width="100%",
        overflow="hidden",
        border_radius="var(--radius-3)",
    )