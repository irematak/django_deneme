# Generated by Django 4.1.5 on 2023-01-23 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0009_alter_tablo_revision_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablo',
            name='revision_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
