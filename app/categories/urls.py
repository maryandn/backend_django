from django.urls import path
from .views import CategoriesView, SubCategoriesView

urlpatterns = [
    path('', CategoriesView.as_view()),
    path('subcategories/<int:pk>/', SubCategoriesView.as_view())
]
