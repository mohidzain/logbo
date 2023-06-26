from django.urls import path
from . import views
from django.urls.resolvers import URLPattern

urlpatterns=[
    path('',views.student_signin, name='student_signin'),
    path('student_signup',views.student_signup, name='student_signup'),
    path('judge_signup',views.judge_signup, name='judge_signup'),
    path('mentor_signup',views.mentor_signup, name='mentor_signup'),
    path('admin_signup',views.admin_signup, name='admin_signup'),
    path('student_profile',views.student_profile, name='student_profile'),
    path('logout',views.logout_view),
]