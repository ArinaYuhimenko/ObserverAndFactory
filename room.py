# room.py

from abc import ABC, abstractmethod


class Room(ABC):
    @abstractmethod
    def book(self):
        pass

    @abstractmethod
    def cancel_booking(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class StandardRoom(Room):
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity

    def book(self):
        # Логика бронирования обычного номера
        pass

    def cancel_booking(self):
        # Логика отмены бронирования обычного номера
        pass

    def __str__(self):
        return f"Стандарт #{self.number} Количество персон - {self.capacity}"

class SuiteRoom(Room):
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity

    def book(self):
        #Логика бронирования люксового номера
        pass

    def cancel_booking(self):
        # Логика отмены бронирования люксового номера
        pass

    def __str__(self):
        return f"Люкс #{self.number} Количество персон - {self.capacity}"