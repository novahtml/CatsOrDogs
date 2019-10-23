from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    path('upload/',views.upload_view, name='upload_image'),
    url(r'^$',views.index, name='index'),

]