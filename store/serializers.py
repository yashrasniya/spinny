from rest_framework import serializers
from .models import Box
from rest_framework.fields import empty


class serializer_Box_public(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = [
            'id',
            'Length',
            'width',
            'Height',
            'Area',
            'Volume'
        ]
        read_only=[
            'Area',
            'Volume'
        ]


class Box_serializer_staff(serializers.ModelSerializer):
    Created_by = serializers.SerializerMethodField()
    Length = serializers.FloatField(required=True)
    width = serializers.FloatField(required=True)
    Height = serializers.FloatField(required=True)
    Last_Updated = serializers.DateTimeField(required=False)
    class Meta:
        model = Box
        fields = [
            'id',
            'Length',
            'width',
            'Height',
            'Area',
            'Volume',
            'Created_by',
            'Last_Updated'
        ]



    def get_Created_by(self, obj):
        return obj.Created_by.username
