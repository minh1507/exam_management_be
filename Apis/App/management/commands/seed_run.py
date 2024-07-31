from django.core.management.base import BaseCommand
import importlib.util
import os

class Command(BaseCommand):
    help = 'Run seeds'

    def handle(self, *args, **kwargs):
        seeds_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'seeds')

        arr = os.listdir(seeds_folder)
        # arr.reverse()
        for filename in arr:
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]  # Strip .py extension
                module_path = os.path.join(seeds_folder, filename)

                # Load the module
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Optionally, call a function in the module to run seeds
                if hasattr(module, 'run'):
                    module.run()

        self.stdout.write(self.style.SUCCESS('Run seed success'))
