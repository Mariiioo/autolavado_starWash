# Generated by Django 3.1.3 on 2020-11-23 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StarWash', '0010_auto_20201015_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=50)),
                ('asunto', models.CharField(max_length=50)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]