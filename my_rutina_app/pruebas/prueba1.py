import reflex as rx

class EstadoDesplazamiento(rx.State):
    posicion_x: int = 0
    completado: bool = False

    def mover_derecha(self):
        self.posicion_x = 250
        self.completado = True

    def reiniciar(self):
        self.posicion_x = 0
        self.completado = False

def index():
    return rx.vstack(
        # El contenedor (Box) que se desplaza
        rx.box(
            rx.text(
                rx.cond(EstadoDesplazamiento.completado, "¡Animación Lista! 🎉", "Cuadro Deslizable")
            ),
            padding="20px",
            background_color=rx.cond(EstadoDesplazamiento.completado, "#4ADE80", "#60A5FA"),
            border_radius="12px",
            width="200px",
            text_align="center",
            color="white",
            font_weight="bold",
            # CSS para mover el cuadro y suavizar la animación
            style={
                "transform": f"translateX({EstadoDesplazamiento.posicion_x}px)",
                "transition": "transform 0.4s ease-out, background-color 0.4s ease",
            },
        ),
        
        # Botones de control para probar la lógica
        rx.hstack(
            rx.button("Deslizar a la derecha", on_click=EstadoDesplazamiento.mover_derecha, color_scheme="blue"),
            rx.button("Reiniciar", on_click=EstadoDesplazamiento.reiniciar, color_scheme="gray"),
            spacing="4",
        ),
        spacing="6",
        padding="50px",
    )