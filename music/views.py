from django.views import generic
from . models import Album, Song
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import UserForm

# where to redirect to after deletion
from django.urls import reverse_lazy

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


class UpdateAlbumView(generic.UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class DeleteAlbumView(generic.DeleteView):
    model = Album

    # redirect to homepage after deletion
    success_url = reverse_lazy('music:index')


class SignupView(View):
    form_class = UserForm
    template_name = 'music/signup_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})
