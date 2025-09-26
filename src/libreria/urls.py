from django.urls import path
from . import views # Importa le views dalla cartella corrente

# Questo è il registro URL della nostra app 'libreria'
urlpatterns = [
    # Se l'URL è vuoto (cioè /libreria/), chiama la funzione 'lista_libri' in views.py
    path('', views.lista_libri, name='lista_libri'),
    path('<int:pk>',views.dettaglio_libro, name='dettaglio_libro'),
    path('nuovo/', views.crea_libro, name='crea_libro'),
    path('<int:pk>/modifica/', views.modifica_libro, name='modifica_libro'),
    path('<int:pk>/elimina/', views.elimina_libro, name='elimina_libro'),
]