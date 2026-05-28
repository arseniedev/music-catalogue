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



class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )