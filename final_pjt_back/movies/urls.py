# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/vote/', views.movie_vote),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/review/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/createreview/', views.review_create),
    path('movies/<str:username>/', views.recommend_movie),
    path('movies/limit/<int:limit>', views.movie_list_limit),


    #discoveryMovie
    path('discoverymovie/', views.discovery_movie_list),
    path('discoverymovie/<int:genre_pk>/', views.discovery_movie),
    path('search/<str:keyword>/', views.search_movie),

    #keywordMovie
    path('movies/keyword/<int:keyword_pk>/', views.keyword_movie),

    #likemovie
    path('movies/like/<int:movie_pk>/', views.like),

    #still images
    path("movie/<int:movie_id>/stills/", views.still_images),

    #movie title
    path("movie/title/<int:movie_pk>/", views.movie_title),



    # # # 필수 작성
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # # optional UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]

