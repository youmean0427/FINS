# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.user_info),
    path('isuser/<str:username>/', views.is_user),
    path('follow/<str:username>/', views.follow,),
    path('followings/', views.followinglist),

    path('feedlist/<str:username>/', views.feed_list),
    path('feed/<int:feed_pk>/',views.feed_detail),
    path('feed/<int:feed_pk>/like/', views.feed_like),
    path('feed/<int:feed_pk>/likecheck/', views.feed_like_check)
]

