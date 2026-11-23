import reflex as rx
from my_rutina_app.models import Elemento
from my_rutina_app.funciones.cargar import cargar

class ElementosState(rx.State):
    elementos: list[Elemento] = []
    elementos_filtrados: list[Elemento] = []

    def rellenar_lista(self):
        for elem in cargar():
            self.elementos.append(Elemento(**elem))

    @rx.event
    def filtrar_elementos(self, texto: str) -> list[Elemento]:
        """Función Buscar Elemento."""
        if not texto:
            self.elementos_filtrados = self.elementos
        self.elementos_filtrados = [
            elem for elem in self.elementos 
            if self.busqueda.lower() in elem.nombre.lower()
            or self.busqueda.lower() in elem.fig.lower()
        ]
