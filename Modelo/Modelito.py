import json
import os

class NotasModel:
    def __init__(self, archivo='notas.json'):
        self.archivo = archivo
        self.notas = self._cargar_notas()

    def _cargar_notas(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as file:
                return json.load(file)
        else:
            return []

    def _guardar_notas(self):
        with open(self.archivo, 'w') as file:
            json.dump(self.notas, file)

    def crear_nota(self, nota):
        self.notas.append(nota)
        self._guardar_notas()

    def obtener_notas(self):
        return self.notas

    def actualizar_nota(self, indice, nueva_nota):
        self.notas[indice] = nueva_nota
        self._guardar_notas()

    def eliminar_nota(self, indice):
        del self.notas[indice]
        self._guardar_notas()
