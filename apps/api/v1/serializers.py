from apps.bmi.models import BMI
from apps.core.serializers import DynamicFieldsModelSerializer


class BMIListSerializer(DynamicFieldsModelSerializer):

    class Meta:
        fields = '__all__'
        model = BMI


class BMICreateSerializer(DynamicFieldsModelSerializer):

    class Meta:
        fields = ('weight', 'height')
        model = BMI
