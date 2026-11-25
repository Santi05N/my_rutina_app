import reflex as rx


def boton_simple(texto: str, color: str) -> rx.Component:
    return rx.button(
        texto,
        color_scheme=color,
        width="80px",
        height="100%"
    )