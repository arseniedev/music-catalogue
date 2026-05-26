from django import forms
from django .forms import ModelForm
from .models import Album, Artist

# Create an Album form
class AlbumForm(ModelForm):
    class Meta: 
        model = Album
        fields = "__all__"

# Create an Artist form
class ArtistForm(ModelForm):
    class Meta: 
        model = Artist
        fields = "__all__"

        