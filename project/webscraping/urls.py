from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home, name='home'), 
    path('weather/<str:city_name>/', views.weather, name='weather'),
    path('logout/', views.logout_view, name='logout'),
    path('movies/<str:searchTerm>/', views.movien, name='movien'),
    path('actors/<str:searchTerm>/', views.actorn, name='actorn'),
    path('doubts/<str:searchTerm>/', views.doubtn, name='doubtn'),
    path('products/<str:searchTerm>/', views.pricen, name='pricen'),
    path('doubt_resolve_history/',views.doubt_resolve_history,name="doubt_resolve_history"),
    path('movie_history/',views.movie_history,name="movie_history"),
    path('price_comparator_history/', views.price_comparator_history, name='price_comparator_history'),
    path('weather_search_history/', views.weather_search_history, name='weather_search_history'),
    path('index2', views.index2, name='index2'),
    path('index5', views.index5, name='index5'),
    path('index6', views.index6, name='index6'),
    path('index9', views.index9, name='index9'),
    path('index4', views.index4, name='index4'),
    path('index10', views.index10, name='index10'),
    path('index7', views.index7, name='index7'),
    path('index8', views.index8, name='index8'),
    path('index3', views.index3, name='index3'),
    path('index/', views.index, name='index'),
    path('index', views.index, name='index'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

