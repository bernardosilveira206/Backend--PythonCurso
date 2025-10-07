#CONCEITOS INICIAIS BOO
# class MinhaClasse:
#     def __init__(self, info, elemento):
#         self.atributo_1 = "meu atributo"
#         self.atributo_2 = elemento
#         self.atributo_3 = [1, 2, "a"]
#         self.atributo_4 = info
#         print(self.atributo_4)
        
# def metodo_1(self):
#     print("minha acao1")
#     print("minha acao2")
#     print(self.atributo_2)
#     return "Olá mundo"

# def metodo_2(self, numero):
#     self.metodo_1()
#     print(self.atributo_3[1] + numero)
    
# minha_classe = MinhaClasse("informação", 213)

# minha_classe.metodo_2(3)


class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.__cpf = cpf
        
    def apresentar(self):
        print(f'Minha Altura - {self.altura}')
        self.__coletar_documento(   ) #pegamos a informação que esta privada
    
    def __coletar_documento(self): #definimos uma informação privada dentro da classe
        print(f'Meu documento - {self.__cpf}')
        

joao = Pessoa("1.80", "111.222.333-44")
joao.apresentar() #exibimos a informação que estava  através de outro metodo publico dentro da classe