import argparse
from django.apps import apps
from django.conf import settings
from django.core.management.base import LabelCommand, CommandError, BaseCommand
from django.db import models
from scaffold.management import utils


class Command(BaseCommand):
    help = 'Generates a serializers.py file for a desired app'

    def add_arguments(self, parser):
        parser.add_argument('--app-name', required=True, help='The app name of your generated serializers.py file')

    def handle(self, *args, **options):
        app_name = options['app_name']
        try:
            app = apps.get_app_config(app_name)
        except LookupError:
            return utils.show_required_apps(command=self)

        utils.generate_file(app_name=app_name, source='serializers')

        result = app_name
        print(app_name)
        self.stdout.write(self.style.SUCCESS(result))
