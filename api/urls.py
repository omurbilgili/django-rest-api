from django.urls import path
from .views import StaticDataView,AddNumbersView


urlpatterns = [
    path('', StaticDataView.as_view(), name='static-data'),
    path('add/', AddNumbersView.as_view(), name='add-numbers'),
]