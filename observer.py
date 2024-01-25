# observer.py

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, reservation):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass