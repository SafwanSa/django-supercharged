from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
from django.apps import apps


def show_required_apps(command: BaseCommand) -> None:
    command.stderr.write('This command requires an existing app name as argument')
    command.stderr.write('Available apps:')
    app_labels = settings.LOCAL_APPS
    for label in sorted(app_labels):
        command.stderr.write('    %s' % label)
    return


def show_required_models(command: BaseCommand, app: any) -> None:
    models = app.get_models()
    app_name = app.name.split('.')[1]
    command.stderr.write(f'This command requires an existing model of {app_name} app')
    command.stderr.write(f'Available models for {app_name} app:')
    for model in models:
        command.stderr.write('    %s' % model._meta.model_name)
    return


def generate_file(app_name: str, source: str) -> None:
    app_models = apps.get_app_config(app_name).get_models()
    path = f"{Path(__file__).parent}/file_generator_templates/{source}.txt"
    file = open(path, 'r')
    content = file.readlines()
    file.close()
    file = open(f'apps/{app_name}/{source}.py', 'w')
    imports = [line for line in content if 'import' in line]
    file.writelines(imports)
    content = [line for line in content if line not in imports]
    temp_content = list(content)

    for model in app_models:
        file.write('\n')
        while content:
            start_loop_index = content.index('{loop}\n')
            end_loop_index = content.index('{endloop}\n') + 1
            for line in content[start_loop_index:end_loop_index]:
                if not 'loop' in line:
                    file.write(
                        line.replace(
                            '{{model_name}}',
                            model._meta.object_name).replace(
                            '{{model_verbose}}',
                            model._meta.verbose_name)
                    )
                content.remove(line)
        content = list(temp_content)
    file.close()
