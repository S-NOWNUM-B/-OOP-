from abc import ABC, abstractmethod

class DatabaseInterface(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query: str):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class MySQLDatabase(DatabaseInterface):

    def __init__(self):
        self.connection = None

    def connect(self):
        if self.connection is None:
            print("Подключение к MySQL...")
            self.connection = "MySQL Connection"

    def execute_query(self, query: str):
        if self.connection is None:
            raise ConnectionError("Нет соединения с MySQL")
        print(f"Выполнение запроса в MySQL: {query}")
        return "Результат MySQL"

    def disconnect(self):
        if self.connection:
            print("Отключение от MySQL...")
            self.connection = None

class PostgreSQLDatabase(DatabaseInterface):

    def __init__(self):
        self.connection = None

    def connect(self):
        if self.connection is None:
            print("Подключение к PostgreSQL...")
            self.connection = "PostgreSQL Connection"

    def execute_query(self, query: str):
        if self.connection is None:
            raise ConnectionError("Нет соединения с PostgreSQL")
        print(f"Выполнение запроса в PostgreSQL: {query}")
        return "Результат PostgreSQL"

    def disconnect(self):
        if self.connection:
            print("Отключение от PostgreSQL...")
            self.connection = None

class DatabaseConnection:

    _instance = None

    def __new__(cls, database: DatabaseInterface):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.database = database
            cls._instance.database.connect()
        return cls._instance

    def execute_query(self, query: str):
        return self.database.execute_query(query)

    def disconnect(self):
        if self.database:
            self.database.disconnect()
        DatabaseConnection._instance = None

print("--- Использование MySQLDatabase ---")
mysql_db = MySQLDatabase()
db_connection1 = DatabaseConnection(mysql_db)
print(db_connection1.execute_query("SELECT * FROM users"))
db_connection1.disconnect()

print("\n--- PostgreSQLDatabase ---")
pg_db = PostgreSQLDatabase()
db_connection2 = DatabaseConnection(pg_db)
print(db_connection2.execute_query("SELECT * FROM orders"))
db_connection2.disconnect()