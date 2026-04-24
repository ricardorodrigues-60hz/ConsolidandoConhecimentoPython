class Account:
    def __init__(self, titular, numero, saldo, tipo, status):
        
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__tipo = tipo
        self.__status = status
    
    def get_titular(self):
        return self.__titular
    
    def get_numero(self):
        return self.__numero
    
    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_status(self):
        return self.__status

    def get_tipo(self):
        return self.__tipo
    
    def abrir_conta(self):
        self.__status = True

    def fechar_conta(self):
        self.__status = False
    



