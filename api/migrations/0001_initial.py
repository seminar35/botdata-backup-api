# Generated by Django 3.2.7 on 2021-09-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.TextField()),
                ('Classname', models.TextField()),
                ('Projname', models.TextField()),
                ('Description', models.TextField()),
                ('contact_id', models.TextField()),
            ],
        ),
    ]
