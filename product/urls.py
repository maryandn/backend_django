from django.urls import path
from .views import ProductView, ChangeProductView

urlpatterns = [
    path('<int:pk>', ProductView.as_view()),
    path('change_product/<int:pk>', ChangeProductView.as_view())
]
