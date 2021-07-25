# from django.shortcuts import render
#
# cars = [
#     {"model": 'BMW', "year": 2020},
#     {"model": 'Audi', "year": 2010},
#     {"model": 'KIA', "year": 2008},
# ]
#
# def home(request):
#     return render(request, 'index.html', {'cars': cars})
#
# def add_car(request, model, year):
#     cars.append({'model': model, 'year': year})
#     return render(request, 'index.html', {'cars': cars})
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CarModel
from .serializers import CarSerializer

# class MyView(APIView):
#     def get(self, *args, **kwargs):
#         params = self.request.query_params
#         name = params.get('name')
#         print(name)
#         return Response('hello from get')
#
#     def post(self, *args, **kwargs):
#         return Response('hello from post')
#
#     def put(self, *args, **kwargs):
#         return Response('hello from put')
#
#     def patch(self, *args, **kwargs):
#         return Response('hello from patch')
#     def delete(self, *args, **kwargs):
#         return Response('hello from delete')
#
# class MyViewSecond(APIView):
#     def get(self, *args, **kwargs):
#         print(kwargs.get('id'))
#         return Response('Ok')


# lh:8000/cars GET all
# lh:8000/cars POST create
# lh:8000/cars/:id GET get one
# lh:8000/cars/:id PUT update all
# lh:8000/cars/:id PATCH update a few fields
# lh:8000/cars/:id DELETE delete item

class CarCreateListView(APIView):  # відповідає за доставання всього сипску і створення якогось нового
    def get(self, *args, **kwargs):  # дістати весь список
        qs = CarModel.objects.all() #query set сформує запит в БД
        serializer = CarSerializer(qs, many=True) # first parameter 'instance' - те, що вже збережено в БД, зараз це - qs,
        # many=True вказує, що буде багато об'єктів, масив, оскільки тягнемо всіх CarModel.objects.all()
        return Response(serializer.data)  # data - це вже сформований JSON

    def post(self, *args, **kwargs):
        body = self.request.data   # поле data в request, що надходить від користувача, містить тіло з даними, які будемо додавати в БД
        serializer = CarSerializer(data=body)
        if not serializer.is_valid(): # перевірка чи немає в отриманих даних від користувача помилки
            return Response(serializer.errors)
        serializer.save() #збереження перевірених даних в БД
        return Response(serializer.data)

class RetriaveDeleteVieiw(APIView):   # витягує і видаляє об'єкт по айді
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = CarModel.objects.get(pk=pk) #метод get в objects моделі витягує з БД завжди 1 об'єкт по заданому id (pk)
        except Exception as e:
            return Response('Not found')
        serializer = CarSerializer(data)
        return Response(serializer.data) #повертаємо запитувані дані

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = CarModel.objects.get(pk=pk)  # метод get в objects моделі витягує з БД завжди 1 об'єкт по заданому id (pk)
        except Exception as e:
            return Response('Not found')
        data.delete()
        return Response ('Deleted')




