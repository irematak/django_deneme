# Generated by Django 4.1.5 on 2023-01-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0016_politika_revision_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='revision_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='liste',
            name='revision_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='prosedur',
            name='revision_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tablo',
            name='revision_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='talimat',
            name='revision_number',
            field=models.IntegerField(default=1),
        ),
    ]
