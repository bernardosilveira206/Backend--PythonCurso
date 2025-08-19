#email_cliente = "milena@gmail.COM"
#minusculo
#email_cliente = email_cliente.upper()
#print(email_cliente)

#minusculo
#email_cliente = email_cliente.lower()
#print(email_cliente)

#@
#print(email_cliente.find("@")) #-1 quando não for encontrado

#tamanho do texto 
nome_cliente = 'Milena Baião'
#print(len(email_cliente)) #tamanho do email do cliente  
#print(len(nome_cliente)) #len -> contagem de caracteres

#pegar um caracter - solicitar entre []

#print(email_cliente[15])
#print(nome_cliente[5])
#print(nome_cliente[-2]) #solicitar caracter de trás pra frente
#print(nome_cliente[3]) #solicitar informação a partir de um ponto 
#print(nome_cliente[0:7]) #solicitar informação a partir de um certo ponto até outro ponto 

#replace = substutui uma informação dentro da string 
email_cliente = "milena@gmail.com"
#novo_email = email_cliente.replace("gmail.com","hotmail.com")
#print(novo_email)

#novo_nome = nome_cliente.replace("Milena","Flavia")
#print(novo_nome)

#novo_nome = nome_cliente.replace("Baião","Silveia")
#print(novo_nome)

#Maiusculas e minúsculas
nome = "bernardo silveira"

#print(nome.capitalize()) #primeira letra maiúscula e o resto minúsculo 
#print(nome.title()) #primeira letra de cada palavra maiúscula
#print(nome.upper()) #todas as letras maiúsculas
#print(nome.lower()) #todas as letras misnúsculas

#extrair informação de variáveis diferentes
#pevar servidor do email
#posicao_arroba= email_cliente.find("@")+1 #+1 para não pegar o @
#servidor = email_cliente[posicao_arroba:] 
#print(servidor) 

#pegar primeiro nome do cliente
posicao_espaco = nome.find(" ") #encontrar o espaço
primeiro_nome = nome[:posicao_espaco] #pegar o primeiro nome até o espaço
sobrenome = nome[posicao_espaco + 1 :] # +1 para não pegar o espaçp
print(primeiro_nome) #paga o primeiro nome
print(sobrenome) #pega o sobrenome