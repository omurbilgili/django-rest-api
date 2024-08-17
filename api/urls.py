from django.urls import path
from .views import StaticDataView,AddNumbersView,SampleDataView


urlpatterns = [
    path('', StaticDataView.as_view(), name='static-data'),
    path('numbers/',SampleDataView.as_view(),name='sample-data'),
    path('add/', AddNumbersView.as_view(), name='add-numbers'),
]