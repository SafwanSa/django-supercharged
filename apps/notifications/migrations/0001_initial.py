# Generated by Django 4.0 on 2022-01-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('type', models.CharField(choices=[('Email', 'Email'), ('SMS', 'SMS')], max_length=5)),
                ('receivers', models.TextField(help_text='This takes a comma separated value. (e.g. example@1.com,example@2.com)')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True, null=True)),
                ('data', models.TextField(blank=True, null=True)),
                ('template', models.CharField(blank=True, max_length=255, null=True)),
                ('result', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]