from django.shortcuts import render, render_to_response

from django.http import HttpResponse


def index(request):
    'Display map'
    return render_to_response('waypoints/index.html', {
    })