import reflex as rx
from my_rutina_app.models import Elemento, Rutina
import uuid

class RutinaState(rx.State):
    rutina = Rutina(
        id=uuid.uuid4(), 
        nombre='Nueva Rutina', 
        elementos=[], 
        dificultad_total=0, 
        sexo='M'
        )

    def calcular_dificultad(self) -> int:
        dificultad_total = 0 
        trif_o_quad = 0
        for elem in self.rutina.elementos:
            dificultad_total += elem.dificultad
            if 'triffis' in elem.nombre.lower() or 'quadriffis' in elem.nombre.lower():
                trif_o_quad += 1
        if self.rutina.sexo == 'M':
            if trif_o_quad > 5:
                dificultad_total += (trif_o_quad - 5) * 3
        else:
            if trif_o_quad > 2:
                dificultad_total += (trif_o_quad - 2) * 3
        self.rutina.dificultad_total = dificultad_total

    def cambiar_sexo(self):
        self.rutina.sexo = 'F' if self.rutina.sexo == 'M' else 'M'


    def limite_elementos(self):
        if len(self.rutina.elementos) == 10:
            return False
        return True

    def agregar_elemento(self, item: Elemento):
        if self.limite_elementos:
            self.rutina.elementos.append(item)
            self.calcular_dificultad()
            # return f"{item.fig} agregado correctamente"
        # else:
            # Mostrar mensaje que ya no se pueden agregar mas elementos
            # return "Se alcanzo el limite de elementos en la rutina"
