# reservation.py
from observer import Subject


class ReservationNotificationSubject(Subject):
    def __init__(self, room, client):
        self.room = room
        self.client = client
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

class Reservation:
    def __init__(self, room, client):
        self.room = room
        self.client = client
        self.subject = ReservationNotificationSubject(self.room, self.client)

    def notify_staff(self):
        self.subject.notify_observers()