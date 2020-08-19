from django.conf.urls import url
from .views import shopView
from django.urls import path

app_name = "shop"

urlpatterns = [
    path('product/<int:shop_id>/', shopView.as_view()),
]



























