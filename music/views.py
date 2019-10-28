from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# from django.template import loader

from django.views import generic
from . models import Album, Song
from django.urls import reverse

# old method using function based views
# def index(request):
#     albums = Album.objects.all()
#     context = {'albums': albums, }
#     return render(request, 'music/index.html', context)
#
#
# def detail(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     context = {'album': album}
#     return render(request, 'music/detail.html', context)
#
#
# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         context = {
#             'album': album,
#             'error_message': 'You did not select any song',
#         }
#         return render(request, 'music/detail.html', context)
#     else:
#         if selected_song.is_favorite:
#             selected_song.is_favorite = False
#             selected_song.save()
#         else:
#             selected_song.is_favorite = True
#             selected_song.save()
#
#         context = {
#             'album': album
#         }
#         return render(request, 'music/detail.html', context)


# new method using class based views
class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'albums'

    # use function to get model / database
    # default name in index page will be album list
    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DeleteView):
    model = Album
    template_name = 'music/detail.html'


class CreateAlbumView(generic.CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
