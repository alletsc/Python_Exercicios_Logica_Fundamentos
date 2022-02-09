class Fila:
    def __init__(self):
        self.fila = []

    def entrar(self, nome):
        self.fila.append(nome)

    def sair(self):
        self.fila.pop(0)

# dir(Fila)


supermercado = Fila()
loterica = Fila()
banco = Fila()

banco.entrar("stella")
supermercado.entrar("Jodi")
loterica.entrar("Rui")
