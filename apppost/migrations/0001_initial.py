# Generated by Django 4.0.3 on 2022-04-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=40)),
                ('subtitulo', models.CharField(max_length=40)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='post')),
                ('conten_post', models.TextField()),
                ('autor', models.CharField(max_length=40)),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]