from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Añadido

urlpatterns = [
    path('signup/', views.UserCreateAndLoginView.as_view(), name='signup'),  # Cambiado
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='accounts/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('user_delete/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),
]