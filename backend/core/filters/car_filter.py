from django_filters import rest_framework as filters

from core.models import CarModel


class CarFilter(filters.FilterSet):
    user = filters.BaseInFilter(field_name='userId') # фільтрація по входженню (чи є таке входження)
    brand = filters.CharFilter()
    year = filters.RangeFilter() # field_name не вказуємо, то буде за замовчуванням використовув. назку змінної year,
    # яка дорівнює назві поля в моделі
    # у query params при створенні запиту в Postman прописувати слід як
    # year_min та year_max

    class Meta:
        model = CarModel
        fields = ('brand', 'year', 'user')