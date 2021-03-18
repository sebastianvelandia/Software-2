from django.conf.urls import url
from HistoriaApp import views

urlpatterns = [
    url(r'^autor/$',views.autorApi),
    url(r'^autor/([0-9]+)$',views.autorApi),

    url(r'^libro/$',views.libroApi),
    url(r'^libro/([0-9]+)$',views.libroApi),

    url(r'^resena/$',views.resenaApi),
    url(r'^resena/([0-9]+)$',views.resenaApi),

    url(r'^calificacion/$',views.calificacionApi),
    url(r'^calificacion/([0-9]+)$',views.calificacionApi)
]
