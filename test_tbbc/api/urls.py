from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registerContact/', views.registerContact),
    path('editingContact/<id>', views.editingContact),
    path('editContact/', views.editContact),
    path('deleteContact/<id>', views.deleteContact)
]
