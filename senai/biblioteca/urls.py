from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("infantil.html", views.infantil, name="infantil"),
    path("romance.html", views.romance, name="Romance"),
    path("Fantasia.html", views.Fantasia, name="Fantasia"),
    path("Fic.html", views.Fic, name="Fic"),
    path("carrinho.html", views.carrinho, name="carrinho"),
    path("crud", views.crud, name="crud"),
   
    path("novidade", views.nov, name="novidade"),
    path('adicionar', views.create, name="create"),
    path('atualizar/<int:id>/', views.update, name='update'),
    path('editar/<int:id>', views.edit, name="edit"),
    path('deletar/<int:id>', views.delete, name='delete'),
    path('login', views.login, name='login'),
    path('admin', views.admin, name="admin")
 
    

]