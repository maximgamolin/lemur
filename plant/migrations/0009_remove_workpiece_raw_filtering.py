# Generated by Django 3.2.8 on 2021-10-09 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0008_workpiece_raw_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workpiece',
            name='raw_filtering',
        ),
    ]