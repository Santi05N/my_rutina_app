import reflex as rx
from my_rutina_app.models import Elemento
from my_rutina_app.funciones.cargar import cargar

class ElementosState(rx.State):
    elementos: list[Elemento] = []
    elementos_filtrados: list[Elemento] = []
    limite: int = 25
    paso: int = 25
    busqueda: str= ""

    def rellenar_lista(self):
        self.elementos = [Elemento(**elem) for elem in cargar()]
        self.elementos.sort(key= lambda e: (e.dificultad, e.fig))
        self.elementos_filtrados = self.elementos
        self.limite = self.paso

    def limpiar_busqueda(self):
        self.busqueda = ""
        self.elementos_filtrados = self.elementos
        self.limite = self.paso

    @rx.event
    def filtrar_elementos(self, texto: str) -> list[Elemento]:
        """Función Buscar Elemento."""
        self.busqueda = texto
        self.limite = self.paso
        if not texto:
            self.elementos_filtrados = self.elementos
        else:
            self.elementos_filtrados = [
                elem for elem in self.elementos 
                if texto.lower() in elem.nombre.lower()
                or texto.lower() in elem.fig.lower()
            ]

    @rx.var
    def elementos_visibles(self) -> list[Elemento]:
        return self.elementos_filtrados[: self.limite]

    @rx.var
    def hay_mas_elementos(self) -> bool:
        return self.limite < len(self.elementos)

    def cargar_mas(self):
        self.limite += self.paso

    def resetear_limite(self):
        self.limite = self.paso