class Account:
    #__init__ método construtor da classe,
    #  ele é chamado automaticamente quando um objeto da classe é criado.
    #  Ele é usado para inicializar os atributos do objeto.
    #  self é uma referência ao objeto atual, e é usado para acessar os atributos e métodos do objeto.
    def __init__(self, titular: str, numero: int, saldo: float, tipo: str, status: bool = False):        
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__tipo = tipo
        self.__status = status
        ##adicionar o atributo Stack para armazenar histórico de transações, definir metodos extrato.
        #buscar opcoes para banco de dados para armazenar as contas e transações,
        #implementar autenticação de usuário, adicionar funcionalidades como transferência entre contas, etc. 

    #método __str__ para representar o objeto como uma string
    def __str__(self):
        return (f"{'-' * 30}\n"
                f"Titular: {self.__titular}\n"
                f"Número: {self.__numero}\n"
                f"Saldo: {self.__saldo}\n"
                f"Tipo: {self.__tipo}\n"
                f"Status: {'Ativa' if self.__status else 'Fechada'}\n"
                f"{'-' * 30}")

    #Métodos Especiais de acesso (getters e setters) para os atributos privados

    def set_titular(self, titular: str):
        self.__titular = titular
    
    def get_titular(self) -> str:
        return self.__titular
    
    def set_numero(self, numero: int):
        self.__numero = numero
    
    def get_numero(self) -> int:
        return self.__numero


    #@property e @saldo.setter são decoradores que permitem acessar o saldo como um atributo,
    #mas na verdade estão chamando os métodos get_saldo e set_saldo respectivamente.
    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo: float):
        if saldo < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self.__saldo = saldo

    def set_status(self, status: bool):
        self.__status = status

    def get_status(self) -> bool:
        return self.__status
    
    def set_tipo(self, tipo: str):
        self.__tipo = tipo

    def get_tipo(self) -> str:
        return self.__tipo
    

    #Métodos específicos para operações bancárias

    def abrir_conta(self):
        self.__tipo = self.__tipo
        self.__status = True
        if self.__tipo == "CC":
            self.__saldo = 50.0
        elif self.__tipo == "CP":
            self.__saldo = 150.0
        else:
            raise ValueError("Tipo de conta inválido. Use 'CC' para conta corrente ou 'CP' para conta poupança.")

    def fechar_conta(self):
        if self.__saldo > 0:
            raise ValueError("A conta ainda tem dinheiro. Retire o dinheiro antes de fechar a conta.")
        elif self.__saldo < 0:
            raise ValueError("A conta está em débito. Pague o débito antes de fechar a conta.")
        else:
            self.__status = False
        
    
    def depositar(self, valor: float):
        if not self.__status:
            raise ValueError("A conta está fechada. Não é possível fazer depósitos.")
        self.__saldo += valor

    def sacar(self, valor: float):
        if not self.__status:
            raise ValueError("A conta está fechada. Não é possível fazer saques.")
        if self.__saldo < valor:
            raise ValueError("Saldo insuficiente para realizar o saque.")
        self.__saldo -= valor

    def pagar_mensalidade(self):
        if self.__tipo == "CC":
            valor = 12.0
        elif self.__tipo == "CP":
            valor = 20.0
        else:
            raise ValueError("Tipo de conta inválido. Use 'CC' para conta corrente ou 'CP' para conta poupança.")
        if not self.__status:
            raise ValueError("A conta está fechada. Não é possível pagar a mensalidade.")
        if self.__saldo < valor:
            raise ValueError("Saldo insuficiente para pagar a mensalidade.")
        self.__saldo -= valor

        
    



