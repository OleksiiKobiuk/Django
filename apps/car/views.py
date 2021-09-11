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
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from core.models import CarModel
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

class CarCreateListView(ListCreateAPIView):  # відповідає за доставання всього сипску і створення якогось нового
    serializer_class = CarSerializer
    # queryset = CarModel.objects.all()

    def get_queryset(self):
        qs = CarModel.objects.all()
        params = self.request.query_params
        user_id = params.get('userId', None) # для пошуку авто по id юзера, типу GET localhost:8000/api/v1/cars?userId=1
        if user_id:
            qs = qs.filter(user_id=user_id)
        return qs


# class CarCreateListView(GenericAPIView, ListModelMixin, CreateModelMixin):  # відповідає за доставання всього сипску і створення якогось нового
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)


    # def get(self, *args, **kwargs):  # дістати весь список
        # qs = CarModel.objects.all() #query set сформує запит в БД
        # serializer = CarSerializer(qs, many=True) # first parameter 'instance' - те, що вже збережено в БД, зараз це - qs,
        # # many=True вказує, що буде багато об'єктів, масив, оскільки тягнемо всіх CarModel.objects.all()
        # return Response(serializer.data)  # data - це вже сформований JSON

        # qs = CarModel.objects.all().filter(year__gt=2015)
        # qs = qs.filter(model__iexact='nissan')
        # print(qs)
        # return Response('')

        # qs = CarModel.objects.all()
        # brand = self.request.query_params.get('brand', None)
        # year = self.request.query_params.get('year', None)
        # if brand:
        #     qs = qs.filter(brand__iexact=brand)
        # if year:
        #     qs = qs.filter(year__gte=year)
        # serializer = CarSerializer(qs, many=True).data
        # return Response(serializer, status.HTTP_200_OK)

    # def post(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # def post(self, *args, **kwargs):
    #     body = self.request.data   # поле data в request, що надходить від користувача, містить тіло з даними, які будемо додавати в БД
    #     serializer = CarSerializer(data=body)
    #     if not serializer.is_valid(): # перевірка чи немає в отриманих даних від користувача помилки
    #         return Response(serializer.errors)
    #     serializer.save() #збереження перевірених даних в БД
    #     return Response(serializer.data)

class RetriaveUpdDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel
    lookup_field = 'id'

    # def get_object(self):
    #     return CarModel.objects.get(pk=6)

# class RetriaveUpdDeleteView(GenericAPIView):   # витягує і видаляє об'єкт по айді
#     def get(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         try:
#             data = CarModel.objects.get(pk=pk) #метод get в objects моделі витягує
#             # з БД завжди 1 об'єкт по заданому id (pk)
#         except Exception as e:
#             return Response('Not found')
#         serializer = CarSerializer(data)
#         return Response(serializer.data) #повертаємо запитувані дані
#
#     def patch(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         instance = get_object_or_404(CarModel, pk=pk)
#         serializer = CarSerializer(instance, self.request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, *args, **kwargs):
#         # pk = kwargs.get('pk')
#         # try:
#         #     data = CarModel.objects.get(pk=pk)  # метод get в objects моделі витягує з БД завжди 1 об'єкт по заданому id (pk)
#         # except Exception as e:
#         #     return Response('Not found')
#         # data.delete()
#         # return Response ('Deleted')
#
#         pk = kwargs.get('pk')
#         instance = get_object_or_404(CarModel, pk=pk)
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)








