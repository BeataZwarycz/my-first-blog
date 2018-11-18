#importujemy formularze i nasz model z pliku models.py
from django import forms
from .models import Post, Comments

class PostForm(forms.ModelForm): #nazwa_formularza(model)

    class Meta: #do stworzenia tego forumalarzaa wykorzysamy model 'Post'
        model = Post
        fields = ('title', 'text',) #te pola pojawią się w formularzu
#formularz do tworzenia komentarzy:
class CommentsForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('author', 'text')