class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1,
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


th1 = ThreadData()
print(th1.__dict__)  # return {'name': 'thread_1', 'data': {}, 'id': 1}
th2 = ThreadData()
print(th2.__dict__)  # return {'name': 'thread_1', 'data': {}, 'id': 1}
th2.id = 2
print(th2.id)  # return 2
print(th1.id)  # return 2

th1.new_attr = 'new_attr'
print(th2.new_attr)  # return 'new_attr'
