from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# from django.template import loader
from .models import Album


# Create your views here.
# def index(request):
#     return HttpResponse("<h3>The music app homepage</h3>")

# def index(request):
#     all_albums = Album.objects.all()
#     html = ''
#     for album in all_albums:
#         url = '/music/' + str(album.id) + '/'
#         html += '<a href="' + url + '">' + album.album_title + '</a><br>'
#     return HttpResponse(html)

# def index(request):
#     all_albums = Album.objects.all()
#     template = loader.get_template('music/index.html')
#     context = {
#         'all_albums': all_albums,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    albums = Album.objects.all()
    context = {'albums': albums, }
    return render(request, 'music/index.html', context)


def detail(request, album_id):

    # return HttpResponse("<h2>Details for Album id:" + str(id) + "</h2>")
    # try:
    #     album = Album.objects.get(pk=album_id)
    #     context = {'album': album}
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exist")

    album = get_object_or_404(Album, pk=album_id)
    context = {'album': album}
    return render(request, 'music/detail.html', context)