from rest_framework.serializers import ModelSerializer
#
from . import models
#
from _common.serializers import custom_field

#


class HobbySerializer(custom_field.FieldSerializer):
    name_field = 'hobbys'

    class Meta:
        model = models.HobbyModel
        fields = '__all__'


class AboutYouSerializer(custom_field.FieldSerializer):
    name_field = 'about_yous'

    class Meta:
        model = models.AboutYouModel
        fields = '__all__'


class OtherNameSerializer(custom_field.FieldSerializer):
    name_field = 'other_names'

    class Meta:
        model = models.OtherNameModel
        fields = '__all__'
