# Generated by Django 2.0.7 on 2018-12-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20181104_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postreport',
            name='reason',
            field=models.CharField(choices=[('SPAM', 'Spam'), ('VIOLENCE', 'Violence Content')], default=None, max_length=255),
        ),
    ]
