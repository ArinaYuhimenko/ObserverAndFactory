# factory.py

from abc import ABC, abstractmethod

from reservation import Reservation, ReservationNotificationSubject
from room import StandardRoom, SuiteRoom

class AbstractFactory(ABC):
    @abstractmethod
    def create_room(self, number, capacity):
        pass

    @abstractmethod
    def create_reservation(self, room, client):
        pass

class StandardFactory(AbstractFactory):
    def create_room(self, number, capacity):
        room = StandardRoom(number, capacity)
        return room


    def create_reservation(self, room, client):
        reservation = Reservation(room, client)
        subject = ReservationNotificationSubject(room, client)
        reservation.subject = subject
        return reservation

class SuiteFactory(AbstractFactory):
    def create_room(self, number, capacity):
        room = SuiteRoom(number, capacity)
        return room

    def create_reservation(self, room, client):
        reservation = Reservation(room, client)
        reservation.notify_staff()
        return reservation