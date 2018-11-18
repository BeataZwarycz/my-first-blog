from django.contrib import admin
from .models import Post, Comments

# Register your models here.

#Chcemy, aby nasz model był widoczny w panelu admina, rejestrujemy go za pomocą poniższego polecenia:
#admin to jest wbudowana aplikacja!!
admin.site.register(Post)
admin.site.register(Comments)
