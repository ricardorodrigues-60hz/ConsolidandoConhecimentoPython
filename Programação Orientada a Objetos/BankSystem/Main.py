class Main:
    pass

from user import User

from account import Account

def print_account_info(account):
    print("-" * 30)
    print(f"Titular: {account.get_titular()}")
    print(f"Número: {account.get_numero()}")
    print(f"Saldo: {account.saldo}")
    print(f"Tipo: {account.get_tipo()}")
    print(f"Status: {'Ativa' if account.get_status() else 'Fechada'}")
    print("-" * 30)

user1 = User("Rafael", "11999999999", "rafael@example.com", "password123")
account1 = Account(user1.get_nome(), "123456", 1000.0, "Corrente", True)
print_account_info(account1)

account1.depositar(account1.get_status(), 500.0)
print_account_info(account1)
account1.sacar(account1.get_status(), account1.saldo, 200.0)
print_account_info(account1)
account1.pagar_mensalidade(account1.get_tipo(), account1.get_status(), account1.saldo)
print_account_info(account1)

user2 = User("Maria", "11988888888", "maria@example.com", "password456")
account2 = Account(user2.get_nome(), "654321", 2000.0, "Poupança", True)
print_account_info(account2)

account2.depositar(account2.get_status(), 300.0)
print_account_info(account2)
account2.sacar(account2.get_status(), account2.saldo, 100.0)
print_account_info(account2)
account2.pagar_mensalidade(account2.get_tipo(), account2.get_status(), account2.saldo)
print_account_info(account2)
