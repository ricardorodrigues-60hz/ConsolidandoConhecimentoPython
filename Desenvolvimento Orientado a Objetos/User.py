class User:
    #__init__ é o método construtor da classe,
    #  ele é chamado automaticamente quando um objeto da classe é criado.
    #  Ele é usado para inicializar os atributos do objeto.
    #self é uma referência ao objeto atual, e é usado para acessar os atributos e métodos do objeto.
    def __init__(self, nome, telefone, email, senha):

        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__senha = senha
    
    #métodos de acesso (getters) para os atributos privados
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        self.__senha = senha

    #método __str__ para representar o objeto como uma string
    def __str__(self):
        return f"User(nome={self.__nome}, telefone={self.__telefone}, email={self.__email})"