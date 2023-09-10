# agenda/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_contactos, name='lista_contactos'),
    path('crear/', views.crear_contacto, name='crear_contacto'),
    path('editar/<int:contacto_id>/', views.editar_contacto, name='editar_contacto'),
    path('eliminar/<int:contacto_id>/', views.eliminar_contacto, name='eliminar_contacto'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]
