from django.core.management.base import BaseCommand, CommandError
from apps.utilities.models import Config
import json


class Command(BaseCommand):
    help = 'Import settings from a json file.'

    def add_arguments(self, parser):
        parser.add_argument('settings_dir', nargs='+', type=str)

    def handle_configs(self, data: dict) -> tuple:
        created_counter = 0
        counter = 0
        for instance in data:
            new_config, created = Config.objects.get_or_create(
                key=instance['key'],
            )
            if created:
                created_counter += 1
                new_config.value = instance['value']
                new_config.description = instance['description']
                new_config.is_system = instance['is_system']
                new_config.is_private = instance['is_private']
                new_config.tag = instance['tag']
                new_config.save()
            else:
                counter += 1
                new_config.is_system = instance['is_system']
                if new_config.tag == None:
                    new_config.tag = instance['tag']
                new_config.save()
        return created_counter, counter

    def handle(self, *args, **options):
        try:
            settings_dir = options['settings_dir'][0]
        except:
            raise CommandError(
                'Please pass the directory name of a json file.')
        f = open(settings_dir)
        data = json.load(f)

        configs_created_counter, configs_updated_counter = self.handle_configs(
            data.get('configs'))
        
        configs_output = '\n{} configs were created.\n{} configs already exists.\n'.format(
            configs_created_counter, configs_updated_counter)
        
        result = configs_output
        self.stdout.write(self.style.SUCCESS(result))
