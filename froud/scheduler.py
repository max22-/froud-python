class Scheduler:
    def __init__(self):
        self.__processes = set()

    def add(self, process):
        self.__processes.add(process)

    def start(self):
        for p in self.__processes:
            p.setup()
        for p in self.__processes:
            p.start()