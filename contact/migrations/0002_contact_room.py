# Generated by Django 4.2.3 on 2023-11-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='room',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
