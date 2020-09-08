from django.urls import path
from .views import PermissionUserView, SignInView

urlpatterns = [
    path('', PermissionUserView.as_view()),
    path('signin', SignInView.as_view()),

]
