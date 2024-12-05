from animal import Animal  # Correção na importação

class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.__porte = porte  # Inicializa o atributo __porte diretamente no __init__

    def set_porte(self, porte):
        self.__porte = porte  # Define o valor do porte

    def get_porte(self):
        return self.__porte  # Retorna o valor do porte

    def mostrar(self):
        return f"Cachorro: Nome={self.get_nome()}, Idade={self.get_idade()}, Porte={self.get_porte()}"

