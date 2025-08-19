#inputs

email = input("escreva seu email: ") #o input e usado quando queremos receber dados do usuario
nome = input("escreva seu nome: ")
print(nome, email)
print(f"{nome}, verifique seu email para confirmação")

faturamento = float(input("Escreva o faturamento da empresa: ")) #float e usado para numeros com casa decimal
print(faturamento)

imposto = faturamento * 0.1
print(imposto)

#Lista

vendas = [100, 50, 15, 20, 30, 500, 150]
print(vendas)

#soma elementos da lista
total_vendas = sum(vendas) #sum e usado para somar todos os elementos de uma lista
print(total_vendas)

#tamanho da lista
quantidade_vendas = len(vendas) #len e usado para contar o numero de elementos em uma lista
print(quantidade_vendas)

#maximo e mínimo
print(max(vendas))
print(min(vendas)) 

# pegar uma posição da lista
print(vendas[0]) #primeiro elemento da lista
print(vendas[1]) #segundo elemento da lista          #o [] e usado para acessar um elemento especifico da lista
print(vendas[-1]) #ultimo elemento da lista

#verificar um elemento da lista
lista_produtos = ["iphone", "airpor", "ipad", "Macbook"]
print("apple wach" in lista_produtos) #o in e usado para verificar se um elemento esta na lista
print("ipad"in lista_produtos)

produto_procurado = input("Digite o nome do produto procurado: ")
produto_procurado = produto_procurado.lower()  #converte o texto para minusculo
print(produto_procurado in lista_produtos) #verifica se o produto procurado esta na lista

#adicionar um item a lista
lista_produtos.append("apple watch") #o append e usado para adicionar um elemento ao final da lista
lista_produtos.remove("ipad") #o remove e usado para remover um elemento da lista
lista_produtos.pop(0) #o pop e usado para remover o primeiro elemento da lista
print(lista_produtos)

#editar um item da lista
precos_produtos = [ 1000, 500, 2500, 1500]
precos_produtos  [0] = precos_produtos[0] * 1.6 #aumenta o preco do primeiro produto em 60%
print(precos_produtos) 

#contar quantas vezes um elemento aparece na lista
lista_produtos = ["iphone", "airpor", "ipad", "macbook", "iphone"]
print(lista_produtos.count("iphone")) #o count e usado para contar quantas vezes um elemento aparece na lista

#ordenar a lista
lista_produtos.sort() #o sort e usado para ordenar a lista em ordem alfabetica
lista_produtos.reverse() #o sort e usado para ordenar a lista em ordem alfabetica, o reverse inverte a ordem da lista
print(lista_produtos) 

precos_produtos.sort() #ordem crescente
precos_produtos.reverse() #ordem decrescente
print(precos_produtos)      

#e

