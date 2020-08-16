import froud
import time


class Timer(froud.Process):
    def __init__(self):
        froud.Process.__init__(self)
        self.output = froud.Outlet()

    def loop(self):
        self.output.send("Hello, world!")
        time.sleep(1)


class Printer(froud.Process):
    def __init__(self):
        froud.Process.__init__(self)
        self.input = froud.Inlet()

    def loop(self):
        print(self.input.receive())


if __name__ == '__main__':
    t = Timer()
    p = Printer()
    froud.connect(t.output, p.input)
    s = froud.Scheduler()
    s.add(t)
    s.add(p)
    s.start()
    while True:
        pass

