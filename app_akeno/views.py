from django.shortcuts import render, redirect, get_object_or_404
from .models import Anime, Temporada, Episodio, Etiqueta
from django.http import JsonResponse

# Create your views here.
def inicio(request):
    return render(request, "HTML/Inicio.html")
def registrarse(request):
    return render(request, "HTML/Registrarse.html")
def iniciar_sesion(request):
    return render(request, "HTML/Iniciar sesion.html")
def ayuda(request):
    return render(request, "HTML/Ayuda.html")
def comunidad(request):
    return render(request, "HTML/Comunidad.html")
def contactos(request):
    return render(request, "HTML/Contactos.html")
def creditos(request):
    return render(request, "HTML/Creditos.html")
def informacion(request):
    return render(request, "HTML/Informacion.html")
def juegos(request):
    return render(request, "HTML/Juegos.html")
def privacidad(request):
    return render(request, "HTML/Privacidad.html")
def seguridad(request):
    return render(request, "HTML/Seguridad.html")
def servicios(request):
    return render(request, "HTML/Servicios.html")
def crear_anime(request):
    return render(request, "HTML/crear_Anime.html")



def crear_anime(request):
    if request.method == 'POST':
        # 1. Datos básicos del anime
        nombre         = request.POST.get('nombre', '').strip()
        descripcion    = request.POST.get('descripcion', '').strip()
        portada        = request.FILES.get('portada')
        portada_grande = request.FILES.get('portada_grande')

        anime = Anime.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            portada=portada,
            portada_grande=portada_grande
        )

        # 2. Etiquetas (esperamos un campo oculto 'etiquetas' con nombres separados por coma)
        etiquetas_raw = request.POST.get('etiquetas', '')
        for et in [e.strip() for e in etiquetas_raw.split(',') if e.strip()]:
            etiqueta_obj, _ = Etiqueta.objects.get_or_create(nombre=et)
            anime.etiquetas.add(etiqueta_obj)

        # 3. Temporadas y episodios dinámicos
        # Buscamos todos los inputs de nombre de episodio
        for key in request.POST:
            if not key.startswith('nombre_episodio_'):
                continue
            # key == 'nombre_episodio_{t}_{e}'
            _, _, t_str, e_str = key.split('_')
            t = int(t_str)
            e = int(e_str)
            nombre_ep = request.POST.get(key, '').strip()

            temporada, _ = Temporada.objects.get_or_create(anime=anime, numero=t)

            # Recuperamos archivos de episodio
            video_field      = request.FILES.get(f'video_{t}_{e}')
            portada_ep_field = request.FILES.get(f'portada_ep_{t}_{e}')

            episodio = Episodio(
                temporada=temporada,
                nombre=nombre_ep
            )
            if video_field:
                episodio.video = video_field
            if portada_ep_field:
                episodio.portada_ep = portada_ep_field
            episodio.save()

        # 4. Una vez guardado, redirigimos (o podrías renderizar con 'exito': True)
        return redirect('crear_anime')

    return render(request, 'HTML/crear_Anime.html')

def obtener_etiquetas(request):
    if request.method == "GET":
        etiquetas = list(Etiqueta.objects.values_list("nombre", flat=True))
        return JsonResponse({"etiquetas": etiquetas})
    
def admin_animes(request):
    animes = Anime.objects.all()
    return render(request, 'HTML/admin_animes.html', {'animes': animes})

def eliminar_anime(request):
    if request.method == 'POST':
        anime_id = request.POST.get('anime_id')
        try:
            anime = Anime.objects.get(pk=anime_id)

            # Guardamos las etiquetas antes de eliminar el anime
            etiquetas_asociadas = list(anime.etiquetas.all())

            # Borrar archivos de portada y portada grande
            if anime.portada:
                anime.portada.delete(save=False)
            if anime.portada_grande:
                anime.portada_grande.delete(save=False)

            # Eliminar el anime (Django elimina automáticamente la relación ManyToMany)
            anime.delete()

            # Eliminar etiquetas que ya no estén asociadas a ningún otro anime
            for etiqueta in etiquetas_asociadas:
                if etiqueta.anime_set.count() == 0:
                    etiqueta.delete()

            return JsonResponse({'ok': True})
        except Anime.DoesNotExist:
            return JsonResponse({'ok': False})
    return JsonResponse({'ok': False})

def editar_anime(request, anime_id):
    # lógica para mostrar y guardar edición
    anime = get_object_or_404(Anime, pk=anime_id)
    return render(request, 'HTML/editar_Anime.html', {'anime': anime})