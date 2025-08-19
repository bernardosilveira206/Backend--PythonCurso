#EXPLICAÇÃO 2: for/loop
#for i in range(10):#sinaliza quantas vezes uma ação deve ser repetida
#    print("Loop do python")

lista_vendas = [1000, 500, 800, 2000, 2300]
meta = 1200
percentual_bonus = 0.1

#for item in lista_vendas:#escreve todos os itens da lista (o nome item, da varivel, pode ser qualquer outro)
#    print(item)

#for venda in lista_vendas: #de acordo com a lista, verifica um por um e calcula o bonus dentro da condição
#    if venda >= meta:
#        bonus = percentual_bonus * venda
#    else:
#        bonus = 0
#    print("Bonus: ", bonus)

#EXPLICAÇÃO 3: dicionarios - assimilar uma lista com a outra
lista_produtos = ["arroz", "feijão", "macarrão", "farinha"]
precos = [20, 10, 5, 2]

#dic_produtos = {"chave": valor, "chave2": valor2...}
dic_produtos = {"arroz": 20, "feijão": 10, "macarrão": 5, "farinha": 2}

#pegar um elemento dentro da lista do dicionário e mostra o valor correlacionado
#print(dic_produtos["arroz"])

#quantidade de itens da lista
#print(len(dic_produtos))

#editar elemento
#dic_produtos["feijão"] = dic_produtos["feijão"] * 1.3
#print(dic_produtos)

#retirar um item
#dic_produtos.pop("farinha")
#print(dic_produtos)

#adicionar um item
#dic_produtos["café"] = 40
#print(dic_produtos)

#verificar se um item existe no dicionário
#if "arroz" in dic_produtos:
#    print ("Existe o produto")
#else:
#    print("Não existe")

#verificar se um valor existe nos valores do dicionário
#if 50 in dic_produtos.values():
#    print("Existe")
#else:
#    print("Não existe")