# Generated by Django 4.1.5 on 2023-01-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0012_alter_prosedur_revision_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prosedur',
            name='revision_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]