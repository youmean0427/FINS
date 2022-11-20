# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.user_info),
    path('isuser/<str:username>/', views.is_user),
    path('follow/<str:username>/', views.follow,),
    # path('feed/', views.feed),
]
