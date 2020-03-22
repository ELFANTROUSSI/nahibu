from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
path("",views.index,name="index"),
path("form/",views.form,name="form"),
path("addFile/",views.addFile,name="addFile"),
path("download/<str:analyse>", views.downloadResult, name='downloadResult'),
]
