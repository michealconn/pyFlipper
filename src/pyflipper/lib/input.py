from .threaded import Threaded

class Input(Threaded):
    KEYS = ['up', 'down', 'left', 'right', 'back', 'ok']
    TYPES = ['press', 'release', 'short', 'long']

    def __init__(self, serial_wrapper) -> None:
        self._serial_wrapper = serial_wrapper

    def dump(self, timeout: int = 10) -> str:
        self.exec(func=None, timeout=timeout)
        return self._serial_wrapper.send("input dump")
    
    def send(self, key: str, type: str) -> None:
        if key not in self.KEYS:
            raise AssertionError(f"key must be in {self.KEYS}")
        if type not in self.TYPES:
            raise AssertionError(f"type must be in {self.TYPES}")
        #FIXME:
        self._serial_wrapper.send(f"input send {key} {type}")
    
