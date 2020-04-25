from .models import Car
from .serializers import CarSerializer, CarSerializerDetail
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

class CarListCreate(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    permission_classes = (IsAuthenticated,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        self.queryset = request.user.cars.all()
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.data)
        request.data["user"] = request.user.id
        return self.create(request, *args, **kwargs)


class CarRetrieveUpdateDestroy(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    permission_classes = (IsAuthenticated,)
    queryset = Car.objects.all()
    serializer_class = CarSerializerDetail
    lookup_field = 'id'
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        if Car.objects.get(id=kwargs["id"]) in request.user.cars.all():
            return self.retrieve(request, *args, **kwargs)
        raise Http404("You cant access to this")


    def put(self, request, *args, **kwargs):
        print("some")
        if Car.objects.get(id=kwargs["id"]) in request.user.cars.all():
            #request.data["user"] = request.user.id
            print(request.data)
            return self.update(request, *args, **kwargs)
        raise Http404("You cant access to this")

    def delete(self, request, *args, **kwargs):
        if Car.objects.get(id=kwargs["id"]) in request.user.cars.all():
            return self.destroy(request, *args, **kwargs)
        raise Http404("You cant access to this")