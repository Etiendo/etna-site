from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from etna.core.models import Tapas
from etna.core.models import TexteDePresentation

def index(request, language=''):
    template = loader.get_template('index.html')
    if not language:
      language='FR'

    try:
      restaurant_presentation = TexteDePresentation.objects.get(
          type_de_texte='RESTAURANT', langue=language)
    except TexteDePresentation.DoesNotExist:
      restaurant_presentation = None

    try:
      wine_presentation = TexteDePresentation.objects.get(type_de_texte='WINE', langue=language)
    except TexteDePresentation.DoesNotExist:
      wine_presentation = None

    try:
      tapas_courses = list(Tapas.objects.all())
      tapas_courses = list(filter(lambda tapas: tapas.langue == language, tapas_courses))
      tapas_courses.sort(key=lambda tapas: tapas.ordre)
    except Tapas.DoesNotExist:
      tapas_courses = None

    if language == 'EN':
      language = 'FR'
    else:
      language = 'EN'

    context = {
      'enabled': True,
      'methodology': True,
      'restaurant_presentation': restaurant_presentation,
      'wine_presentation': wine_presentation,
      'tapas_courses': tapas_courses,
      'language': language,
    }

    return HttpResponse(template.render(context, request))
