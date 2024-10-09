class Update:
    def __init__(self, serial_wrapper) -> None:
        self._serial_wrapper = serial_wrapper
    
    def install(self, fuf_file: str) -> None:
        if not fuf_file.endswith('.fuf'):
            raise AssertionError
        return self._serial_wrapper.send(f"update install {fuf_file}")
    
    def backup(self, dest_tar_file: str) -> None:
        if not dest_tar_file.endswith('.tar'):
            raise AssertionError
        return self._serial_wrapper.send(f"update backup {dest_tar_file}")
    
    def restore(self, bak_tar_file: str) -> None:
        if not bak_tar_file.endswith('.tar'):
            raise AssertionError
        return self._serial_wrapper.send(f"update restore {bak_tar_file}")