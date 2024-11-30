from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns =  [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
]
