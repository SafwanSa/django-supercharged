import argparse
from django.apps import apps
from django.conf import settings
from django.core.management.base import LabelCommand, CommandError, BaseCommand
from django.db import models
from scaffold.management import utils
from django.db.models.base import ModelBase


class Command(BaseCommand):
    help = 'Registers a custom admin for a desired model'

    def register_model(self, model: ModelBase):
        # Open the admin.py
        # Write the custom admin
        print(model._meta.model_name)
        print(type(model))

    def add_arguments(self, parser):
        parser.add_argument(
            '-m',
            '--model',
            required=True,
            help='The name of the model in the format <APP_NAME.MODEL_NAME>')

    def handle(self, *args, **options):
        app_model = options['model']
        app_name = app_model.split('.')[0]
        model_name = app_model.split('.')[1]
        try:
            app = apps.get_app_config(app_name)
        except LookupError:
            return utils.show_required_apps(command=self)

        models = app.get_models()
        _model = None

        for model in models:
            if model_name == model._meta.model_name:
                _model = model

        if _model is None:
            return utils.show_required_models(command=self, app=app)

        self.register_model(model=model)

        result = app_model
        self.stdout.write(self.style.SUCCESS(result))
