# 1. crie um programa que aceite pedidos de um e-commerce ate que o cliente digite sair.
print("faça o seu pedido ou digite 'sair' para encerrar") 
pedido = "" #string porque 'sair' e um texto.
lista = ["samrtephone", "smarttv", "geladeira", "fogao", "notebook"]

while pedido.lower() != "sair":
    pedido = input("digite um produto da lista:")
    if pedido in lista: 
        print(f"➡️ {pedido} adicionado ao seu carrinho!")
    elif pedido.lower() == "sair"
    print("🛒pedido encerrado")
    else:
        print("esse produto nao esta na lista . escolha outro:")
    