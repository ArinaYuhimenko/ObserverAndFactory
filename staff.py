# staff.py

from observer import Observer

class StaffObserver(Observer):
    def update(self, reservation):
        room_details = str(reservation.room)
        client_details = str(reservation.client)
        print(f"Уведомление для сотрудников: Статус бронирования обновлен - Номер: {room_details}, Клиент: {client_details}")