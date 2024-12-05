class Animal:
    def __init__(self, nome, idade):
        self.__nome = nome  # Atributo nome
        self.__idade = idade  # Atributo idade

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_idade(self, idade):
        self.__idade = idade

    def get_idade(self):
        return self.__idade
