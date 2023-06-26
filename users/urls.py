from django.urls import path
from . import views
from django.urls.resolvers import URLPattern

urlpatterns=[
    path('',views.signin, name='signin'),
    path('signup',views.signup, name='signup'),
    path('home',views.home, name='home'),
    path('logout',views.logout_view),
]