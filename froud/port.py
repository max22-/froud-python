from itertools import cycle
import time
from froud.wire import Wire


class Inlet:
    def __init__(self):
        self.__wires = set()
        self.__iterator = cycle(self.__wires)

    def acceptwire(self, wire):
        self.__wires.add(wire)
        self.__iterator = cycle(self.__wires)

    def receive(self):
        if len(self.__wires) == 0:
            raise RuntimeError("Inlet not connected")
        while True:
            for i in range(len(self.__wires)):
                w = next(self.__iterator)
                if not w.empty():
                    return w.receive()
            time.sleep(0.01)


class Outlet:
    def __init__(self):
        self.__wire = None

    def acceptwire(self, wire):
        if self.__wire is not None:
            raise RuntimeError("Outlet already connected")
        self.__wire = wire

    def send(self, message):
        if self.__wire is None:
            raise RuntimeError("Outlet not connected")
        self.__wire.send(message)


def connect(outlet, inlet, capacity=0):
    wire = Wire(capacity)
    outlet.acceptwire(wire)
    inlet.acceptwire(wire)