from django.urls import path
from . import views
from django.urls.resolvers import URLPattern

urlpatterns=[
    path('',views.student_signin, name='student_signin'),
    path('teacher_signin',views.teacher_signin, name='teacher_signin'),
    path('judge_signin',views.judge_signin, name='judge_signin'),
    path('mentor_signin',views.mentor_signin, name='mentor_signin'),
    path('admin_signin',views.admin_signin, name='admin_signin'),

    path('student_signup',views.student_signup, name='student_signup'),
    path('teacher_signup',views.teacher_signup, name='teacher_signup'),
    path('judge_signup',views.judge_signup, name='judge_signup'),
    path('mentor_signup',views.mentor_signup, name='mentor_signup'),
    path('admin_signup',views.admin_signup, name='admin_signup'),
    
    path('step_1',views.step_1, name='step_1'),
    path('step_2',views.step_2, name='step_2'),
    
    path('team_portal',views.team_portal, name='team_portal'),
    path('view_team',views.view_team, name='view_team'),
    
    path('student_portal',views.student_portal, name='student_portal'),
    path('student_profile',views.student_profile, name='student_profile'),

    path('teacher_profile',views.teacher_profile, name='teacher_profile'),

    path('logout',views.logout_view, name='logout'),
]