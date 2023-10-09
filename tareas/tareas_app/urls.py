from django.urls import path, re_path
from .views import TareaView,ProyectoView, UsuarioView
urlpatterns=[
    path('listar_usuarios/',UsuarioView.as_view(),name='listar_usuarios'),
    path('listar_usuarios/<int:id>',UsuarioView.as_view(),name='listar_usuarios'),
    path('listar_proyectos/',ProyectoView.as_view(),name='listar_proyectos'),
    path('listar_proyectos/<int:id>',ProyectoView.as_view(),name='listar_proyectos'),
    path('listar_tareas/',TareaView.as_view(),name='listar_tareas'),
    path('listar_tareas/<int:id>',TareaView.as_view(),name='listar_tareas'),
]