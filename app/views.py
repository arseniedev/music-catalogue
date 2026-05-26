from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Album, Artist
from .forms import AlbumForm, ArtistForm

def home(request):
    return render(request, "music_catalogue/homepage.html")

def auth(request):
    return render(request, "music_catalogue/authentication.html")


def album_details(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, "music_catalogue/album_details.html", {"album": album})

def artist_details(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    return render(request, "music_catalogue/artist_details.html", {"artist": artist})

def all_albums(request):
    items = Album.objects.all()
    # return HttpResponse("This is the homepage." % name)
    title = "Albums"
    return render(request, "music_catalogue/albums.html", {"album_list" : items, "page_title" : title})

def all_artists(request):
    items = Artist.objects.all()
    title = "Artist"
    return render(request, "music_catalogue/artists.html", {"artist_list" : items, "page_title" : title})


@login_required
def add_album(request):
    submitted = False
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-album?submitted=True')
    else:
        form = AlbumForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "music_catalogue/add_album.html", {'form': form, 'submitted': submitted})


@login_required
def add_artist(request):
    submitted = False
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-artist?submitted=True')
    else:
        form = ArtistForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "music_catalogue/add_artist.html", {'form': form, 'submitted': submitted})