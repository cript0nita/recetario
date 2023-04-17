from django.urls import path

from . import views

app_name = "recetas"
urlpatterns = [
    path('', views.index, name='index'),
    path('listado/', views.listado, name='listado'),
    path('listado/<cat_id>', views.listado, name='listado'),

    # CRUD RECETAS
    path('create/', views.create, name='create'),
    path('read/<rec_id>', views.read, name='read'),
    path('update/<rec_id>', views.update, name='update'),
    path('delete/<rec_id>', views.delete, name='delete')

    
]