# Generated by Django 4.1.5 on 2023-01-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0015_rename_rrevision_date_form_revision_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='politika',
            name='revision_number',
            field=models.IntegerField(default=1),
        ),
    ]
