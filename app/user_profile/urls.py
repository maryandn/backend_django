from django.urls import path
from .views import UserView, SignInView

urlpatterns = [
    path('', UserView.as_view()),
    path('signin', SignInView.as_view()),

]
