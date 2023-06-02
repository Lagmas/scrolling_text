from django.shortcuts import render
from django.http import HttpResponse
from .utils import create_running_text_video
import os
from .models import RunningTextHistory


def index(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        text_color = request.POST.get('text_color', '#000000')
        bg_color = request.POST.get('bg_color', '#0000FF')
        if not (1 <= len(text) <= 40):
            return HttpResponse('Количество символов должно быть от 1 до 40', status=400)
        width = 100
        height = 100
        duration = 3
        video_response = create_running_text_video(text, text_color, bg_color, width, height, duration)
        if video_response:
            history_entry = RunningTextHistory(text=text)
            history_entry.save()
            with open(video_response, 'rb') as file:
                response = HttpResponse(file.read(), content_type='video/mp4')
                name = "running_text.mp4"
                response['Content-Disposition'] = f'attachment; filename={name}'
                file.close()
                os.remove(video_response)
                return response
    return render(request, 'ticker/index.html')