# Generated by Django 5.1 on 2024-08-12 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckServerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date_time', models.DateTimeField(auto_now_add=True, verbose_name='Запись создана')),
                ('update_date_time', models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')),
                ('text', models.TextField(verbose_name='Some text')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='Some number')),
            ],
            options={
                'verbose_name': 'Тест сервера',
                'verbose_name_plural': 'Тест сервера',
            },
        ),
    ]
