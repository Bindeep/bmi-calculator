from django.urls import path
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'base.html'


urlpatterns = [
    path('', IndexView.as_view())
]
