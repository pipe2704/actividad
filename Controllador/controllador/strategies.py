


class BaseStrategy:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def ejecutar(self):
        pass


class CrearNotaStrategy(BaseStrategy):
    def ejecutar(self):
        nota = self.view.solicitar_nota()
        self.model.crear_nota(nota)


class LeerNotasStrategy(BaseStrategy):
    def ejecutar(self):
        notas = self.model.obtener_notas()
        self.view.mostrar_notas(notas)


class ActualizarNotaStrategy(BaseStrategy):
    def ejecutar(self):
        indice = self.view.solicitar_indice()
        nueva_nota = self.view.solicitar_nota()
        self.model.actualizar_nota(indice - 1, nueva_nota)


class EliminarNotaStrategy(BaseStrategy):
    def ejecutar(self):
        indice = self.view.solicitar_indice()
        self.model.eliminar_nota(indice - 1)


class SalirStrategy(BaseStrategy):
    def ejecutar(self):
        exit()
