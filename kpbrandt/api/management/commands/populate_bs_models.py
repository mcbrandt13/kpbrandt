from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    help = 'Populate models for generating corporate bs statements. ' \
           'Provide a .py file consisting of dict'

    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, *args, **options):
        with open(options['file'], 'r') as f:
            values = eval(f.read())
            for model_name, words_list in values.items():
                m = apps.get_model('api', model_name)
                for word in words_list:
                    x, created = m.objects.get_or_create(word=word)
                    if created:
                        self.stdout.write('adding %s to %s' %
                                          (word, model_name))
                    else:
                        self.stdout.write('%s exists in model %s' %
                                          (word, model_name))
