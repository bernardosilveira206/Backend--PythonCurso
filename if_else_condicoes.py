vendas = 1500
meta = 1300   

# > maior que
# < menor que
# >= maior ou igual a
# <= menor ou igual a
# == igual a
# != diferente de

if vendas > meta:
    print("vendedor ganha bonus")
    print("Bateu a meta de vendas")
    bonus = 0.1 * vendas     #vendedor ganha 10% da venda 
    print("Bonus do vendedor", bonus)
else:
    print("vendedor não ganha bonus")
    print("Não ganhou a meta de vedas")

#if codicao/cpmparação:
    #tudo que acontece se a condição for verdadeira
    #outras condiçoes
#else condicao/comparação:
    #tudo que acontece se a condição for falsa
    #outras condiçoes
    
#cenário 2
vendas = int(input("Digite o valor das vendas: ")) #pede para iserir o valor da venda para calcular os bonus
vendas_empresa = int(input("Digite o valor das empresarias: ")) 
meta_empresa = 1800
meta1 = 1300 # se bater a meta 1 ganha 10%
meta2 = 2000 # se bater a meta 2 ganha 13%
meta3 = 2500 # se bater a meta 3 gahnha 15

if vendas >= 2000:
    bonus = 0.13 * vendas
else:
    if vendas >= 1300:
        bonus = 0.1 * vendas
    else:
        bonus = 0
print("Exemplo 2, ele ganha um Bonus:", bonus)

#elif O comando elif é uma combinação das palavras-chave “else” e “if”. Ele permite testar múltiplas condições encadeadas, ou seja, verifica se uma condição é verdadeira e, caso contrário, verifica a próxima condição e assim por diante. 
if vendas >= 2500 and vendas_empresa >= meta_empresa: #and verifica se duas condições são verdadeiras simultaneamente
    bonus = 0.15 * vendas
elif vendas >= 2000 and vendas_empresa >= meta_empresa:
    bonus = 0.13 * vendas
elif vendas >= 1300 and vendas_empresa >= meta_empresa:
    bonus = 0.1 * vendas
else:
    bonus = 0
print("bonus:", bonus)

lista_produtos = ["airpod", "ipad", "iphone", "macbook"]
produto_procurado = input("Procure um produto: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print("produto em estoque")
else:
    print("não temos este produto")