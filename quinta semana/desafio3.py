# 1. **Crie uma função `exibir_cardapio()`:** Esta função deve criar o dicionário do cardápio e usar um loop `for` para imprimi-lo na tela.
# 2. **Crie uma função `receber_pedido()`:** Esta função deve conter o loop `while` que recebe os sabores do cliente e os armazena em uma lista. Ela deve **retornar** a lista de pedidos.
# 3. **Crie uma função `calcular_total()`:** Esta função deve receber a lista de pedidos e o dicionário do cardápio como **parâmetros**. Ela deve calcular o valor total e **retornar** o resultado.
# 4. **Execute o fluxo:** No código principal, chame as funções na ordem correta para simular o processo de pedido: `exibir_cardapio()`, `receber_pedido()`, `calcular_total()` e, por fim, imprima o total final.

# 1. funçao para exibir o cardapio
def exibir_cardapio():
    cardapio = {
        "mussarela":30.00,
        "calabresa":32.00,
        "pepperoni":35.00,
        "quatro queijo":38.00,
        "frango com catupiry":40.00
    }
    pedido =[] #lista vazia
    print("🍕bem vindo a pizzaria sabores!")
    print("faça seu pedido (digite sair para encerrar):")
    for sabor, preco in cardapio.items():
        print(f"{sabor.caprd()}: R$ {preco:.2f}")
    return cardapio # retorna o dicionário para ser usado em outras funções

   # 2. Função para receber o pedido
def receber_pedido(cardapio):
    pedido = []
    print("\nfaça seu pedido (digite 'sair' para encerrar):")
    while True:
        sabor_escolhido = input("escolha um sabor:")
        if  sabor_escolhido == "sair":
            break # encerra o loop quando o cliente digite 'sair'
        elif sabor_escolhido in cardapio:
            pedido.append(sabor_escolhido)
            print(f"🍕{sabor_escolhido} adicionado ao seu pedido!")
        else:
            print("❌esse saobor nao esta no cardapio. escplha outro.")


   # 3. Função para calcular o total
def calcular_total(pedido, cardapio):
    total = sum(cardapio[sabor] for sabor in pedido)
    return total

    # 4. Fluxo principal
cardapio = exibir_cardapio()
pedido = receber_pedido(cardapio)
total = calcular_total(pedido, cardapio)

print("--- resumo do pedido---")
if pedido: #verifica se existi algum valor em pedido
    for sabor in pedido:
        print(f"➡️ {sabor}: R$ {cardapio[sabor]:.2f}") #devolver o valor do sabor da pizza se ela estiver no dicionari cardapio.
    print(f"total a pagar: R${total:.2f}")
else:
    print("❌nehuma pizza foi pedido. volte sempre.")