# myapp/management/commands/runserver_custom.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Run migrations'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Run migration success'))
        from django.core.management import call_command
        call_command('migrate')
