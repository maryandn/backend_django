from django.urls import path
from .views import ProductView, ChangeProductView, ColorView, BrandView, EditBrandView, EditColorView, GetProductView

urlpatterns = [
    path('<int:pk>', ProductView.as_view()),
    path('change_product/<int:pk>', ChangeProductView.as_view()),
    path('get_product/<int:pk>', GetProductView.as_view()),
    path('color/', ColorView.as_view()),
    path('brand/', BrandView.as_view()),
    path('color/<int:pk>', EditColorView.as_view()),
    path('brand/<int:pk>', EditBrandView.as_view())
]
