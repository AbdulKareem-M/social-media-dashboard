from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.UserRegistrationView.as_view(), name='user_register'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
]
