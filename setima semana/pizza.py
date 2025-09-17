class pizza:
    # atributos da classe(construtor padrao)
    def __init__(self, sabor, tamanho, preco):
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = preco
    
    # metodo nosso criado para descrever
    def descricao(self):
        return f"pizza de {self.sabor}, tamanho: {self.tamanho} preco:$ {self.preco:.2f}"
        

# criando objetos da classe pizza
pizza1 = pizza("calabressa","familia",52.00)
pizza2 = pizza("mussarela","media", 49.90)
print(pizza1.descricao())
print(pizza2.descricao())  