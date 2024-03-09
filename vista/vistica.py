class NotasView:
    def mostrar_notas(self, notas):
        print("Lista de notas:")
        for i, nota in enumerate(notas):
            print(f"{i + 1}. {nota}")
        print()

    def solicitar_nota(self):
        return input("Ingrese la nueva nota: ")

    def solicitar_indice(self):
        return int(input("Ingrese el índice de la nota: "))
