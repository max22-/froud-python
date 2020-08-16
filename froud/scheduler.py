class Scheduler:
    def __init__(self):
        self.__processes = set()

    def add(self, processes):
        self.__processes.update(processes)

    def start(self):
        for p in self.__processes:
            p.setup()
        for p in self.__processes:
            p.start()
        for p in self.__processes:
            p.join()