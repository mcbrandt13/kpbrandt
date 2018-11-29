from django.contrib import admin
from .models import Adverb, Verb, Adjective, Noun, Quotes

admin.site.register([x for x in [Adverb, Verb, Adjective, Noun, Quotes]])
