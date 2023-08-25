from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import serializer_Box_public, Box_serializer_staff
from .models import Box
import datetime


# Create your views here.
def Error(message, status=404, **kwargs):
    error = {"message": message}
    error.update(kwargs)
    return Response(error, status=status)


class Box_view(APIView):
    permission_classes = [IsAuthenticated]
    Not_Staff = "sorry you can't create box"
    qury = {
        "Length__gt":           "length_more_than",
        "Length__lt":           "length_less_than",
        "width__gt":            "breadth_more_than",
        "width__lt":            "breadth_less_than",
        "Height__gt":           "height_more_than",
        "Area__lt":             "Area_less_than",
        "Area__gt":             "Area_more_than",
        "Volume__lt":           "Volume_less_than",
        "Volume__gt":           "Volume_more_than",
        "Last_Updated__gt":     "Ceated_after",
        "Last_Updated__lt":     "Ceated_before",
        "Created_by__username": "username",
    }

    def check(self, obj, request):
        data = {}
        for i in self.qury:
            if request.GET.get(self.qury[i], ''):
                data.update({i: request.GET.get(self.qury[i])})
        return obj.filter(**data)

    def get(self, request):
        obj = Box.objects.all()
        obj = self.check(obj, request)

        if not request.user.is_staff:
            return Response(serializer_Box_public(obj, many=True).data)
        else:
            return Response(Box_serializer_staff(obj, many=True).data)

    def post(self, request):
        if not request.user.is_staff:
            return Error(self.Not_Staff)
        ser_obj = Box_serializer_staff(data=request.data)
        if ser_obj.is_valid():
            ser_obj.save(Created_by=request.user, Last_Updated=datetime.datetime.now())
            return Response(Box_serializer_staff(Box.objects.filter(), many=True).data)
        else:
            return Error("some this went worng!!", status=400, error=ser_obj.errors)

    def delete(self, request, id=None):
        if not id:
            return Error("id not found for delete")
        if not request.user.is_staff:
            return Error(self.Not_Staff)
        obj = Box.objects.filter(id=id, Created_by=request.user)
        if obj:
            obj.delete()
            return self.get(request)
        else:
            return Error("id not exist or not related to you!!")


class box_update(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id=None):
        if not id:
            return Error("id not found for delete")
        obj = Box.objects.filter(id=id)
        if obj:
            ser_obj = serializer_Box_public(obj[0], data=request.data)
            if ser_obj.is_valid():
                ser_obj.save()
                return Response(Box_serializer_staff(Box.objects.filter(), many=True).data)
            else:
                return Error("some this went worng!!", status=400, error=ser_obj.errors)
        else:
            return Error("id not exist or not related to you!!")
