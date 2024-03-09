from Controllador.controllador.strategies import CrearNotaStrategy, LeerNotasStrategy, ActualizarNotaStrategy, EliminarNotaStrategy, SalirStrategy


class NotasController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.operaciones = self._crear_operaciones()

    def _crear_operaciones(self):
        return {
            '1': CrearNotaStrategy(self.model, self.view),
            '2': LeerNotasStrategy(self.model, self.view),
            '3': ActualizarNotaStrategy(self.model, self.view),
            '4': EliminarNotaStrategy(self.model, self.view),
            '5': SalirStrategy(self.model, self.view)
        }

    def ejecutar(self):
        while True:
            print("Seleccione una operación:")
            print("1. Crear nota")
            print("2. Leer notas")
            print("3. Actualizar nota")
            print("4. Eliminar nota")
            print("5. Salir")

            opcion = input("Opción: ")

            if opcion in self.operaciones:
                self.operaciones[opcion].ejecutar()
            else:
                print("Opción no válida. Inténtelo de nuevo.")
