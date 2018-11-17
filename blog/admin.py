from django.contrib import admin
from .models import Post

# Register your models here.

#Chcemy, aby nasz model był widoczny w panelu admina, rejestrujemy go za pomocą poniższego polecenia:
admin.site.register(Post)
