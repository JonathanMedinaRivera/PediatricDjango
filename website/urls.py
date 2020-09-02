from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('home.html',views.home, name="home"),
    path('contact_us.html',views.contact_us, name="contact"),
    path('about_us.html',views.about_us, name="about"),
    path('blog.html',views.blog, name="blog"),
    path('team.html',views.team, name="team"),
    path('services.html',views.services, name="services"),
]
