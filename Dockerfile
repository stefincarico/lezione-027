# Partiamo da un'immagine Python
FROM python:3.12-slim

# Impostiamo delle variabili d'ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Creiamo e ci spostiamo nella cartella di lavoro
WORKDIR /app

# Copiamo il file delle dipendenze e le installiamo
COPY requirements.txt .
RUN pip install -r requirements.txt

# Comando per avviare il server Django.
# Questo viene eseguito automaticamente da `docker-compose up`.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
