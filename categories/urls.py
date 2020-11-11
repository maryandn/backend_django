from django.urls import path
from .views import CategoriesView, SubCategoriesView, EditCategoriesView, EditSubCategoriesView

urlpatterns = [
    path('', CategoriesView.as_view()),
    path('edit_category/<int:pk>/', EditCategoriesView.as_view()),
    path('sub_categories/<int:pk>/', SubCategoriesView.as_view()),
    path('edit_sub_categories/<int:pk>/', EditSubCategoriesView.as_view())
]
