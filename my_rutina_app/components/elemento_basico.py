import reflex as rx
from ..states.elementos_state import Elemento
from .boton_simple import boton_simple

def elemento_box(item: Elemento, nombre_funcion: str) -> rx.Component:

    bg_color = rx.match(
        item.direccion,
        ('f', rx.color('orange',3)),
        ('b', rx.color('violet',3)),
        rx.color('cyan',3)
    )
    border_color = rx.match(
            item.direccion,
            ('f', rx.color('orange',7)),
            ('b', rx.color('violet',7)),
            rx.color('cyan', 7)
        )

    boton_match = rx.match(
        nombre_funcion,
        ("agregar", boton_simple("Agregar a rutina", "green")),
        ("borrar", boton_simple("Eliminar de rutina", "red")),
        boton_simple("Deshabilitado", "gray")
    )
    
    return rx.card(
        # Tira de color a la izquierda del elemento
        rx.flex(

            # Simbologia fig y color de fondo segun la direccion
            rx.flex(
                rx.text(f"{item.fig}", size="4"),
                padding='3',
                border_radius="4px",
                bg=bg_color,
                align="center",
                justify="center",
            ),

            # Nombre del elemento
            rx.text(item.nombre, weight="bold", size="3"),

            rx.spacer(),

            # Dificultad del elemento
            rx.vstack(
                rx.text("Diff:", size="1", color_scheme="gray"),
                rx.text(
                    item.dificultad, weight="bold", size="4", class_name="mono"
                ),
                align_items="end",
                spacing="0",
            ),

            # Boton para agregar o eliminar
            boton_match,

            align="center",
            spacing="3",
            width="100%",
        ),
        style={
            "border_left": f"4px solid {border_color}",
            "width": "100%",
            "margin_right": "20px",
        },
        variant="surface"
    )
