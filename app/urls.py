from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('informacoes/<int:id>', views.dados, name="dados"),
    path('addlembrete/', views.add, name="add"),
    path('changestatus/<int:id>', views.changeStatus, name="change-status"),
    path('editarlembrete/<int:id>', views.editar, name="edit"),
    path('deletarlembrete/<int:id>',views.deletar, name="deletar")
]