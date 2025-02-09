class User:
    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    def __eq__(self, other):
        if isinstance(other, User):
            return self._email == other._email
        return False

    def __hash__(self):
        return hash(self._email)

    def __repr__(self):
        return f"User: {self._username}, email: {self._email}, password: {self._password}"

class UserDatabase:
    def __init__(self):
        self.users = set()

    def add_user(self, user: User):
        if user in self.users:
            print(f"User {user.username} already exists!")
        else:
            self.users.add(user)
            print(f"User {user.username} added!")

    def has_user(self, user: User):
        return user in self.users

    def __repr__(self):
        return f"UserDatabase({list(self.users)})"

db = UserDatabase()

user1 = User("SNOWNUB", "dfvhj@gmail.com", "11322dhbf")
user2 = User("Stas", "fhb@gmail.com", "123456")
user3 = User("Jim", "hrngtjfv.com", "1")

db.add_user(user1)
db.add_user(user2)
db.add_user(user3)
db.add_user(user1)

print("\nСписок пользоватлей в базе:")
print(db)

print("\nПроверка наличия пользователей:")
print(f"SNOWNUMB в базе? {"да" if db.has_user(user1) else "нет"}")
print(f"Stas в базе? {"Yes" if db.has_user(user2) else "No"}")
print(f"Kenedi в базе? {"Yes" if db.has_user(User("Kenedi", "KenediTheBestBoss1@gmail.com", "TheBestWorldAndUSABoss")) else "No"}")

print("\nВсе пользователи в базе данных:")
for User in db.users:
    print(f"User: {User.username}, email: {User.email}")