import threading


class Process(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__stopFlag = False

    def run(self):
        while not self.__stopFlag:
            self.loop()

    def stop(self):
        self.__stopFlag = True

    def setup(self):
        pass

    def loop(self):
        pass
