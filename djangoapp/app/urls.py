from django.urls import path, include
from app.views import MercadoList

urlpatterns = [
    path('', MercadoList.as_view(), name='mercado-list')
]
