from rest_framework.pagination import LimitOffsetPagination # обмеженняПропуск для пагінації
from rest_framework.response import Response


class CarPagination(LimitOffsetPagination):
    max_limit = 1000  # встановлення максимального ліміту виведення, який може запитати користувач

    def get_paginated_response(self, data): #перевизначаємо відображення виведенеих елеиентів при пагінації
        return Response({
            'link': {
                'next': self.get_next_link(),
                'prev': self.get_previous_link()
            },
            'count': self.count,
            'data': data
        })