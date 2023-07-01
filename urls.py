from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    # path('',views.login),
    path('admin',views.admin),
    path('volunteer',views.volunteer),
    path('police',views.police),
    path('message',views.message),
    path('signup',views.signup),
    path('member',views.member),
    path('penalty',views.penalty),
    path('campaigns',views.campaigns),
    path('info',views.info),
    path('post',views.post),
    path('rehab',views.rehab),
    path('demo',views.demo),
    path('',views.registeration),
    path('candidates',views.candidates),


]