from abc import ABC, abstractmethod

class State(ABC):
    def start(self) -> None: pass
    def stop(self) -> None: pass
    def log(self) -> None: pass