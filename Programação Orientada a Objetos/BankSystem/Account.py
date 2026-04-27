class Account:
    def __init__(self, titular: str, numero: int, saldo: float, tipo: str, status: bool = False):
        
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__tipo = tipo
        self.__status = status

    
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

    def abrir_conta(self, tipo: str):
        self.__tipo = tipo
        self.__status = True
        if tipo == "CC":
            self.__saldo = 50.0
        elif tipo == "CP":
            self.__saldo = 150.0
        else:
            raise ValueError("Tipo de conta inválido. Use 'CC' para conta corrente ou 'CP' para conta poupança.")

    def fechar_conta(self, saldo: float):
        if self.__saldo > 0:
            raise ValueError("A conta ainda tem dinheiro. Retire o dinheiro antes de fechar a conta.")
        elif self.__saldo < 0:
            raise ValueError("A conta está em débito. Pague o débito antes de fechar a conta.")
        else:
            self.__status = False
        
    
    def depositar(self, status: bool, valor: float):
        if not status:
            raise ValueError("A conta está fechada. Não é possível fazer depósitos.")
        self.__saldo += valor

    def sacar(self, status: bool, saldo: float, valor: float):
        if not status:
            raise ValueError("A conta está fechada. Não é possível fazer saques.")
        if saldo < valor:
            raise ValueError("Saldo insuficiente para realizar o saque.")
        self.__saldo -= valor

    def pagar_mensalidade(self, tipo: str, status: bool, saldo: float):
        if tipo == "CC":
            valor = 12.0
        elif tipo == "CP":
            valor = 20.0
        else:
            raise ValueError("Tipo de conta inválido. Use 'CC' para conta corrente ou 'CP' para conta poupança.")
        if not status:
            raise ValueError("A conta está fechada. Não é possível pagar a mensalidade.")
        if saldo < valor:
            raise ValueError("Saldo insuficiente para pagar a mensalidade.")
        self.__saldo -= valor


    



