from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Generate migrations for the default app'

    def handle(self, *args, **kwargs):
        app_name = 'App'  # Replace 'App' with your actual default app name
        try:
            from django.core.management import call_command
            call_command('makemigrations', app_name)
            self.stdout.write(self.style.SUCCESS(f'Successfully generated migrations for app "{app_name}"'))
        except CommandError as e:
            self.stderr.write(self.style.ERROR(f'Error generating migrations for app "{app_name}": {e}'))
