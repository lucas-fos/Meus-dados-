# class filha - subclass()
from pizzapadrao import pizzapadrao
class pizzadoce(pizzapadrao):
    def __init__(self, sabor, tamanho, preco, ingrediente, borda_recheada):
        super().__init__(sabor, tamanho, preco, ingrediente)
        self.borda_recheada = borda_recheada

    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f''' 
        borda recheada: {self.borda_recheada}
        ''')

# crindo objetos
pizza_comum = pizzapadrao("calabresa", "familia", 29.90,"tomate, cebola")
pizza_chocolate = pizzadoce("chocolate com morango", "pequena", 31.90, "chocolate, morango","chocolate")

print(" --- pizza comum ---")
pizza_comum.mostrar_detalhes()
print(" --- pizza doce ---")
pizza_chocolate.mostrar_detalhes()
