lista_precos = [1900, 1000, 800, 3000]
 
#imposto
#aliquota 1 - IR - 0.2, se o preço produto foi até 2000, acima disso e 0.3 (30%)
#aliquota 2 - ISS - 0.15
#aliquota 3 - CSLL - 0.05

def calcula_imposto_total(preco):   #def definição
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco
    imposto_iss = 0.15 * preco 
    imposto_csll = 0.05 * preco 
    imposto_total = imposto_ir + imposto_csll + imposto_iss
    return imposto_total


for preco in lista_precos:
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco
    imposto_iss = 0.15 * preco 
    imposto_csll = 0.05 * preco 
    imposto_total = imposto_ir + imposto_csll + imposto_iss
    print(f"imposto total sobre o produto de R$ {preco} é de R$ {imposto_total}")
    
nova_lista_produtos = [3000, 5000, 6000, 7000]

for preco in nova_lista_produtos:
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco
    imposto_iss = 0.15 * preco 
    imposto_csll = 0.05 * preco 
    imposto_total = imposto_ir + imposto_csll + imposto_iss
    print(f"imposto total sobre o produto de R$ {preco} é de R$ {imposto_total}")
    