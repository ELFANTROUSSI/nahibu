# Generated by Django 2.2.11 on 2020-03-21 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse', '0008_auto_20200321_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='kitNumber',
            field=models.OneToOneField(on_delete='CASCADE', to='analyse.NahibuClient'),
        ),
    ]
