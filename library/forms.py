from django.forms import ModelForm, TextInput
from library.models import Paper

class PaperForm(ModelForm):
    class Meta:
        model = Paper
        
        widgets = {
            'authors': TextInput(attrs={'cols': 80, 'rows': 20}),
        }