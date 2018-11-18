#importujemy formularze i nasz model z pliku models.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm): #nazwa_formularza(model)

    class Meta: #do stworzenia tego forumalarzaa wykorzysamy model 'Post'
        model = Post
        fields = ('title', 'text',) #te pola pojawią się w formularzu