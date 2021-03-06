from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    return render(request, 'home/room.html', {'room_name': room_name, 'username': username})
