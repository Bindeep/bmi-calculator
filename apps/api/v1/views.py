from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.api.v1.serializers import BMIListSerializer, BMICreateSerializer
from apps.bmi.models import BMI
from apps.bmi.utils import calculate_bmi
from apps.core.viewsets import ListViewSet


class BMIViewSet(ListViewSet):
    queryset = BMI.objects.all()
    serializer_class = BMIListSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    @action(detail=False, methods=['post'])
    def calculate(self, request, *args, **kwargs):
        ser = BMICreateSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        weight = ser.data.get('weight')
        height = ser.data.get('height')
        bmi = calculate_bmi(
            weight,
            height
        )
        bmi_obj = BMI.objects.create(
            weight=weight, height=height, bmi=bmi
        )
        return Response({
            'bmi': bmi,
            'weight_group': bmi_obj.weight_group
        })
