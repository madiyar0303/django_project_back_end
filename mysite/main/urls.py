from django.urls import path
from . import views


app_name = "main"


urlpatterns = {
    path("", views.homepage, name="homepage"),
    path('post/', views.individual_post, name='individual_post'),
    path("register", views.register_request, name="register"),
    path('subscribe/', views.subscribe, name='subscribe'),
}