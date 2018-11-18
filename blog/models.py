from django.db import models
from django.utils import timezone

# Tworzę swój 'model' tutaj.

class Post(models.Model): #definiujemy nasz model, class- oznacza, że tworzymy obiekt
# Post - nazwa modelu, models.Model - oznacza to, że nasz obiekt jest modelem Django, będzie go przechowywał w bazie danych
# Poniżej dodajemy właściwości do modelu i definiujemy ich typy
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#np.: models.ForeignKey - odnośnik do innego modelu
    title = models.CharField(max_length=200) #ograniczona liczba znaków
    text = models.TextField() #tekst z nieograniczoną liczbą znakó
    created_date = models.DateTimeField(
            default=timezone.now) #ustawiamy datę i godzinę
    published_date = models.DateTimeField(
            blank=True, null=True)
#def oznacza, że jest to metoda, publish - jej nazwa
    def publish(self): # a to jest metoda(czynność)
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

"""Ten model jest odpowiedzialny za dodawanie komentarzy
text - pole na komentarz, author - pole na wpisanie imienia, created_date - data publikacji"""
class Comments(models.Model):
    text = models.TextField() #miejsce na tekst
    created_date = models.DateTimeField(default=timezone.now) #wyświetli się data publikacji
    author = models.CharField(max_length=20)
#wyświetli autora
    def __str__(self):
        return self.author +' napisał komentarz: ' + self.text



