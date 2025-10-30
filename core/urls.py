from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cursos, name='lista_cursos'),
    path('curso/novo/', views.criar_curso, name='criar_curso'),
    path('curso/<int:id>/editar/', views.editar_curso, name='editar_curso'),
    path('curso/<int:id>/deletar/', views.deletar_curso, name='deletar_curso'),
]
