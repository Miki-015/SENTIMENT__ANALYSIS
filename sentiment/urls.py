from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("", views.intro, name="Introduction"),
    path("analyse/", views.analyse, name="Analyse"),
    path("final_output/",views.final_output,name="user_input"),
    path("ans/",views.ans,name="ans"),
    path("get_ans/",views.get_ans,name="get_ans"),
    path("form/",views.form,name="form"),
    path("upload/",views.upload,name="upload")

]


