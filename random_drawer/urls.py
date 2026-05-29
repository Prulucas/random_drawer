from django.contrib import admin
from django.urls import path
from drawer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/namedrawer/', views.name_drawer, name='name_drawer'),
    path('api/numberdrawer/', views.number_drawer, name='number_drawer'),
]
