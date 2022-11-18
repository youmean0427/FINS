# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/review/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/createreview/', views.review_create),

    #discoveryMovie
    path('discoverymovie/', views.discovery_movie_list),
    path('discoverymovie/<int:genre_pk>/', views.discovery_movie),

    # # # 필수 작성
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # # optional UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]

