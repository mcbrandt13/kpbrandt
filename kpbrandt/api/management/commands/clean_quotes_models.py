from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    help = 'Wipe all quotes in db and repopulate with 5 standard ones.'

    def handle(self, *args, **options):
        m = apps.get_model('api', 'Quotes')
        count, info = m.objects.all().delete()
        self.stdout.write('Deleted %s Quotes' % count)

        base = [{'phrase': 'He had decided to live forever or die in the attempt, and his only '
                           'mission each time he went up was to come down alive.',
                 'author': 'Joseph Heller'},
                {'phrase': 'Certain things, they should stay the way they are. You ought to be '
                           'able to stick them in one of those big glass cases and just leave '
                           'them alone.',
                 'author': 'Holden Caulfield'},
                {'phrase': 'The only consistent feature in all of your dissatisfying relationships'
                           ' is you.', 'author': 'Unknown'},
                {'phrase': 'You can make big money as long as you let yourself make it.',
                 'author': 'Tom Wilsonberg, Home Movies'},
                ]
        [m(**quote).save() for quote in base]
        self.stdout.write('Repopulated Quotes')
