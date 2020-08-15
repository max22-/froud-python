import queue


class Wire:
    def __init__(self, capacity=0):
        self.__queue = queue.Queue(capacity)
        pass

    def send(self, message):
        self.__queue.put(message)

    def receive(self):
        return self.__queue.get()

    def empty(self):
        return self.__queue.empty()
