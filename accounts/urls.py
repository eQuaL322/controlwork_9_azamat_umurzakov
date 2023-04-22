from django.urls import path

from accounts.views import ProfileView, LoginView

urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),

]
