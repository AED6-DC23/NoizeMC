from django.shortcuts import render


def checklist(request):
    return render (request, 'checklist.html')


def afisha(request):
    return render (request, 'afisha.html')


def music(request):
    return render (request, 'music.html')


def video(request):
    return render (request, 'video.html')


def merch(request):
    return render (request, 'merch.html')


def youtube(request):
    return render (request, 'youtube.html')