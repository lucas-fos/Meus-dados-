# 1. **Exiba um cardápio:** Crie um **dicionário** para armazenar o cardápio da pizzaria, contendo pelo menos 5 sabores e seus respectivos preços (por exemplo, `{"Mussarela": 30.00, "Calabresa": 32.00}`).
# 2. **Receba o pedido:** Use um **loop `while`** para permitir que o cliente adicione vários sabores ao pedido. O loop deve continuar até que o cliente digite "sair". Armazene os sabores escolhidos em uma **lista**.
# 3. **Calcule o total:** Percorra a lista de pedidos com um **loop `for`** e calcule o valor total a ser pago, somando os preços de cada pizza com base no dicionário do cardápio.
# 4. **Imprima o resumo:** Ao final do pedido, imprima um resumo formatado, mostrando cada pizza pedida e o valor total final.

# 1. crie um dicionario (dict) para o cardapio
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

# 2. recebe o pedido do cliente com um loop while.
while True:
    sabor_escolhido = input("escolha um sabor:")
    if  sabor_escolhido == "sair":
        break # encerra o loop quando o cliente digite 'sair'
    elif sabor_escolhido in cardapio:
        pedido.append(sabor_escolhido)
        print(f"🍕{sabor_escolhido} adicionado ao seu pedido!")
    else:
        print("❌esse saobor nao esta no cardapio. escplha outro.")


#  3. calcule o total do pedido com um loop while.
total = 0 
for sabor in pedido:
    total += cardapio[sabor]

# 4. imprimir o resumo
print("--- resumo do pedido---")
if pedido: #verifica se existi algum valor em pedido
    for sabor in pedido:
        print(f"➡️ {sabor}: R$ {cardapio[sabor]:.2f}") #devolver o valor do sabor da pizza se ela estiver no dicionari cardapio.
    print(f"total a pagar: R${total:.2f}")
else:
    print("❌nehuma pizza foi pedido. volte sempre.")