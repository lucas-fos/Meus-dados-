# 1.  ,exibir_cardapio()`:** Esta função deve criar o dicionário do cardápio e usar um loop `for` para imprimi-lo na tela.
# 2.  ,receber_pedido()`:** Esta função deve conter o loop `while` que recebe os sabores do cliente e os armazena em uma lista. Ela deve **retornar** a lista de pedidos.
# 3.  ,calcular_total()`:** Esta função deve receber a lista de pedidos e o dicionário do cardápio como **parâmetros**. Ela deve calcular o valor total e **retornar** o resultado.
# 4.  ,Execute o fluxo:** No código principal, chame as funções na ordem correta para simular o processo de pedido: `exibir_cardapio()`, `receber_pedido()`, `calcular_total()` e, por fim, imprima o total final.

#criação da função exibir cardapio()
def exibir_cardapio():
    cardapio = {
    "Mussarela": 30.00,
    "Calabresa": 32.00,
    "Pepperoni": 35.00,
    "Quatro Queijos": 38.00,
    "Frango com Catupiry": 40.00
        }
    print("--- Cardápio da Pizzaria Sabores ---")
    for pizza, preco in cardapio.items():
        print(f"🍕 {pizza}: R$ {preco:.2f}")
    return cardapio

#criação da fumçao receber_pedido()
def receber_pedido(cardapio):
    pedido = [] 
    while True:
        sabor = input("digite o sabor da pizza (ou sair para finalizar)")
        if sabor == "sair":
            break
        elif sabor in cardapio:
            pedido.append(sabor)
            print(f"🍕{sabor} adicionado ao pedido!")
        else:
            print("esse sabor nao esta disponivel. escolha outro sabor.")
    return pedido

#criação da função calcular_total()
def calcular_total(pedido,cardapio):
    total = 0
    for pizza in pedido:
        total += cardapio[pizza]
    return total
    

# criação da função main()
def main():
    cardapio = exibir_cardapio()
    pedido = receber_pedido(cardapio)
    total = calcular_total(pedido, cardapio)
    
    print("🛒 resumo do pedido")
    for pizza in pedido:
        print(f"💰{pizza} - R$ {cardapio[pizza]}")
    print(f"💵 total a pagar: R$ {total:.2f}")


# Executar o programa
main()