from django.urls import path
from .views import PermissionUserView, SignUpView

urlpatterns = [
    path('user', PermissionUserView.as_view()),
    path('signin', SignUpView.as_view()),

]
