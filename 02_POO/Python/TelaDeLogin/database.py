import datetime 

class Database:
    def __init__(self, file_name):
        self.file_name = file_name
        self.users = None
        self.file = None
        self.load_users()

    def load_users(self):
        self.file = open(self.file_name, 'r')
        self.users = { }

        for line in self.file:
            user, password, email, created_at = line.strip().split(',')
            self.users[email] = (password, user, created_at)

        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1
        
    def add_user(self, user, password, email):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), user.strip(), Database.get_date())
            self.save()
            return 1
        else:
            print('Email já cadastrado')
            return -1
        
    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.user[email][0] == password
        else:
            return False
    
    def save(self):
        with open(self.file_name, 'w') as file:
            for user in self.users:
                password, name, created_at = self.users[user]
                file.write(f'{name},{password},{user},{created_at}\n')
    
    @staticmethod
    def get_date():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')