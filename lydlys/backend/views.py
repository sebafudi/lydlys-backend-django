from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from backend.models import Song, Show
from backend.serializers import SongSerializer, ShowSerializer


@csrf_exempt
def song_list(request):
    """
    List all songs, or create a new song.
    """
    if request.method == "GET":
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def song_detail(request, pk):
    """
    Retrieve, update or delete a song.
    """
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = SongSerializer(song)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SongSerializer(song, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        song.delete()
        return HttpResponse(status=204)


@csrf_exempt
def show_list(request):
    """
    List all shows, or create a new show.
    """
    if request.method == "GET":
        shows = Show.objects.all()
        serializer = ShowSerializer(shows, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ShowSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def show_detail(request, pk):
    """
    Retrieve, update or delete a show.
    """
    try:
        show = Show.objects.get(pk=pk)
    except Show.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ShowSerializer(show)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ShowSerializer(show, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        show.delete()
        return HttpResponse(status=204)
