# class pai - superclass()
class pizzapadrao:
    def __init__(self, sabor, tamanho, preco, ingrediente):
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = preco
        self.ingrediente = ingrediente

    def mostrar_detalhes(self):
        print(f''' 
        ---detalhes da pizza---
            sabor: {self.sabor}
            tamanho: {self.tamanho}
            preco: {self.preco}
            ingrediente: {self.ingrediente}
            ''')

pizza_calabresa = pizzapadrao("calabresa","pequeno", 50.00, "tomate, oregano")
pizza_marguerita = pizzapadrao("marguerita","medio", 55.00, "tomate, oregano, queijo")

# pizza_calabresa.mostrar_detalhe()
# pizza_marguerita.mostrar_detalhe()