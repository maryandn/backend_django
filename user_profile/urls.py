from django.urls import path
from .views import PermissionUserView, SignUpView

urlpatterns = [
    path('user', PermissionUserView.as_view()),
    path('signup', SignUpView.as_view()),

]
