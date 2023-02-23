class DB:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Connect with DB: {self.user}, {self.user}, {self.port}')

    def close(self):
        print("Close connect with DB")

    def read(self):
        print('Read from DB')

    def write(self, data):
        print('Write to DB {data}')

    def __del__(self):
        DB.__instance = None


db1 = DB('root', '123', 5432)
db2 = DB('admin', '1234', 21017)

print(id(db1), id(db2))
