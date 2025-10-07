#Getter e Setter são métodos usados para acessar e modificar os atributos dentro de uma classe de forma controlada promovendo o "encapsulamento"
#Encapsulamento protegem a integridade dos dados de um objeto, impedinto o acesso dereto e modificações não autorizadas.

class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None  
        self.__info = None
        
    def setter(self, valor: int) -> None:
        self.__valor = valor  
        
    def getter(self) -> int:
        return self.__valor   


my_class = MinhaClasse()
#my_class.valor = 123 burlando o Encapsulamento
my_class.setter(42)
valor = my_class.getter()
print(valor)  # Saída: 42