try: #são usados para tratar erros, trata de executar um codigo que pode dar erro 
    numero1 = float(input("Digite o primeiro número:")) 
    numero2 = int(input("Digite o segundo número:"))
    numero3 = int(input("Digite o terceiro número:"))
    numero4 = int(input("Digite o quarto número:"))
    print(f"Os numeros digitados foram: \n{numero1} \n{numero2} \n{numero3} \n{numero4}")
except ValueError:
    #codigo que será executado se der erro 
    print("\nEntrada invalida! Por favor,digire apenas numeros. ")