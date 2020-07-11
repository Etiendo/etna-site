from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from etna.core.models import TapasCourse
from etna.core.models import PresentationText

def index(request):
    template = loader.get_template('index.html')
    try:
      restaurant_presentation = PresentationText.objects.get(
          text_type='RESTAURANT')
    except PresentationText.DoesNotExist:
      restaurant_presentation = None

    try:
      wine_presentation = PresentationText.objects.get(text_type='WINE')
    except PresentationText.DoesNotExist:
      wine_presentation = None

    try:
      tapas_courses = list(TapasCourse.objects.all())
      tapas_courses.sort(key=lambda tapas: tapas.order)
    except TapasCourse.DoesNotExist:
      tapas_courses = None

    context = {
      'enabled': True,
      'methodology': True,
      'restaurant_presentation': restaurant_presentation,
      'wine_presentation': wine_presentation,
      'tapas_courses': tapas_courses
    }

    return HttpResponse(template.render(context, request))
