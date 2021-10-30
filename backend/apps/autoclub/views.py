from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny

from core.models import AutoClubModel

from .serializer import AutoClubAddUsersSerializer


class AddUsersView(UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AutoClubAddUsersSerializer
    queryset = AutoClubModel.objects.all()
    http_method_names = ('patch',) # вказується яким методом будемо оновлювати дані. В даному випадку - PATCH



