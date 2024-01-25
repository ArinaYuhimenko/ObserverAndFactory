from client import Client
from factory import StandardFactory, SuiteFactory
from staff import StaffObserver

def main():
    # Создаем клиента
    client1 = Client("Вася Пупкин")
    client2 = Client("Петя Пупкин")

    # Создаем фабрики
    standard_factory = StandardFactory()
    suite_factory = SuiteFactory()

    # Создаем комнаты
    standard_room = standard_factory.create_room(101, 2)
    suite_room = suite_factory.create_room(201, 4)

    # Создаем резервацию
    standard_reservation = standard_factory.create_reservation(standard_room, client1)
    suite_reservation = suite_factory.create_reservation(suite_room, client2)

    # Создаем наблюдателя
    staff_observer = StaffObserver()

    # Присоединяем наблюдателя к резервации
    standard_reservation.subject.attach(staff_observer)
    suite_reservation.subject.attach(staff_observer)

    # Проверяем работу кода
    print("Reservation notifications:")
    standard_reservation.notify_staff()
    suite_reservation.notify_staff()

if __name__ == "__main__":
    main()