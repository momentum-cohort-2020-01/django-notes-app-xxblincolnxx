from django.forms import ModelForm
from .models import Note

class NewNote(ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'body',)