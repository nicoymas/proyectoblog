# Generated by Django 4.0.3 on 2022-04-21 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0002_remove_mensajeria_cuerpo_mensajeria_conten_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensajeria',
            old_name='conten_post',
            new_name='cuerpo',
        ),
    ]
