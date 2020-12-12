from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static
urlpatterns = [
    path('', views.index,name ='index'),
    path('create',views.create,name = 'create'),
    path('completed',views.completed,name = 'completed'),
    path('view',views.view,name = 'view'),
    path('edit',views.edit,name = 'edit'),
    path('save_edit',views.save_edit,name = 'save_edit'),

]