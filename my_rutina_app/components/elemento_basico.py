import reflex as rx
from ..states.elementos_state import Elemento

def elemento_box(item: Elemento) -> rx.Component:

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
    return rx.card(
        rx.flex(
            rx.flex(
                rx.icon(tag=item.fig, size=20),
                padding='3',
                border_radius="full",
                bg=bg_color,
                align="center",
                justify="center",
            ),
            rx.text(item.nombre, weight="bold", size="3"),
            rx.spacer(),
            rx.vstack(
                    rx.text("Diff:", size="1", color_scheme="gray"),
                    rx.text(
                        item.dificultad, weight="bold", size="4", class_name="mono"
                    ),
                    align_items="end",
                    spacing="0",
                ),
                align="center",
                spacing="3",
                width="100%",
            ),
        style={
            "border_left": f"4px solid {border_color}",
            "width": "100%",
        },
        variant="surface",
    )
