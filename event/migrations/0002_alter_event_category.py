# Generated by Django 4.2.3 on 2023-12-05 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('dicas', 'Dicas'), ('eventos', 'Eventos')], max_length=20),
        ),
    ]
