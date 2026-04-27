class Main:
    pass

from User import User

from Account import Accont

user1 = User("Rafael", "11999999999", "rafael@example.com", "password123")
account1 = Accont(user1.get_nome(), "123456", 1000.0)

print(user1)
print(user1.get_nome())
print(user1.get_telefone())
print(user1.get_email())
print(user1.get_senha())

print(account1)
print(account1.get_titular())
print(account1.get_numero())
print(account1.get_saldo())

