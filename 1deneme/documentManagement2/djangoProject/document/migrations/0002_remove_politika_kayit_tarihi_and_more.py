# Generated by Django 4.1.5 on 2023-01-03 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='politika',
            name='kayit_tarihi',
        ),
        migrations.RemoveField(
            model_name='politika',
            name='revision_date',
        ),
        migrations.RemoveField(
            model_name='politika',
            name='revision_number',
        ),
    ]
