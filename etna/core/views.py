from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from etna.core.models import TapasCourse
from etna.core.models import PresentationText

def index(request):
    template = loader.get_template('index.html')
    restaurant_presentation = PresentationText.objects.get(
        text_type='RESTAURANT')
    wine_presentation = PresentationText.objects.get(text_type='WINE')

    context = {
      'enabled': True,
      'methodology': True,
      'restaurant_presentation': restaurant_presentation,
      'wine_presentation': wine_presentation,
      'tapas_courses': TapasCourse.objects.all()
    }

    return HttpResponse(template.render(context, request))
