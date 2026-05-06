class Main:
    pass

from user import User

from account import Account

user1 = User("Rafael", "11999999999", "rafael@example.com", "password123")
account1 = Account(user1.get_nome(), "123456", 1000.0, "CC", True)
print(account1)

account1.depositar(500.0)
print(account1)
account1.sacar(200.0)
print(account1)
account1.pagar_mensalidade()
print(account1)

user2 = User("Maria", "11988888888", "maria@example.com", "password456")
account2 = Account(user2.get_nome(), "654321", 2000.0, "CP", True)
print(account2)

account2.depositar(300.0)
print(account2)
account2.sacar(100.0)
print(account2)
account2.pagar_mensalidade()
print(account2)

account1.sacar(1288.0)
account2.sacar(2180.0)
print(account1)
print(account2)

account1.fechar_conta()
print(account1)
account2.fechar_conta()
print(account2)

