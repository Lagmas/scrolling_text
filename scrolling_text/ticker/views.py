# from django.shortcuts import render


# from django.http import HttpResponse


# # Главная страница
# # def index(request):    
# #     return HttpResponse('Главная страница')

# def index(request):
#     template = 'ticker/index.html'
#     return render(request, template)

# app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
from .utils import create_running_text_video

def index(request):
    template = 'ticker/index.html'
    if request.method == 'POST':
        text = request.POST['text']
        video_name = f'running_text_{text}.mp4'
        create_running_text_video(text, 100, 100, 3)

        video = Video.objects.create(name=video_name, file=video_name)
        video.save()

        return HttpResponse(f"Видео успешно создано: <a href='/media/{video.file}'>{video.name}</a>")
    
    return render(request, template)
