from django.urls import path, include

app_name = "api_v1"

urlpatterns = [
    path('bmi/', include('apps.bmi.api.v1.urls'))
]
