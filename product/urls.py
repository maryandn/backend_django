from django.urls import path
from .views import ProductView, ChangeProductView, ImgView

urlpatterns = [
    path('<int:pk>', ProductView.as_view()),
    path('change_product/<int:pk>', ChangeProductView.as_view()),
    path('add_img', ImgView.as_view())
]
