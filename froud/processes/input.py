import evdev
import froud


"""Sends 1 or -1 on the output port"""
class Encoder(froud.Process):
    def __init__(self, devicepath):
        froud.Process.__init__(self)
        self.__devicePath = devicepath
        self.outp = froud.Outlet()

    def run(self):
        device = evdev.InputDevice(self.__devicePath)
        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_REL:
                self.outp.send(event.value)


"""Sends (key_code, "pressed") or (key_code, "released") on the output port"""
class Keypad(froud.Process):
    def __init__(self, devicePath):
        froud.Process.__init__(self)
        self.__devicePath = devicePath
        self.outp = froud.Outlet()

    def run(self):
        device = evdev.InputDevice(self.__devicePath)
        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                if event.value == 0:
                    self.outp.send((event.code, "released"))
                else:
                    self.outp.send((event.code, "pressed"))