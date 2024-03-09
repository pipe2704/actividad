from Modelo.Modelito import NotasModel
from vista.vistica import NotasView
from Controllador.controllador.notas import NotasController


def crear_aplicacion():
    model = NotasModel()
    view = NotasView()
    controller = NotasController(model, view)
    return controller


if __name__ == "__main__":
    app_ = crear_aplicacion()
    app_.ejecutar()
