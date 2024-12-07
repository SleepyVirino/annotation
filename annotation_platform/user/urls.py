from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),  # 注册
    path('login/', views.LoginView.as_view(), name='login'),  # 登录
    path('profile/', views.ProfileView.as_view(), name='profile'),  # 个人资料
    path('logout/', views.LogoutView.as_view(), name='logout'),  # 退出登录
    path('data-statistics/', views.DataStatisticsView.as_view(), name='data-statistics'),
]
