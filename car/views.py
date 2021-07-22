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


class MyView(APIView):
    def get(self, *args, **kwargs):
        params = self.request.query_params
        name = params.get('name')
        print(name)
        return Response('hello from get')

    def post(self, *args, **kwargs):
        return Response('hello from post')

    def put(self, *args, **kwargs):
        return Response('hello from put')

    def patch(self, *args, **kwargs):
        return Response('hello from patch')
    def delete(self, *args, **kwargs):
        return Response('hello from delete')

class MyViewSecond(APIView):
    def get(self, id, *args, **kwargs):
        print(kwargs.get('id'))
        return Response('Ok')
