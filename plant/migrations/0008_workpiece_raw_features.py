# Generated by Django 3.2.8 on 2021-10-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0007_rename_raw_features_workpiece_raw_joins'),
    ]

    operations = [
        migrations.AddField(
            model_name='workpiece',
            name='raw_features',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
