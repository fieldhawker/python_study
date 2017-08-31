from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from project.services import scraping_service


def index(request):

    schedules = scraping_service.ScrapingService.get_blueimpulse_schedule()
    print(schedules)

    return render(request, 'event/index.html', {
        'hoge': 'test string',
        'fuga': '<br>tag</br>',
        'schedules': schedules,
    })
