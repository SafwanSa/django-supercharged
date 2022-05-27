
import os
import django
import sys


def generate_file(app_name: str, app_models: any, source: str) -> None:
    file = open(f'generator/{source}.txt', 'r')
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


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    django.setup()
    from django.apps import apps
    try:
        app_name = sys.argv[1]
    except IndexError:
        print('Error. You have to provide the app name')
        sys.exit(1)
    app_models = apps.get_app_config(app_name).get_models()
    generate_file(app_name=app_name, app_models=app_models, source='serializer')
    app_models = apps.get_app_config(app_name).get_models()
    generate_file(app_name=app_name, app_models=app_models, source='queries')
    generate_file(app_name=app_name, app_models=app_models, source='services')


if __name__ == '__main__':
    main()
