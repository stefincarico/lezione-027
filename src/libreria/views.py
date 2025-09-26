from django.shortcuts import render, get_object_or_404,redirect

from .forms import LibroForm
from .models import Libro

def lista_libri(request):
    # ... (questa view non cambia) ...
    tutti_i_libri = Libro.objects.all()
    context = {'elenco_libri': tutti_i_libri}
    return render(request, 'libreria/lista_libri.html', context)

# --- NUOVA VIEW ---
def dettaglio_libro(request, pk):
    # 1. Recupera il singolo oggetto libro usando la Primary Key (pk)
    # get_object_or_404 è una scorciatoia utilissima:
    # Prova a prendere l'oggetto. Se non esiste, solleva automaticamente un errore 404.
    libro_singolo = get_object_or_404(Libro, pk=pk)

    # 2. Prepara il context per il template
    context = {
        'libro': libro_singolo,
    }

    # 3. Renderizza il nuovo template di dettaglio
    return render(request, 'libreria/libro_dettaglio.html', context)

# --- NUOVA VIEW ---
def crea_libro(request):
    # Logica per la richiesta POST (invio dati)
    if request.method == 'POST':
        # Crea un'istanza del form e la popola con i dati dalla richiesta (binding)
        form = LibroForm(request.POST)
        # Controlla se il form è valido
        if form.is_valid():
            form.save() # Salva il nuovo libro nel database
            return redirect('lista_libri') # Reindirizza alla lista dei libri
    # Logica per la richiesta GET (visualizzazione)
    else:
        form = LibroForm() # Crea un form vuoto

    context = {'form': form}
    return render(request, 'libreria/libro_form.html', context)


# --- VIEW DI AGGIORNAMENTO ---
def modifica_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        # Passiamo 'instance=libro' per dire al form quale oggetto modificare
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libri')
    else:
        # Passiamo 'instance=libro' per pre-compilare il form con i dati esistenti
        form = LibroForm(instance=libro)
    
    context = {'form': form}
    return render(request, 'libreria/libro_form.html', context)

# --- VIEW DI ELIMINAZIONE ---
def elimina_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libri')
    
    context = {'libro': libro}
    return render(request, 'libreria/libro_confirm_delete.html', context)