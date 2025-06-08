from django.urls import path
from app_akeno import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.inicio,name='inicio'),
    path("Ayuda", views.ayuda, name='ayuda'),
    path("Comunidad", views.comunidad, name='comunidad'),
    path("Contactos", views.contactos, name='contactos'),
    path("Creditos", views.creditos, name='creditos'),
    path("Informacion", views.informacion, name='informacion'),
    path("Iniciar Sesion", views.iniciar_sesion, name='iniciar_sesion'),
    path("Juegos", views.juegos, name='juegos'),
    path("Privacidad", views.privacidad, name='privacidad'),
    path("Registrarse", views.registrarse, name='registrarse'),
    path("Seguridad", views.seguridad, name='seguridad'),
    path("Servicios", views.servicios, name='servicios'),
    path("admin-animes/crear/", views.crear_anime, name='crear_anime'),
    path("obtener-etiquetas/", views.obtener_etiquetas, name="obtener_etiquetas"),
    path("admin-animes/", views.admin_animes, name='admin_animes'),
    path("admin-animes/eliminar/", views.eliminar_anime, name='eliminar_anime'),
    path("admin-animes/editar/<int:anime_id>/", views.editar_anime, name='editar_anime'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)